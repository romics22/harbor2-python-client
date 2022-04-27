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


class RegistryUpdate(object):
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
        'credential_type': 'str',
        'access_key': 'str',
        'access_secret': 'str',
        'insecure': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'url': 'url',
        'credential_type': 'credential_type',
        'access_key': 'access_key',
        'access_secret': 'access_secret',
        'insecure': 'insecure'
    }

    def __init__(self, name=None, description=None, url=None, credential_type=None, access_key=None, access_secret=None, insecure=None, _configuration=None):  # noqa: E501
        """RegistryUpdate - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._name = None
        self._description = None
        self._url = None
        self._credential_type = None
        self._access_key = None
        self._access_secret = None
        self._insecure = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if url is not None:
            self.url = url
        if credential_type is not None:
            self.credential_type = credential_type
        if access_key is not None:
            self.access_key = access_key
        if access_secret is not None:
            self.access_secret = access_secret
        if insecure is not None:
            self.insecure = insecure

    @property
    def name(self):
        """Gets the name of this RegistryUpdate.  # noqa: E501

        The registry name.  # noqa: E501

        :return: The name of this RegistryUpdate.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this RegistryUpdate.

        The registry name.  # noqa: E501

        :param name: The name of this RegistryUpdate.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this RegistryUpdate.  # noqa: E501

        Description of the registry.  # noqa: E501

        :return: The description of this RegistryUpdate.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this RegistryUpdate.

        Description of the registry.  # noqa: E501

        :param description: The description of this RegistryUpdate.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def url(self):
        """Gets the url of this RegistryUpdate.  # noqa: E501

        The registry URL.  # noqa: E501

        :return: The url of this RegistryUpdate.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this RegistryUpdate.

        The registry URL.  # noqa: E501

        :param url: The url of this RegistryUpdate.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def credential_type(self):
        """Gets the credential_type of this RegistryUpdate.  # noqa: E501

        Credential type of the registry, e.g. 'basic'.  # noqa: E501

        :return: The credential_type of this RegistryUpdate.  # noqa: E501
        :rtype: str
        """
        return self._credential_type

    @credential_type.setter
    def credential_type(self, credential_type):
        """Sets the credential_type of this RegistryUpdate.

        Credential type of the registry, e.g. 'basic'.  # noqa: E501

        :param credential_type: The credential_type of this RegistryUpdate.  # noqa: E501
        :type: str
        """

        self._credential_type = credential_type

    @property
    def access_key(self):
        """Gets the access_key of this RegistryUpdate.  # noqa: E501

        The registry access key.  # noqa: E501

        :return: The access_key of this RegistryUpdate.  # noqa: E501
        :rtype: str
        """
        return self._access_key

    @access_key.setter
    def access_key(self, access_key):
        """Sets the access_key of this RegistryUpdate.

        The registry access key.  # noqa: E501

        :param access_key: The access_key of this RegistryUpdate.  # noqa: E501
        :type: str
        """

        self._access_key = access_key

    @property
    def access_secret(self):
        """Gets the access_secret of this RegistryUpdate.  # noqa: E501

        The registry access secret.  # noqa: E501

        :return: The access_secret of this RegistryUpdate.  # noqa: E501
        :rtype: str
        """
        return self._access_secret

    @access_secret.setter
    def access_secret(self, access_secret):
        """Sets the access_secret of this RegistryUpdate.

        The registry access secret.  # noqa: E501

        :param access_secret: The access_secret of this RegistryUpdate.  # noqa: E501
        :type: str
        """

        self._access_secret = access_secret

    @property
    def insecure(self):
        """Gets the insecure of this RegistryUpdate.  # noqa: E501

        Whether or not the certificate will be verified when Harbor tries to access the server.  # noqa: E501

        :return: The insecure of this RegistryUpdate.  # noqa: E501
        :rtype: bool
        """
        return self._insecure

    @insecure.setter
    def insecure(self, insecure):
        """Sets the insecure of this RegistryUpdate.

        Whether or not the certificate will be verified when Harbor tries to access the server.  # noqa: E501

        :param insecure: The insecure of this RegistryUpdate.  # noqa: E501
        :type: bool
        """

        self._insecure = insecure

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
        if issubclass(RegistryUpdate, dict):
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
        if not isinstance(other, RegistryUpdate):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RegistryUpdate):
            return True

        return self.to_dict() != other.to_dict()
