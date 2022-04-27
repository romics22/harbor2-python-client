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


class Access(object):
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
        'resource': 'str',
        'action': 'str',
        'effect': 'str'
    }

    attribute_map = {
        'resource': 'resource',
        'action': 'action',
        'effect': 'effect'
    }

    def __init__(self, resource=None, action=None, effect=None, _configuration=None):  # noqa: E501
        """Access - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._resource = None
        self._action = None
        self._effect = None
        self.discriminator = None

        if resource is not None:
            self.resource = resource
        if action is not None:
            self.action = action
        if effect is not None:
            self.effect = effect

    @property
    def resource(self):
        """Gets the resource of this Access.  # noqa: E501

        The resource of the access  # noqa: E501

        :return: The resource of this Access.  # noqa: E501
        :rtype: str
        """
        return self._resource

    @resource.setter
    def resource(self, resource):
        """Sets the resource of this Access.

        The resource of the access  # noqa: E501

        :param resource: The resource of this Access.  # noqa: E501
        :type: str
        """

        self._resource = resource

    @property
    def action(self):
        """Gets the action of this Access.  # noqa: E501

        The action of the access  # noqa: E501

        :return: The action of this Access.  # noqa: E501
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this Access.

        The action of the access  # noqa: E501

        :param action: The action of this Access.  # noqa: E501
        :type: str
        """

        self._action = action

    @property
    def effect(self):
        """Gets the effect of this Access.  # noqa: E501

        The effect of the access  # noqa: E501

        :return: The effect of this Access.  # noqa: E501
        :rtype: str
        """
        return self._effect

    @effect.setter
    def effect(self, effect):
        """Sets the effect of this Access.

        The effect of the access  # noqa: E501

        :param effect: The effect of this Access.  # noqa: E501
        :type: str
        """

        self._effect = effect

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
        if issubclass(Access, dict):
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
        if not isinstance(other, Access):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Access):
            return True

        return self.to_dict() != other.to_dict()
