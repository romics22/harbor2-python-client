# coding: utf-8

"""
    Harbor API

    These APIs provide services for manipulating Harbor project.  # noqa: E501

    OpenAPI spec version: 2.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.registry_api import RegistryApi  # noqa: E501
from swagger_client.rest import ApiException


class TestRegistryApi(unittest.TestCase):
    """RegistryApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.registry_api.RegistryApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_registry(self):
        """Test case for create_registry

        Create a registry  # noqa: E501
        """
        pass

    def test_delete_registry(self):
        """Test case for delete_registry

        Delete the specific registry  # noqa: E501
        """
        pass

    def test_get_registry(self):
        """Test case for get_registry

        Get the specific registry  # noqa: E501
        """
        pass

    def test_get_registry_info(self):
        """Test case for get_registry_info

        Get the registry info  # noqa: E501
        """
        pass

    def test_list_registries(self):
        """Test case for list_registries

        List the registries  # noqa: E501
        """
        pass

    def test_list_registry_provider_infos(self):
        """Test case for list_registry_provider_infos

        List all registered registry provider information  # noqa: E501
        """
        pass

    def test_list_registry_provider_types(self):
        """Test case for list_registry_provider_types

        List registry adapters  # noqa: E501
        """
        pass

    def test_ping_registry(self):
        """Test case for ping_registry

        Check status of a registry  # noqa: E501
        """
        pass

    def test_update_registry(self):
        """Test case for update_registry

        Update the registry  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()