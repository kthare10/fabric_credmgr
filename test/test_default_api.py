# coding: utf-8

"""
    Fabric Credential Manager API

    This is Fabric Credential Manager API  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: kthare10@renci.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import fabric_credmgr
from fabric_credmgr.api.default_api import DefaultApi  # noqa: E501
from fabric_credmgr.rest import ApiException


class TestDefaultApi(unittest.TestCase):
    """DefaultApi unit test stubs"""

    def setUp(self):
        self.api = fabric_credmgr.api.default_api.DefaultApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_post(self):
        """Test case for create_post

        Generate OAuth tokens for an user  # noqa: E501
        """
        pass

    def test_create_with_id_token_post(self):
        """Test case for create_with_id_token_post

        Generate OAuth tokens for an user provided CILogon ID Token  # noqa: E501
        """
        pass

    def test_get_get(self):
        """Test case for get_get

        get tokens for an user  # noqa: E501
        """
        pass

    def test_refresh_post(self):
        """Test case for refresh_post

        Refresh OAuth tokens for an user  # noqa: E501
        """
        pass

    def test_revoke_post(self):
        """Test case for revoke_post

        Revoke a refresh token for an user  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
