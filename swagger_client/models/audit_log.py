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


class AuditLog(object):
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
        'id': 'int',
        'username': 'str',
        'resource': 'str',
        'resource_type': 'str',
        'operation': 'str',
        'op_time': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'username': 'username',
        'resource': 'resource',
        'resource_type': 'resource_type',
        'operation': 'operation',
        'op_time': 'op_time'
    }

    def __init__(self, id=None, username=None, resource=None, resource_type=None, operation=None, op_time=None, _configuration=None):  # noqa: E501
        """AuditLog - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._username = None
        self._resource = None
        self._resource_type = None
        self._operation = None
        self._op_time = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if username is not None:
            self.username = username
        if resource is not None:
            self.resource = resource
        if resource_type is not None:
            self.resource_type = resource_type
        if operation is not None:
            self.operation = operation
        if op_time is not None:
            self.op_time = op_time

    @property
    def id(self):
        """Gets the id of this AuditLog.  # noqa: E501

        The ID of the audit log entry.  # noqa: E501

        :return: The id of this AuditLog.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AuditLog.

        The ID of the audit log entry.  # noqa: E501

        :param id: The id of this AuditLog.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def username(self):
        """Gets the username of this AuditLog.  # noqa: E501

        Username of the user in this log entry.  # noqa: E501

        :return: The username of this AuditLog.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this AuditLog.

        Username of the user in this log entry.  # noqa: E501

        :param username: The username of this AuditLog.  # noqa: E501
        :type: str
        """

        self._username = username

    @property
    def resource(self):
        """Gets the resource of this AuditLog.  # noqa: E501

        Name of the repository in this log entry.  # noqa: E501

        :return: The resource of this AuditLog.  # noqa: E501
        :rtype: str
        """
        return self._resource

    @resource.setter
    def resource(self, resource):
        """Sets the resource of this AuditLog.

        Name of the repository in this log entry.  # noqa: E501

        :param resource: The resource of this AuditLog.  # noqa: E501
        :type: str
        """

        self._resource = resource

    @property
    def resource_type(self):
        """Gets the resource_type of this AuditLog.  # noqa: E501

        Tag of the repository in this log entry.  # noqa: E501

        :return: The resource_type of this AuditLog.  # noqa: E501
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this AuditLog.

        Tag of the repository in this log entry.  # noqa: E501

        :param resource_type: The resource_type of this AuditLog.  # noqa: E501
        :type: str
        """

        self._resource_type = resource_type

    @property
    def operation(self):
        """Gets the operation of this AuditLog.  # noqa: E501

        The operation against the repository in this log entry.  # noqa: E501

        :return: The operation of this AuditLog.  # noqa: E501
        :rtype: str
        """
        return self._operation

    @operation.setter
    def operation(self, operation):
        """Sets the operation of this AuditLog.

        The operation against the repository in this log entry.  # noqa: E501

        :param operation: The operation of this AuditLog.  # noqa: E501
        :type: str
        """

        self._operation = operation

    @property
    def op_time(self):
        """Gets the op_time of this AuditLog.  # noqa: E501

        The time when this operation is triggered.  # noqa: E501

        :return: The op_time of this AuditLog.  # noqa: E501
        :rtype: datetime
        """
        return self._op_time

    @op_time.setter
    def op_time(self, op_time):
        """Sets the op_time of this AuditLog.

        The time when this operation is triggered.  # noqa: E501

        :param op_time: The op_time of this AuditLog.  # noqa: E501
        :type: datetime
        """

        self._op_time = op_time

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
        if issubclass(AuditLog, dict):
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
        if not isinstance(other, AuditLog):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AuditLog):
            return True

        return self.to_dict() != other.to_dict()
