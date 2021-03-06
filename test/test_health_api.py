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
from swagger_client.api.health_api import HealthApi  # noqa: E501
from swagger_client.rest import ApiException


class TestHealthApi(unittest.TestCase):
    """HealthApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.health_api.HealthApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_health(self):
        """Test case for get_health

        Check the status of Harbor components  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
