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


class UserProfile(object):
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
        'email': 'str',
        'realname': 'str',
        'comment': 'str'
    }

    attribute_map = {
        'email': 'email',
        'realname': 'realname',
        'comment': 'comment'
    }

    def __init__(self, email=None, realname=None, comment=None, _configuration=None):  # noqa: E501
        """UserProfile - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._email = None
        self._realname = None
        self._comment = None
        self.discriminator = None

        if email is not None:
            self.email = email
        if realname is not None:
            self.realname = realname
        if comment is not None:
            self.comment = comment

    @property
    def email(self):
        """Gets the email of this UserProfile.  # noqa: E501


        :return: The email of this UserProfile.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this UserProfile.


        :param email: The email of this UserProfile.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def realname(self):
        """Gets the realname of this UserProfile.  # noqa: E501


        :return: The realname of this UserProfile.  # noqa: E501
        :rtype: str
        """
        return self._realname

    @realname.setter
    def realname(self, realname):
        """Sets the realname of this UserProfile.


        :param realname: The realname of this UserProfile.  # noqa: E501
        :type: str
        """

        self._realname = realname

    @property
    def comment(self):
        """Gets the comment of this UserProfile.  # noqa: E501


        :return: The comment of this UserProfile.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this UserProfile.


        :param comment: The comment of this UserProfile.  # noqa: E501
        :type: str
        """

        self._comment = comment

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
        if issubclass(UserProfile, dict):
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
        if not isinstance(other, UserProfile):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UserProfile):
            return True

        return self.to_dict() != other.to_dict()
