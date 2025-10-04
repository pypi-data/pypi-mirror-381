"""
Unit tests for WizVulnerabilityIntegration
"""

import logging
import unittest
from unittest.mock import patch, MagicMock

from regscale.core.app.utils.api_handler import APIHandler
from regscale.integrations.commercial.wizv2.scanner import WizVulnerabilityIntegration
from regscale.integrations.commercial.wizv2.variables import WizVariables
from regscale.integrations.variables import ScannerVariables
from regscale.models import regscale_models
from tests.regscale.integrations.commercial.wizv2 import (
    asset_nodes,
    vuln_nodes,
    PROJECT_ID,
    PLAN_ID,
)

logger = logging.getLogger("regscale")


class TestWizVulnerabilityIntegration(unittest.TestCase):
    regscale_version = APIHandler().regscale_version
    project_id = PROJECT_ID
    plan_id = PLAN_ID

    def clean_plan(self, plan_id):
        if self.regscale_version >= "5.64.0" or self.regscale_version == "localdev":
            for scan in regscale_models.ScanHistory.get_all_by_parent(
                plan_id, regscale_models.SecurityPlan.get_module_string()
            ):
                for vuln_mapping in regscale_models.VulnerabilityMapping.find_by_scan(scan.id):
                    vuln_mapping.delete()
                # No delete api
                # scan.delete()
        for asset in regscale_models.Asset.get_all_by_parent(plan_id, regscale_models.SecurityPlan.get_module_string()):
            for issue in regscale_models.Issue.get_all_by_parent(asset.id, asset.get_module_string()):
                issue.delete()
            asset.delete()
        for issue in regscale_models.Issue.get_all_by_parent(plan_id, regscale_models.SecurityPlan.get_module_string()):
            issue.delete()

    def assert_vulnerability_counts(self, assets, expected_counts):
        for asset in assets:
            vulnerability_ids = self.get_vulnerability_ids(asset)
            expected_count = expected_counts.get(asset.wizId, 0)
            if expected_count != len(vulnerability_ids):
                logger.error(f"Vulnerabilities for asset {asset.wizId}: {vulnerability_ids}")
            self.assertEqual(
                expected_count,
                len(vulnerability_ids),
                f"Expected {expected_count} vulnerability ids for asset {asset.wizId}, got {vulnerability_ids}",
            )

    def get_vulnerability_ids(self, asset):
        if self.regscale_version >= "5.64.0" or self.regscale_version == "localdev":
            return {
                vuln_mapping.vulnerabilityId
                for vuln_mapping in regscale_models.VulnerabilityMapping.find_by_asset(asset.id, status="Open")
            }
        return set()

    def assert_open_issues_with_assets(self, assets, expected_count):
        open_issues_with_assets = self.get_open_issues_with_assets(assets)
        if expected_count != len(open_issues_with_assets):
            logger.error(f"Open Issues: {open_issues_with_assets}")
        self.assertEqual(
            expected_count,
            len(open_issues_with_assets),
            f"Expected {expected_count} open issues tied to assets, but found {len(open_issues_with_assets)}",
        )
        self.verify_issue_asset_association(open_issues_with_assets, assets)

    def get_open_issues_with_assets(self, assets):
        open_issues = []
        for asset in assets:
            asset_issues = regscale_models.Issue.get_all_by_parent(
                parent_id=asset.id, parent_module=asset.get_module_string()
            )
            open_issues.extend([issue for issue in asset_issues if issue.status == regscale_models.IssueStatus.Open])
        return open_issues

    def verify_issue_asset_association(self, issues, assets):
        asset_names = [asset.wizId for asset in assets]
        for issue in issues:
            self.assertIsNotNone(issue.assetIdentifier, f"Issue {issue.id} is not associated with an asset")
            self.assertIn(
                issue.assetIdentifier.split("\n")[0],
                asset_names,
                f"Issue {issue.id} is associated with an asset not in the current set",
            )

    @patch("regscale.integrations.commercial.wizv2.scanner.WizVulnerabilityIntegration.fetch_wiz_data_if_needed")
    @patch("regscale.integrations.commercial.wizv2.scanner.WizVulnerabilityIntegration.authenticate")
    def test_wiz_vulnerability_integration_consolidated(self, mock_authenticate, mock_fetch_wiz_data):
        mock_authenticate.return_value = None
        self.clean_plan(self.plan_id)
        integration = WizVulnerabilityIntegration(plan_id=self.plan_id)

        mock_fetch_wiz_data.return_value = asset_nodes
        assets = list(integration.fetch_assets(wiz_project_id=self.project_id))
        self.assertEqual(2, len(assets))
        integration.sync_assets(plan_id=self.plan_id, wiz_project_id=self.project_id)

        mock_fetch_wiz_data.return_value = vuln_nodes
        findings = integration.fetch_findings(wiz_project_id=self.project_id)
        self.assertEqual(12, len(list(findings)))
        integration.sync_findings(plan_id=self.plan_id, wiz_project_id=self.project_id)

        assets = regscale_models.Asset.get_all_by_parent(self.plan_id, regscale_models.SecurityPlan.get_module_string())
        self.assertEqual(2, len(assets))

        expected_counts = {
            "52c50c20-3d07-58ac-ab2e-c412bf35351b": 2,
            "52c50c20-3d07-58ac-ab2e-c412bf35351c": 1,
        }
        self.assert_vulnerability_counts(assets, expected_counts)

        if self.regscale_version >= "5.64.0" or self.regscale_version == "localdev":
            self.assert_open_issues_with_assets(assets, 2)

        mock_fetch_wiz_data.return_value = vuln_nodes[:1]
        integration = WizVulnerabilityIntegration(plan_id=self.plan_id)
        integration.sync_findings(plan_id=self.plan_id, wiz_project_id=self.project_id)

        expected_counts = {
            "52c50c20-3d07-58ac-ab2e-c412bf35351b": 1,
            "52c50c20-3d07-58ac-ab2e-c412bf35351c": 0,
        }
        self.assert_vulnerability_counts(assets, expected_counts)

    @patch("regscale.integrations.commercial.wizv2.scanner.WizVulnerabilityIntegration.fetch_wiz_data_if_needed")
    @patch("regscale.integrations.commercial.wizv2.scanner.WizVulnerabilityIntegration.authenticate")
    def test_wiz_vulnerability_integration_per_asset(self, mock_authenticate, mock_fetch_wiz_data):
        ScannerVariables.issueCreation = "PerAsset"
        mock_authenticate.return_value = None
        self.clean_plan(self.plan_id)
        integration = WizVulnerabilityIntegration(plan_id=self.plan_id)

        mock_fetch_wiz_data.return_value = asset_nodes
        assets = list(integration.fetch_assets(wiz_project_id=self.project_id))
        self.assertEqual(2, len(assets))
        integration.sync_assets(plan_id=self.plan_id, wiz_project_id=self.project_id)

        mock_fetch_wiz_data.return_value = vuln_nodes
        findings = integration.fetch_findings(wiz_project_id=self.project_id)
        self.assertEqual(12, len(list(findings)))
        integration.sync_findings(plan_id=self.plan_id, wiz_project_id=self.project_id)

        assets = regscale_models.Asset.get_all_by_parent(self.plan_id, regscale_models.SecurityPlan.get_module_string())
        self.assertEqual(2, len(assets))

        expected_counts = {
            "52c50c20-3d07-58ac-ab2e-c412bf35351b": 2,
            "52c50c20-3d07-58ac-ab2e-c412bf35351c": 1,
        }
        self.assert_vulnerability_counts(assets, expected_counts)

        self.assert_open_issues_with_assets(assets, 3)

        mock_fetch_wiz_data.return_value = vuln_nodes[:1]
        integration = WizVulnerabilityIntegration(plan_id=self.plan_id)
        integration.sync_findings(plan_id=self.plan_id, wiz_project_id=self.project_id)

        expected_counts = {
            "52c50c20-3d07-58ac-ab2e-c412bf35351b": 1,
            "52c50c20-3d07-58ac-ab2e-c412bf35351c": 0,
        }
        self.assert_vulnerability_counts(assets, expected_counts)

    @patch("regscale.integrations.commercial.wizv2.scanner.WizVulnerabilityIntegration.fetch_wiz_data_if_needed")
    @patch("regscale.integrations.commercial.wizv2.scanner.WizVulnerabilityIntegration.authenticate")
    def test_wiz_assets_with_hardware_asset_types_enabled(self, mock_authenticate, mock_fetch_wiz_data):
        WizVariables.useWizHardwareAssetTypes = True
        WizVariables.wizHardwareAssetTypes = ["CLIENT_APPLICATION"]
        mock_authenticate.return_value = None
        integration = WizVulnerabilityIntegration(plan_id=self.plan_id)

        mock_fetch_wiz_data.return_value = asset_nodes
        assets = list(integration.fetch_assets(wiz_project_id=self.project_id))
        self.assertEqual(2, len(assets))
        integration.sync_assets(plan_id=self.plan_id, wiz_project_id=self.project_id)

        mock_fetch_wiz_data.return_value = vuln_nodes
        findings = integration.fetch_findings(wiz_project_id=self.project_id)
        self.assertEqual(12, len(list(findings)))
        integration.sync_findings(plan_id=self.plan_id, wiz_project_id=self.project_id)

        assets = regscale_models.Asset.get_all_by_parent(self.plan_id, regscale_models.SecurityPlan.get_module_string())
        self.assertEqual(2, len(assets))
        for asset in assets:
            self.assertEqual(asset.assetCategory, regscale_models.AssetCategory.Hardware)

    @patch("regscale.integrations.commercial.wizv2.scanner.WizVulnerabilityIntegration.fetch_wiz_data_if_needed")
    @patch("regscale.integrations.commercial.wizv2.scanner.WizVulnerabilityIntegration.authenticate")
    def test_wiz_assets_with_hardware_asset_types_disabled(self, mock_authenticate, mock_fetch_wiz_data):
        WizVariables.useWizHardwareAssetTypes = False
        WizVariables.wizHardwareAssetTypes = ["CLIENT_APPLICATION"]
        mock_authenticate.return_value = None
        integration = WizVulnerabilityIntegration(plan_id=self.plan_id)

        mock_fetch_wiz_data.return_value = asset_nodes
        assets = list(integration.fetch_assets(wiz_project_id=self.project_id))
        self.assertEqual(2, len(assets))
        integration.sync_assets(plan_id=self.plan_id, wiz_project_id=self.project_id)

        mock_fetch_wiz_data.return_value = vuln_nodes
        findings = integration.fetch_findings(wiz_project_id=self.project_id)
        self.assertEqual(12, len(list(findings)))
        integration.sync_findings(plan_id=self.plan_id, wiz_project_id=self.project_id)

        assets = regscale_models.Asset.get_all_by_parent(self.plan_id, regscale_models.SecurityPlan.get_module_string())
        self.assertEqual(2, len(assets))
        for asset in assets:
            self.assertEqual(asset.assetCategory, regscale_models.AssetCategory.Software)

    @patch("regscale.integrations.commercial.wizv2.scanner.WizVulnerabilityIntegration.fetch_wiz_data_if_needed")
    @patch("regscale.integrations.commercial.wizv2.scanner.WizVulnerabilityIntegration.authenticate")
    def test_wiz_due_date_calculation(self, mock_authenticate, mock_fetch_wiz_data):
        from datetime import datetime, timedelta
        from regscale.core.utils.date import date_obj

        mock_authenticate.return_value = None
        integration = WizVulnerabilityIntegration(plan_id=self.plan_id)

        mock_fetch_wiz_data.return_value = vuln_nodes
        mock_app = MagicMock()
        mock_app.config = {"issues": {"wiz": {"critical": 1, "high": 2, "moderate": 3, "low": 4}}}
        with patch.object(integration, "app", mock_app):
            findings = integration.fetch_findings(wiz_project_id=self.project_id)
            findings = list(findings)
            self.assertEqual(12, len(findings))
            for finding in findings:
                # convert the due_date to a datetime object for comparison
                finding_due_date = datetime.strptime(finding.due_date, "%Y-%m-%dT%H:%M:%S")
                first_seen_date = date_obj(finding.first_seen)
                if finding.severity == regscale_models.IssueSeverity.Critical.value:
                    self.assertEqual(
                        finding_due_date.date(),
                        (first_seen_date + timedelta(days=mock_app.config["issues"]["wiz"]["critical"])),
                    )
                elif finding.severity == regscale_models.IssueSeverity.High.value:
                    self.assertEqual(
                        finding_due_date.date(),
                        (first_seen_date + timedelta(days=mock_app.config["issues"]["wiz"]["high"])),
                    )
                elif finding.severity == regscale_models.IssueSeverity.Moderate.value:
                    self.assertEqual(
                        finding_due_date.date(),
                        (first_seen_date + timedelta(days=mock_app.config["issues"]["wiz"]["moderate"])),
                    )
                elif finding.severity == regscale_models.IssueSeverity.Low.value:
                    self.assertEqual(
                        finding_due_date.date(),
                        (first_seen_date + timedelta(days=mock_app.config["issues"]["wiz"]["low"])),
                    )
                else:
                    self.assertEqual(finding_due_date.date(), (first_seen_date + timedelta(days=60)))


if __name__ == "__main__":
    unittest.main()
