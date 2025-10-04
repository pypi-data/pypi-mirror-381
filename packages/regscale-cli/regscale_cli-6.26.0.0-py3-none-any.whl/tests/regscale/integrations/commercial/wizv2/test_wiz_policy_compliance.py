#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Unit tests for Wiz Policy Compliance Integration.
"""

import json
import os
from unittest.mock import Mock, patch, mock_open

import pytest

from regscale.integrations.commercial.wizv2.policy_compliance import (
    WizComplianceItem,
    WizPolicyComplianceIntegration,
)


class TestWizComplianceItem:
    """Test the WizComplianceItem class."""

    def setup_method(self):
        """Set up test data."""
        self.mock_raw_data = {
            "id": "assessment-123",
            "result": "FAIL",
            "policy": {
                "id": "policy-456",
                "name": "Test Policy",
                "description": "Test policy description",
                "severity": "HIGH",
                "remediationInstructions": "Fix the issue",
                "securitySubCategories": [
                    {
                        "externalId": "AC-3",
                        "category": {"framework": {"id": "wf-id-4", "name": "NIST SP 800-53 Revision 5"}},
                    }
                ],
            },
            "resource": {
                "id": "resource-789",
                "name": "Test Resource",
                "type": "VIRTUAL_MACHINE",
                "region": "us-east-1",
                "subscription": {"cloudProvider": "Azure", "name": "Test Subscription", "externalId": "sub-123"},
                "tags": [{"key": "Environment", "value": "Production"}, {"key": "Owner", "value": "TestTeam"}],
            },
            "output": {"someField": "someValue"},
        }

        self.mock_integration = Mock()
        self.mock_integration.framework_id = "wf-id-4"  # Add framework_id for filtering
        self.mock_integration.get_framework_name.return_value = "NIST SP 800-53 Revision 5"

    def test_wiz_compliance_item_creation(self):
        """Test creating a WizComplianceItem from raw data."""
        item = WizComplianceItem(self.mock_raw_data, self.mock_integration)

        assert item.id == "assessment-123"
        assert item.result == "FAIL"
        assert item.resource_id == "resource-789"
        assert item.resource_name == "Test Resource"
        assert item.control_id == "AC-3"
        assert item.compliance_result == "FAIL"
        assert item.severity == "HIGH"
        assert item.framework_id == "wf-id-4"
        assert item.framework == "NIST SP 800-53 Revision 5"
        assert item.is_fail
        assert not item.is_pass

    def test_wiz_compliance_item_pass_result(self):
        """Test WizComplianceItem with PASS result."""
        self.mock_raw_data["result"] = "PASS"
        item = WizComplianceItem(self.mock_raw_data, self.mock_integration)

        assert item.compliance_result == "PASS"
        assert item.is_pass
        assert not item.is_fail

    def test_wiz_compliance_item_missing_control_id(self):
        """Test WizComplianceItem with missing control ID."""
        # Remove security subcategories
        self.mock_raw_data["policy"]["securitySubCategories"] = []
        item = WizComplianceItem(self.mock_raw_data, self.mock_integration)

        assert item.control_id == ""
        assert item.framework == ""
        assert item.framework_id is None

    def test_wiz_compliance_item_missing_policy(self):
        """Test WizComplianceItem with missing policy data."""
        self.mock_raw_data["policy"] = {}
        item = WizComplianceItem(self.mock_raw_data, self.mock_integration)

        assert item.control_id == ""
        assert item.severity is None
        assert "unknown policy" in item.description.lower()
        assert item.framework == ""

    def test_wiz_compliance_item_description_fallback(self):
        """Test description fallback when policy description is missing."""
        # Remove description but keep name
        del self.mock_raw_data["policy"]["description"]
        item = WizComplianceItem(self.mock_raw_data, self.mock_integration)

        assert "Test Policy" in item.description

        # Test with ruleDescription
        self.mock_raw_data["policy"]["ruleDescription"] = "Rule description"
        item = WizComplianceItem(self.mock_raw_data, self.mock_integration)
        assert item.description == "Rule description"

    def test_wiz_compliance_item_framework_caching(self):
        """Test that framework mapping uses integration cache."""
        item = WizComplianceItem(self.mock_raw_data, self.mock_integration)

        # Access framework property
        framework = item.framework

        # Verify integration's get_framework_name was called
        self.mock_integration.get_framework_name.assert_called_with("wf-id-4")
        assert framework == "NIST SP 800-53 Revision 5"

    def test_wiz_compliance_item_no_integration(self):
        """Test WizComplianceItem without integration instance."""
        item = WizComplianceItem(self.mock_raw_data, None)

        # Should fallback to framework name from raw data
        assert item.framework == "NIST SP 800-53 Revision 5"


class TestWizPolicyComplianceIntegration:
    """Test the WizPolicyComplianceIntegration class."""

    def setup_method(self):
        """Set up test fixtures."""
        self.integration = WizPolicyComplianceIntegration(
            plan_id=123,
            wiz_project_id="test-project-123",
            client_id="test-client-id",
            client_secret="test-client-secret",
            framework_id="wf-id-4",
            catalog_id=456,
        )

        # Mock authentication
        self.integration.access_token = "mock-token"
        self.integration.wiz_endpoint = "https://api.wiz.io/graphql"

    def test_initialization(self):
        """Test integration initialization."""
        assert self.integration.plan_id == 123
        assert self.integration.wiz_project_id == "test-project-123"
        assert self.integration.client_id == "test-client-id"
        assert self.integration.client_secret == "test-client-secret"
        assert self.integration.framework_id == "wf-id-4"
        assert self.integration.catalog_id == 456
        assert self.integration.title == "Wiz Policy Compliance Integration"
        assert self.integration.framework == "NIST800-53R5"

    def test_framework_id_mapping(self):
        """Test framework ID to name mapping."""
        assert self.integration._map_framework_id_to_name("wf-id-4") == "NIST800-53R5"
        assert self.integration._map_framework_id_to_name("wf-id-48") == "NIST800-53R4"
        assert self.integration._map_framework_id_to_name("wf-id-5") == "FedRAMP"
        assert self.integration._map_framework_id_to_name("unknown-id") == "unknown-id"

    def test_resource_type_mapping(self):
        """Test resource type to asset type mapping."""
        # Create mock compliance items with different resource types
        test_cases = [
            ("VIRTUAL_MACHINE", "Virtual Machine"),
            ("CONTAINER", "Container"),
            ("DATABASE", "Database"),
            ("BUCKET", "Storage"),
            ("UNKNOWN_TYPE", "Cloud Resource"),
        ]

        for resource_type, expected_asset_type in test_cases:
            mock_data = {
                "id": "test-id",
                "result": "PASS",
                "policy": {},
                "resource": {"type": resource_type},
                "output": {},
            }

            compliance_item = WizComplianceItem(mock_data)
            asset_type = self.integration._map_resource_type_to_asset_type(compliance_item)
            assert asset_type == expected_asset_type

    @patch("regscale.integrations.commercial.wizv2.policy_compliance.wiz_authenticate")
    @patch("regscale.integrations.commercial.wizv2.policy_compliance.check_license")
    def test_authenticate_wiz(self, mock_check_license, mock_wiz_authenticate):
        """Test Wiz authentication."""
        # Set up mocks
        mock_app = Mock()
        mock_app.config = {"wizUrl": "https://api.wiz.io/graphql"}
        mock_check_license.return_value = mock_app
        mock_wiz_authenticate.return_value = "test-token"

        # Clear existing token
        self.integration.access_token = ""

        token = self.integration.authenticate_wiz()

        assert token == "test-token"
        assert self.integration.access_token == "test-token"
        assert self.integration.wiz_endpoint == "https://api.wiz.io/graphql"

        mock_wiz_authenticate.assert_called_once_with(client_id="test-client-id", client_secret="test-client-secret")

    @patch("regscale.integrations.commercial.wizv2.policy_compliance.run_async_queries")
    def test_fetch_policy_assessments_from_wiz(self, mock_run_async_queries):
        """Test fetching policy assessments from Wiz API."""
        # Mock API response
        mock_nodes = [
            {"id": "assessment-1", "result": "PASS"},
            {"id": "assessment-2", "result": "FAIL"},
        ]
        mock_run_async_queries.return_value = [("configuration", mock_nodes, None)]  # (query_type, nodes, error)

        results = self.integration._fetch_policy_assessments_from_wiz()

        assert len(results) == 2
        assert results[0]["id"] == "assessment-1"
        assert results[1]["result"] == "FAIL"

        # Verify the query was called with correct parameters
        mock_run_async_queries.assert_called_once()
        call_args = mock_run_async_queries.call_args
        assert call_args[1]["max_concurrent"] == 1

    @patch("regscale.integrations.commercial.wizv2.policy_compliance.run_async_queries")
    def test_fetch_policy_assessments_with_error(self, mock_run_async_queries):
        """Test handling API errors when fetching assessments."""
        # Mock API error response
        mock_run_async_queries.return_value = [("configuration", [], "API Error message")]

        with pytest.raises(SystemExit):  # error_and_exit raises SystemExit
            self.integration._fetch_policy_assessments_from_wiz()

    def test_create_compliance_item(self):
        """Test creating compliance item from raw data."""
        raw_data = {
            "id": "test-id",
            "result": "FAIL",
            "policy": {"name": "Test Policy"},
            "resource": {"id": "res-123", "name": "Test Resource"},
            "output": {},
        }

        item = self.integration.create_compliance_item(raw_data)

        assert isinstance(item, WizComplianceItem)
        assert item.id == "test-id"
        assert item.result == "FAIL"

    @patch.object(WizPolicyComplianceIntegration, "_load_regscale_assets")
    @patch.object(WizPolicyComplianceIntegration, "_asset_exists_in_regscale")
    def test_fetch_compliance_data(self, mock_asset_exists, mock_load_assets):
        """Test fetching raw compliance data with filtering."""
        # Mock that all assets exist
        mock_asset_exists.return_value = True

        # Set up the asset cache that's used in the filtering logic
        self.integration._regscale_assets_by_wiz_id = {
            "res-1": Mock(name="Resource 1", wizId="res-1"),
            "res-2": Mock(name="Resource 2", wizId="res-2"),
        }

        # Mock _load_regscale_assets to not override our cache
        mock_load_assets.return_value = None

        # Mock the raw data fetch with proper framework data
        mock_raw_data = [
            {
                "id": "assessment-1",
                "result": "PASS",
                "policy": {
                    "name": "Policy 1",
                    "securitySubCategories": [
                        {
                            "externalId": "AC-2",
                            "category": {"framework": {"id": "wf-id-4", "name": "NIST SP 800-53 Revision 5"}},
                        }
                    ],
                },
                "resource": {"id": "res-1", "name": "Resource 1"},
                "output": {},
            },
            {
                "id": "assessment-2",
                "result": "FAIL",
                "policy": {
                    "name": "Policy 2",
                    "securitySubCategories": [
                        {
                            "externalId": "AC-3",
                            "category": {"framework": {"id": "wf-id-4", "name": "NIST SP 800-53 Revision 5"}},
                        }
                    ],
                },
                "resource": {"id": "res-2", "name": "Resource 2"},
                "output": {},
            },
        ]

        with patch.object(self.integration, "_fetch_policy_assessments_from_wiz", return_value=mock_raw_data):
            raw_data = self.integration.fetch_compliance_data()

        assert len(raw_data) == 2  # Both items should pass filtering
        assert all(isinstance(item, dict) for item in raw_data)
        assert raw_data[0]["result"] == "PASS"
        assert raw_data[1]["result"] == "FAIL"

    @patch("builtins.open", new_callable=mock_open)
    @patch("os.makedirs")
    @patch("regscale.integrations.commercial.wizv2.policy_compliance.datetime")
    def test_write_policy_data_to_json(self, mock_datetime, mock_makedirs, mock_file):
        """Test writing policy data to JSON file."""
        # Set up mock datetime
        mock_datetime.now.return_value.strftime.return_value = "20230806_120000"

        # Set up mock compliance data
        self.integration.all_compliance_items = [
            WizComplianceItem(
                {
                    "id": "test-1",
                    "result": "PASS",
                    "policy": {"name": "Test Policy"},
                    "resource": {"id": "res-1", "name": "Resource 1"},
                    "output": {},
                }
            )
        ]
        self.integration.failed_compliance_items = []
        self.integration.framework_mapping = {"wf-id-4": "NIST SP 800-53 Revision 5"}

        file_path = self.integration.write_policy_data_to_json()

        # Verify file path
        expected_path = os.path.join("artifacts", "wiz", "policy_compliance_report_20230806_120000.json")
        assert file_path == expected_path

        # Verify directory creation
        mock_makedirs.assert_called_once_with(os.path.join("artifacts", "wiz"), exist_ok=True)

        # Verify file write
        mock_file.assert_called_once_with(expected_path, "w", encoding="utf-8")

        # Verify JSON content was written
        handle = mock_file()
        assert handle.write.called

    @patch("os.path.exists")
    @patch("builtins.open", new_callable=mock_open)
    def test_load_framework_mapping_from_cache(self, mock_file, mock_exists):
        """Test loading framework mapping from cache file."""
        mock_exists.return_value = True

        cache_data = {
            "framework_mapping": {"wf-id-4": "NIST SP 800-53 Revision 5", "wf-id-5": "FedRAMP"},
            "timestamp": "2023-08-06T12:00:00",
        }

        mock_file.return_value.read.return_value = json.dumps(cache_data)

        mapping = self.integration.load_or_create_framework_mapping()

        assert mapping == cache_data["framework_mapping"]
        assert self.integration.framework_mapping == mapping
        mock_file.assert_called_once()

    @patch("os.path.exists")
    @patch("regscale.integrations.commercial.wizv2.policy_compliance.run_async_queries")
    @patch("builtins.open", new_callable=mock_open)
    @patch("os.makedirs")
    def test_fetch_and_cache_framework_mapping(self, mock_makedirs, mock_file, mock_run_async_queries, mock_exists):
        """Test fetching and caching framework mapping."""
        mock_exists.return_value = False  # No cache file

        # Mock framework data from API
        mock_frameworks = [
            {"id": "wf-id-4", "name": "NIST SP 800-53 Revision 5"},
            {"id": "wf-id-5", "name": "FedRAMP"},
        ]
        mock_run_async_queries.return_value = [("configuration", mock_frameworks, None)]

        mapping = self.integration.load_or_create_framework_mapping()

        expected_mapping = {"wf-id-4": "NIST SP 800-53 Revision 5", "wf-id-5": "FedRAMP"}

        assert mapping == expected_mapping
        assert self.integration.framework_mapping == mapping

        # Verify cache file was written
        mock_file.assert_called()
        mock_makedirs.assert_called()

    def test_get_framework_name(self):
        """Test getting framework name by ID."""
        self.integration.framework_mapping = {"wf-id-4": "NIST SP 800-53 Revision 5", "wf-id-5": "FedRAMP"}

        assert self.integration.get_framework_name("wf-id-4") == "NIST SP 800-53 Revision 5"
        assert self.integration.get_framework_name("wf-id-5") == "FedRAMP"
        assert self.integration.get_framework_name("unknown-id") == "unknown-id"

    def test_create_finding_from_compliance_item_wiz_specific(self):
        """Test creating a finding from Wiz compliance item with enhanced metadata."""
        mock_data = {
            "id": "assessment-123",
            "result": "FAIL",
            "policy": {
                "name": "Test Policy",
                "description": "Test policy description",
                "severity": "HIGH",
                "remediationInstructions": "Fix the issue",
            },
            "resource": {
                "id": "resource-789",
                "name": "Test Resource",
                "type": "VIRTUAL_MACHINE",
                "region": "us-east-1",
                "subscription": {"cloudProvider": "Azure", "name": "Test Subscription"},
            },
            "output": {},
        }

        compliance_item = WizComplianceItem(mock_data, self.integration)
        finding = self.integration.create_finding_from_compliance_item(compliance_item)

        assert finding is not None
        assert finding.title == "Policy Compliance Failure: Test Policy"
        assert finding.external_id == "wiz-policy-assessment-123"
        assert finding.asset_identifier == "resource-789"  # Should use Wiz resource ID for wizId lookup
        assert "Fix the issue" in finding.description
        assert "Azure" in finding.description

    def test_create_asset_from_compliance_item_wiz_specific(self):
        """Test creating an asset from Wiz compliance item with enhanced metadata."""
        mock_data = {
            "id": "assessment-123",
            "result": "FAIL",
            "policy": {"name": "Test Policy"},
            "resource": {
                "id": "resource-789",
                "name": "Test Resource",
                "type": "VIRTUAL_MACHINE",
                "region": "us-east-1",
                "subscription": {"cloudProvider": "Azure", "name": "Test Subscription", "externalId": "sub-123"},
                "tags": [{"key": "Environment", "value": "Production"}, {"key": "Owner", "value": "TestTeam"}],
            },
            "output": {},
        }

        compliance_item = WizComplianceItem(mock_data, self.integration)

        # Mock compliance mapping for notes
        self.integration.asset_compliance_map = {"resource-789": [compliance_item]}
        self.integration.FAIL_STATUSES = ["FAIL"]

        with patch.object(self.integration, "_find_existing_asset_by_resource_id", return_value=None):
            asset = self.integration.create_asset_from_compliance_item(compliance_item)

        assert asset is not None
        assert asset.name == "Test Resource"
        assert asset.identifier == "Test Resource (resource-789)"
        assert asset.asset_type == "Virtual Machine"
        assert "Environment:Production" in asset.description
        assert "Owner:TestTeam" in asset.description
        assert "Azure" in asset.notes
        assert "Test Subscription" in asset.notes

    def test_create_asset_notes(self):
        """Test creating detailed asset notes."""
        mock_data = {
            "id": "assessment-123",
            "result": "FAIL",
            "policy": {"name": "Test Policy"},
            "resource": {
                "id": "resource-789",
                "name": "Test Resource",
                "type": "VIRTUAL_MACHINE",
                "subscription": {"cloudProvider": "Azure", "name": "Test Subscription", "externalId": "sub-123"},
            },
            "output": {},
        }

        compliance_item = WizComplianceItem(mock_data, self.integration)

        # Set up asset compliance map
        self.integration.asset_compliance_map = {"resource-789": [compliance_item, compliance_item]}  # 2 assessments
        self.integration.FAIL_STATUSES = ["FAIL"]

        notes = self.integration._create_asset_notes(compliance_item)

        assert "Wiz Asset Details" in notes
        assert "resource-789" in notes
        assert "VIRTUAL_MACHINE" in notes
        assert "Azure" in notes
        assert "Test Subscription" in notes
        assert "sub-123" in notes
        assert "**Total Assessments:** 2" in notes
        assert "**Failed Assessments:** 2" in notes
        assert "**Compliance Rate:** 0.0%" in notes

    def test_fetch_assets_no_assets_created(self):
        """Test that fetch_assets does not create any assets - they come from inventory import."""
        # Create compliance items
        failed_data = {
            "id": "assessment-fail",
            "result": "FAIL",
            "policy": {
                "name": "Fail Policy",
                "securitySubCategories": [
                    {
                        "externalId": "AC-2",
                        "category": {"framework": {"id": "wf-id-4", "name": "NIST SP 800-53 Revision 5"}},
                    }
                ],
            },
            "resource": {"id": "resource-fail", "name": "Failed Resource", "type": "VIRTUAL_MACHINE"},
            "output": {},
        }

        failed_item = WizComplianceItem(failed_data, self.integration)
        self.integration.failed_compliance_items = [failed_item]

        # Call fetch_assets - should return empty iterator
        assets = list(self.integration.fetch_assets())

        # Should not create any assets
        assert len(assets) == 0

    @patch.object(WizPolicyComplianceIntegration, "_asset_exists_in_regscale")
    def test_framework_filtering_in_findings(self, mock_asset_exists):
        """Test that fetch_findings filters by framework and uses asset names."""
        # Mock that the framework match resource exists in RegScale (using resource ID)
        mock_asset_exists.side_effect = lambda resource_id: resource_id == "resource-framework-match"

        # Create compliance items in different frameworks
        framework_data = {
            "id": "assessment-framework-match",
            "result": "FAIL",
            "policy": {
                "name": "Framework Match Policy",
                "securitySubCategories": [
                    {
                        "externalId": "AC-2",
                        "category": {"framework": {"id": "wf-id-4", "name": "NIST SP 800-53 Revision 5"}},
                    }
                ],
            },
            "resource": {
                "id": "resource-framework-match",
                "name": "Framework Match Resource",
                "type": "VIRTUAL_MACHINE",
            },
            "output": {},
        }

        other_framework_data = {
            "id": "assessment-other-framework",
            "result": "FAIL",
            "policy": {
                "name": "Other Framework Policy",
                "securitySubCategories": [
                    {
                        "externalId": "AC-3",
                        "category": {"framework": {"id": "wf-id-5", "name": "Other Framework"}},
                    }
                ],
            },
            "resource": {
                "id": "resource-other-framework",
                "name": "Other Framework Resource",
                "type": "VIRTUAL_MACHINE",
            },
            "output": {},
        }

        framework_item = WizComplianceItem(framework_data, self.integration)
        other_framework_item = WizComplianceItem(other_framework_data, self.integration)

        # Mock integration data - both items are "failed" but only one belongs to the target framework
        self.integration.all_compliance_items = [framework_item, other_framework_item]
        self.integration.failed_compliance_items = [framework_item, other_framework_item]
        self.integration.FAIL_STATUSES = ["FAIL"]

        # Test that only framework-specific items have valid control IDs
        assert framework_item.control_id == "AC-2"  # Should match framework
        assert other_framework_item.control_id == ""  # Should be empty due to framework filtering

        # Test fetch_assets - should return empty
        assets = list(self.integration.fetch_assets())
        assert len(assets) == 0  # No assets created

        # Test fetch_findings
        findings = list(self.integration.fetch_findings())
        # Should only create finding for framework-matching item that has existing asset
        assert len(findings) == 1
        finding = findings[0]
        assert finding.asset_identifier == "resource-framework-match"  # Should use Wiz resource ID

    @patch.object(WizPolicyComplianceIntegration, "authenticate_wiz")
    @patch.object(WizPolicyComplianceIntegration, "load_or_create_framework_mapping")
    @patch.object(WizPolicyComplianceIntegration, "write_policy_data_to_json")
    @patch.object(WizPolicyComplianceIntegration, "sync_compliance")
    def test_sync_policy_compliance(self, mock_sync_compliance, mock_write_json, mock_load_mapping, mock_auth):
        """Test the main sync policy compliance method."""
        mock_write_json.return_value = "/path/to/output.json"

        self.integration.sync_policy_compliance()

        # Verify all steps were called in correct order
        mock_auth.assert_called_once()
        mock_load_mapping.assert_called_once()
        # Note: process_compliance_data is called internally by sync_compliance, not directly
        mock_sync_compliance.assert_called_once()
        mock_write_json.assert_called_once()

    def test_sync_wiz_compliance_backward_compatibility(self):
        """Test backward compatibility method."""
        with patch.object(self.integration, "sync_policy_compliance") as mock_sync:
            self.integration.sync_wiz_compliance()
            mock_sync.assert_called_once()

    @patch.object(WizPolicyComplianceIntegration, "_asset_exists_in_regscale")
    @patch.object(WizPolicyComplianceIntegration, "_get_control_implementations")
    @patch.object(WizPolicyComplianceIntegration, "_load_existing_records_cache")
    @patch.object(WizPolicyComplianceIntegration, "_process_single_control_assessment")
    def test_control_assessments_only_for_existing_assets(
        self, mock_process_single, mock_load_cache, mock_get_implementations, mock_asset_exists
    ):
        """Test that control assessments are only created for controls with existing assets."""
        from regscale.integrations.compliance_integration import ControlImplementation
        from regscale.models.regscale_models import SecurityControl

        # Mock that only one asset exists (for AC-2 control)
        mock_asset_exists.side_effect = lambda resource_id: resource_id == "resource-with-asset"

        # Mock single control assessment creation to return 1 (one assessment created)
        mock_process_single.return_value = 1

        # Mock control implementations
        mock_impl1 = ControlImplementation(id=1, controlID=100, status="Not Satisfied", title="Test Implementation 1")
        mock_impl2 = ControlImplementation(id=2, controlID=200, status="Not Satisfied", title="Test Implementation 2")
        mock_get_implementations.return_value = [mock_impl1, mock_impl2]

        # Mock SecurityControl.get_object to return controls
        def mock_get_security_control(object_id):
            if object_id == 100:
                control = SecurityControl()
                control.id = 100
                control.controlId = "AC-2"
                return control
            elif object_id == 200:
                control = SecurityControl()
                control.id = 200
                control.controlId = "AC-3"
                return control
            return None

        # Create compliance items - one with existing asset, one without
        compliance_data = [
            {
                "id": "assessment-with-asset",
                "result": "FAIL",
                "policy": {
                    "name": "Policy with Asset",
                    "securitySubCategories": [
                        {
                            "externalId": "AC-2",
                            "category": {"framework": {"id": "wf-id-4", "name": "NIST SP 800-53 Revision 5"}},
                        }
                    ],
                },
                "resource": {"id": "resource-with-asset", "name": "Resource With Asset"},
                "output": {},
            },
            {
                "id": "assessment-no-asset",
                "result": "FAIL",
                "policy": {
                    "name": "Policy No Asset",
                    "securitySubCategories": [
                        {
                            "externalId": "AC-3",
                            "category": {"framework": {"id": "wf-id-4", "name": "NIST SP 800-53 Revision 5"}},
                        }
                    ],
                },
                "resource": {"id": "resource-no-asset", "name": "Resource No Asset"},
                "output": {},
            },
        ]

        # Process the compliance data
        with patch.object(SecurityControl, "get_object", side_effect=mock_get_security_control):
            with patch.object(self.integration, "_fetch_policy_assessments_from_wiz", return_value=compliance_data):
                self.integration.process_compliance_data()
                self.integration._process_control_assessments()

        # Verify only one control assessment was processed (AC-2 with existing asset)
        # AC-3 should be skipped because its asset doesn't exist
        mock_process_single.assert_called_once_with(
            control_id="ac-2",
            implementations=[mock_impl1, mock_impl2],
            processed_impl_today=set(),
        )


class TestWizComplianceItemEdgeCases:
    """Test edge cases for WizComplianceItem."""

    def test_empty_data(self):
        """Test WizComplianceItem with minimal data."""
        minimal_data = {"id": "", "result": "", "policy": {}, "resource": {}, "output": {}}

        item = WizComplianceItem(minimal_data)

        assert item.id == ""
        assert item.result == ""
        assert item.resource_id == ""
        assert item.resource_name == ""
        assert item.control_id == ""
        assert item.severity is None
        assert item.framework == ""
        assert not item.is_pass
        assert not item.is_fail

    def test_nested_missing_data(self):
        """Test WizComplianceItem with nested missing data."""
        data_with_missing_nested = {
            "id": "test",
            "result": "PASS",
            "policy": {"securitySubCategories": [{"category": {"framework": {}}}]},  # Missing id and name
            "resource": {"subscription": {}},  # Missing cloudProvider
            "output": {},
        }

        item = WizComplianceItem(data_with_missing_nested)

        assert item.framework_id is None
        assert item.framework == ""


if __name__ == "__main__":
    pytest.main([__file__])
