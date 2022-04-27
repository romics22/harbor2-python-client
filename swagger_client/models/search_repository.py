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


class SearchRepository(object):
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
        'project_id': 'int',
        'project_name': 'str',
        'project_public': 'bool',
        'repository_name': 'str',
        'pull_count': 'int',
        'artifact_count': 'int'
    }

    attribute_map = {
        'project_id': 'project_id',
        'project_name': 'project_name',
        'project_public': 'project_public',
        'repository_name': 'repository_name',
        'pull_count': 'pull_count',
        'artifact_count': 'artifact_count'
    }

    def __init__(self, project_id=None, project_name=None, project_public=None, repository_name=None, pull_count=None, artifact_count=None, _configuration=None):  # noqa: E501
        """SearchRepository - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._project_id = None
        self._project_name = None
        self._project_public = None
        self._repository_name = None
        self._pull_count = None
        self._artifact_count = None
        self.discriminator = None

        if project_id is not None:
            self.project_id = project_id
        if project_name is not None:
            self.project_name = project_name
        if project_public is not None:
            self.project_public = project_public
        if repository_name is not None:
            self.repository_name = repository_name
        if pull_count is not None:
            self.pull_count = pull_count
        if artifact_count is not None:
            self.artifact_count = artifact_count

    @property
    def project_id(self):
        """Gets the project_id of this SearchRepository.  # noqa: E501

        The ID of the project that the repository belongs to  # noqa: E501

        :return: The project_id of this SearchRepository.  # noqa: E501
        :rtype: int
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this SearchRepository.

        The ID of the project that the repository belongs to  # noqa: E501

        :param project_id: The project_id of this SearchRepository.  # noqa: E501
        :type: int
        """

        self._project_id = project_id

    @property
    def project_name(self):
        """Gets the project_name of this SearchRepository.  # noqa: E501

        The name of the project that the repository belongs to  # noqa: E501

        :return: The project_name of this SearchRepository.  # noqa: E501
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this SearchRepository.

        The name of the project that the repository belongs to  # noqa: E501

        :param project_name: The project_name of this SearchRepository.  # noqa: E501
        :type: str
        """

        self._project_name = project_name

    @property
    def project_public(self):
        """Gets the project_public of this SearchRepository.  # noqa: E501

        The flag to indicate the publicity of the project that the repository belongs to (1 is public, 0 is not)  # noqa: E501

        :return: The project_public of this SearchRepository.  # noqa: E501
        :rtype: bool
        """
        return self._project_public

    @project_public.setter
    def project_public(self, project_public):
        """Sets the project_public of this SearchRepository.

        The flag to indicate the publicity of the project that the repository belongs to (1 is public, 0 is not)  # noqa: E501

        :param project_public: The project_public of this SearchRepository.  # noqa: E501
        :type: bool
        """

        self._project_public = project_public

    @property
    def repository_name(self):
        """Gets the repository_name of this SearchRepository.  # noqa: E501

        The name of the repository  # noqa: E501

        :return: The repository_name of this SearchRepository.  # noqa: E501
        :rtype: str
        """
        return self._repository_name

    @repository_name.setter
    def repository_name(self, repository_name):
        """Sets the repository_name of this SearchRepository.

        The name of the repository  # noqa: E501

        :param repository_name: The repository_name of this SearchRepository.  # noqa: E501
        :type: str
        """

        self._repository_name = repository_name

    @property
    def pull_count(self):
        """Gets the pull_count of this SearchRepository.  # noqa: E501

        The count how many times the repository is pulled  # noqa: E501

        :return: The pull_count of this SearchRepository.  # noqa: E501
        :rtype: int
        """
        return self._pull_count

    @pull_count.setter
    def pull_count(self, pull_count):
        """Sets the pull_count of this SearchRepository.

        The count how many times the repository is pulled  # noqa: E501

        :param pull_count: The pull_count of this SearchRepository.  # noqa: E501
        :type: int
        """

        self._pull_count = pull_count

    @property
    def artifact_count(self):
        """Gets the artifact_count of this SearchRepository.  # noqa: E501

        The count of artifacts in the repository  # noqa: E501

        :return: The artifact_count of this SearchRepository.  # noqa: E501
        :rtype: int
        """
        return self._artifact_count

    @artifact_count.setter
    def artifact_count(self, artifact_count):
        """Sets the artifact_count of this SearchRepository.

        The count of artifacts in the repository  # noqa: E501

        :param artifact_count: The artifact_count of this SearchRepository.  # noqa: E501
        :type: int
        """

        self._artifact_count = artifact_count

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
        if issubclass(SearchRepository, dict):
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
        if not isinstance(other, SearchRepository):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SearchRepository):
            return True

        return self.to_dict() != other.to_dict()