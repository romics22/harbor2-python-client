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


class ScannerRegistrationReq(object):
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
        'name': 'str',
        'description': 'str',
        'url': 'str',
        'auth': 'str',
        'access_credential': 'str',
        'skip_cert_verify': 'bool',
        'use_internal_addr': 'bool',
        'disabled': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'url': 'url',
        'auth': 'auth',
        'access_credential': 'access_credential',
        'skip_cert_verify': 'skip_certVerify',
        'use_internal_addr': 'use_internal_addr',
        'disabled': 'disabled'
    }

    def __init__(self, name=None, description=None, url=None, auth=None, access_credential=None, skip_cert_verify=False, use_internal_addr=False, disabled=False, _configuration=None):  # noqa: E501
        """ScannerRegistrationReq - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._name = None
        self._description = None
        self._url = None
        self._auth = None
        self._access_credential = None
        self._skip_cert_verify = None
        self._use_internal_addr = None
        self._disabled = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        self.url = url
        if auth is not None:
            self.auth = auth
        if access_credential is not None:
            self.access_credential = access_credential
        if skip_cert_verify is not None:
            self.skip_cert_verify = skip_cert_verify
        if use_internal_addr is not None:
            self.use_internal_addr = use_internal_addr
        if disabled is not None:
            self.disabled = disabled

    @property
    def name(self):
        """Gets the name of this ScannerRegistrationReq.  # noqa: E501

        The name of this registration  # noqa: E501

        :return: The name of this ScannerRegistrationReq.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ScannerRegistrationReq.

        The name of this registration  # noqa: E501

        :param name: The name of this ScannerRegistrationReq.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this ScannerRegistrationReq.  # noqa: E501

        An optional description of this registration.  # noqa: E501

        :return: The description of this ScannerRegistrationReq.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ScannerRegistrationReq.

        An optional description of this registration.  # noqa: E501

        :param description: The description of this ScannerRegistrationReq.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def url(self):
        """Gets the url of this ScannerRegistrationReq.  # noqa: E501

        A base URL of the scanner adapter.  # noqa: E501

        :return: The url of this ScannerRegistrationReq.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this ScannerRegistrationReq.

        A base URL of the scanner adapter.  # noqa: E501

        :param url: The url of this ScannerRegistrationReq.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and url is None:
            raise ValueError("Invalid value for `url`, must not be `None`")  # noqa: E501

        self._url = url

    @property
    def auth(self):
        """Gets the auth of this ScannerRegistrationReq.  # noqa: E501

        Specify what authentication approach is adopted for the HTTP communications. Supported types Basic\", \"Bearer\" and api key header \"X-ScannerAdapter-API-Key\"   # noqa: E501

        :return: The auth of this ScannerRegistrationReq.  # noqa: E501
        :rtype: str
        """
        return self._auth

    @auth.setter
    def auth(self, auth):
        """Sets the auth of this ScannerRegistrationReq.

        Specify what authentication approach is adopted for the HTTP communications. Supported types Basic\", \"Bearer\" and api key header \"X-ScannerAdapter-API-Key\"   # noqa: E501

        :param auth: The auth of this ScannerRegistrationReq.  # noqa: E501
        :type: str
        """

        self._auth = auth

    @property
    def access_credential(self):
        """Gets the access_credential of this ScannerRegistrationReq.  # noqa: E501

        An optional value of the HTTP Authorization header sent with each request to the Scanner Adapter API.   # noqa: E501

        :return: The access_credential of this ScannerRegistrationReq.  # noqa: E501
        :rtype: str
        """
        return self._access_credential

    @access_credential.setter
    def access_credential(self, access_credential):
        """Sets the access_credential of this ScannerRegistrationReq.

        An optional value of the HTTP Authorization header sent with each request to the Scanner Adapter API.   # noqa: E501

        :param access_credential: The access_credential of this ScannerRegistrationReq.  # noqa: E501
        :type: str
        """

        self._access_credential = access_credential

    @property
    def skip_cert_verify(self):
        """Gets the skip_cert_verify of this ScannerRegistrationReq.  # noqa: E501

        Indicate if skip the certificate verification when sending HTTP requests  # noqa: E501

        :return: The skip_cert_verify of this ScannerRegistrationReq.  # noqa: E501
        :rtype: bool
        """
        return self._skip_cert_verify

    @skip_cert_verify.setter
    def skip_cert_verify(self, skip_cert_verify):
        """Sets the skip_cert_verify of this ScannerRegistrationReq.

        Indicate if skip the certificate verification when sending HTTP requests  # noqa: E501

        :param skip_cert_verify: The skip_cert_verify of this ScannerRegistrationReq.  # noqa: E501
        :type: bool
        """

        self._skip_cert_verify = skip_cert_verify

    @property
    def use_internal_addr(self):
        """Gets the use_internal_addr of this ScannerRegistrationReq.  # noqa: E501

        Indicate whether use internal registry addr for the scanner to pull content or not  # noqa: E501

        :return: The use_internal_addr of this ScannerRegistrationReq.  # noqa: E501
        :rtype: bool
        """
        return self._use_internal_addr

    @use_internal_addr.setter
    def use_internal_addr(self, use_internal_addr):
        """Sets the use_internal_addr of this ScannerRegistrationReq.

        Indicate whether use internal registry addr for the scanner to pull content or not  # noqa: E501

        :param use_internal_addr: The use_internal_addr of this ScannerRegistrationReq.  # noqa: E501
        :type: bool
        """

        self._use_internal_addr = use_internal_addr

    @property
    def disabled(self):
        """Gets the disabled of this ScannerRegistrationReq.  # noqa: E501

        Indicate whether the registration is enabled or not  # noqa: E501

        :return: The disabled of this ScannerRegistrationReq.  # noqa: E501
        :rtype: bool
        """
        return self._disabled

    @disabled.setter
    def disabled(self, disabled):
        """Sets the disabled of this ScannerRegistrationReq.

        Indicate whether the registration is enabled or not  # noqa: E501

        :param disabled: The disabled of this ScannerRegistrationReq.  # noqa: E501
        :type: bool
        """

        self._disabled = disabled

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
        if issubclass(ScannerRegistrationReq, dict):
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
        if not isinstance(other, ScannerRegistrationReq):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ScannerRegistrationReq):
            return True

        return self.to_dict() != other.to_dict()
