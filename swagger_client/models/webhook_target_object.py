# coding: utf-8

"""
    Harbor API

    These APIs provide services for manipulating Harbor project.  # noqa: E501

    OpenAPI spec version: 2.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.configuration import Configuration


class WebhookTargetObject(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'type': 'str',
        'address': 'str',
        'auth_header': 'str',
        'skip_cert_verify': 'bool'
    }

    attribute_map = {
        'type': 'type',
        'address': 'address',
        'auth_header': 'auth_header',
        'skip_cert_verify': 'skip_cert_verify'
    }

    def __init__(self, type=None, address=None, auth_header=None, skip_cert_verify=None, _configuration=None):  # noqa: E501
        """WebhookTargetObject - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._type = None
        self._address = None
        self._auth_header = None
        self._skip_cert_verify = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if address is not None:
            self.address = address
        if auth_header is not None:
            self.auth_header = auth_header
        if skip_cert_verify is not None:
            self.skip_cert_verify = skip_cert_verify

    @property
    def type(self):
        """Gets the type of this WebhookTargetObject.  # noqa: E501

        The webhook target notify type.  # noqa: E501

        :return: The type of this WebhookTargetObject.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this WebhookTargetObject.

        The webhook target notify type.  # noqa: E501

        :param type: The type of this WebhookTargetObject.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def address(self):
        """Gets the address of this WebhookTargetObject.  # noqa: E501

        The webhook target address.  # noqa: E501

        :return: The address of this WebhookTargetObject.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this WebhookTargetObject.

        The webhook target address.  # noqa: E501

        :param address: The address of this WebhookTargetObject.  # noqa: E501
        :type: str
        """

        self._address = address

    @property
    def auth_header(self):
        """Gets the auth_header of this WebhookTargetObject.  # noqa: E501

        The webhook auth header.  # noqa: E501

        :return: The auth_header of this WebhookTargetObject.  # noqa: E501
        :rtype: str
        """
        return self._auth_header

    @auth_header.setter
    def auth_header(self, auth_header):
        """Sets the auth_header of this WebhookTargetObject.

        The webhook auth header.  # noqa: E501

        :param auth_header: The auth_header of this WebhookTargetObject.  # noqa: E501
        :type: str
        """

        self._auth_header = auth_header

    @property
    def skip_cert_verify(self):
        """Gets the skip_cert_verify of this WebhookTargetObject.  # noqa: E501

        Whether or not to skip cert verify.  # noqa: E501

        :return: The skip_cert_verify of this WebhookTargetObject.  # noqa: E501
        :rtype: bool
        """
        return self._skip_cert_verify

    @skip_cert_verify.setter
    def skip_cert_verify(self, skip_cert_verify):
        """Sets the skip_cert_verify of this WebhookTargetObject.

        Whether or not to skip cert verify.  # noqa: E501

        :param skip_cert_verify: The skip_cert_verify of this WebhookTargetObject.  # noqa: E501
        :type: bool
        """

        self._skip_cert_verify = skip_cert_verify

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(WebhookTargetObject, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, WebhookTargetObject):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, WebhookTargetObject):
            return True

        return self.to_dict() != other.to_dict()
