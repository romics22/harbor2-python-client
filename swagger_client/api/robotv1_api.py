# coding: utf-8

"""
    Harbor API

    These APIs provide services for manipulating Harbor project.  # noqa: E501

    OpenAPI spec version: 2.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class Robotv1Api(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_robot_v1(self, project_name_or_id, robot, **kwargs):  # noqa: E501
        """Create a robot account  # noqa: E501

        Create a robot account  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_robot_v1(project_name_or_id, robot, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str project_name_or_id: The name or id of the project (required)
        :param RobotCreateV1 robot: The JSON object of a robot account. (required)
        :param str x_request_id: An unique ID for the request
        :param bool x_is_resource_name: The flag to indicate whether the parameter which supports both name and id in the path is the name of the resource. When the X-Is-Resource-Name is false and the parameter can be converted to an integer, the parameter will be as an id, otherwise, it will be as a name.
        :return: RobotCreated
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_robot_v1_with_http_info(project_name_or_id, robot, **kwargs)  # noqa: E501
        else:
            (data) = self.create_robot_v1_with_http_info(project_name_or_id, robot, **kwargs)  # noqa: E501
            return data

    def create_robot_v1_with_http_info(self, project_name_or_id, robot, **kwargs):  # noqa: E501
        """Create a robot account  # noqa: E501

        Create a robot account  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_robot_v1_with_http_info(project_name_or_id, robot, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str project_name_or_id: The name or id of the project (required)
        :param RobotCreateV1 robot: The JSON object of a robot account. (required)
        :param str x_request_id: An unique ID for the request
        :param bool x_is_resource_name: The flag to indicate whether the parameter which supports both name and id in the path is the name of the resource. When the X-Is-Resource-Name is false and the parameter can be converted to an integer, the parameter will be as an id, otherwise, it will be as a name.
        :return: RobotCreated
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['project_name_or_id', 'robot', 'x_request_id', 'x_is_resource_name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_robot_v1" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'project_name_or_id' is set
        if self.api_client.client_side_validation and ('project_name_or_id' not in params or
                                                       params['project_name_or_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `project_name_or_id` when calling `create_robot_v1`")  # noqa: E501
        # verify the required parameter 'robot' is set
        if self.api_client.client_side_validation and ('robot' not in params or
                                                       params['robot'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `robot` when calling `create_robot_v1`")  # noqa: E501

        if self.api_client.client_side_validation and ('x_request_id' in params and
                                                       len(params['x_request_id']) < 1):
            raise ValueError("Invalid value for parameter `x_request_id` when calling `create_robot_v1`, length must be greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'project_name_or_id' in params:
            path_params['project_name_or_id'] = params['project_name_or_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'x_request_id' in params:
            header_params['X-Request-Id'] = params['x_request_id']  # noqa: E501
        if 'x_is_resource_name' in params:
            header_params['X-Is-Resource-Name'] = params['x_is_resource_name']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'robot' in params:
            body_params = params['robot']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basic']  # noqa: E501

        return self.api_client.call_api(
            '/projects/{project_name_or_id}/robots', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RobotCreated',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_robot_v1(self, project_name_or_id, robot_id, **kwargs):  # noqa: E501
        """Delete a robot account  # noqa: E501

        This endpoint deletes specific robot account information by robot ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_robot_v1(project_name_or_id, robot_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str project_name_or_id: The name or id of the project (required)
        :param int robot_id: Robot ID (required)
        :param str x_request_id: An unique ID for the request
        :param bool x_is_resource_name: The flag to indicate whether the parameter which supports both name and id in the path is the name of the resource. When the X-Is-Resource-Name is false and the parameter can be converted to an integer, the parameter will be as an id, otherwise, it will be as a name.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_robot_v1_with_http_info(project_name_or_id, robot_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_robot_v1_with_http_info(project_name_or_id, robot_id, **kwargs)  # noqa: E501
            return data

    def delete_robot_v1_with_http_info(self, project_name_or_id, robot_id, **kwargs):  # noqa: E501
        """Delete a robot account  # noqa: E501

        This endpoint deletes specific robot account information by robot ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_robot_v1_with_http_info(project_name_or_id, robot_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str project_name_or_id: The name or id of the project (required)
        :param int robot_id: Robot ID (required)
        :param str x_request_id: An unique ID for the request
        :param bool x_is_resource_name: The flag to indicate whether the parameter which supports both name and id in the path is the name of the resource. When the X-Is-Resource-Name is false and the parameter can be converted to an integer, the parameter will be as an id, otherwise, it will be as a name.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['project_name_or_id', 'robot_id', 'x_request_id', 'x_is_resource_name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_robot_v1" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'project_name_or_id' is set
        if self.api_client.client_side_validation and ('project_name_or_id' not in params or
                                                       params['project_name_or_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `project_name_or_id` when calling `delete_robot_v1`")  # noqa: E501
        # verify the required parameter 'robot_id' is set
        if self.api_client.client_side_validation and ('robot_id' not in params or
                                                       params['robot_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `robot_id` when calling `delete_robot_v1`")  # noqa: E501

        if self.api_client.client_side_validation and ('x_request_id' in params and
                                                       len(params['x_request_id']) < 1):
            raise ValueError("Invalid value for parameter `x_request_id` when calling `delete_robot_v1`, length must be greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'project_name_or_id' in params:
            path_params['project_name_or_id'] = params['project_name_or_id']  # noqa: E501
        if 'robot_id' in params:
            path_params['robot_id'] = params['robot_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'x_request_id' in params:
            header_params['X-Request-Id'] = params['x_request_id']  # noqa: E501
        if 'x_is_resource_name' in params:
            header_params['X-Is-Resource-Name'] = params['x_is_resource_name']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basic']  # noqa: E501

        return self.api_client.call_api(
            '/projects/{project_name_or_id}/robots/{robot_id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_robot_by_idv1(self, project_name_or_id, robot_id, **kwargs):  # noqa: E501
        """Get a robot account  # noqa: E501

        This endpoint returns specific robot account information by robot ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_robot_by_idv1(project_name_or_id, robot_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str project_name_or_id: The name or id of the project (required)
        :param int robot_id: Robot ID (required)
        :param str x_request_id: An unique ID for the request
        :param bool x_is_resource_name: The flag to indicate whether the parameter which supports both name and id in the path is the name of the resource. When the X-Is-Resource-Name is false and the parameter can be converted to an integer, the parameter will be as an id, otherwise, it will be as a name.
        :return: Robot
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_robot_by_idv1_with_http_info(project_name_or_id, robot_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_robot_by_idv1_with_http_info(project_name_or_id, robot_id, **kwargs)  # noqa: E501
            return data

    def get_robot_by_idv1_with_http_info(self, project_name_or_id, robot_id, **kwargs):  # noqa: E501
        """Get a robot account  # noqa: E501

        This endpoint returns specific robot account information by robot ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_robot_by_idv1_with_http_info(project_name_or_id, robot_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str project_name_or_id: The name or id of the project (required)
        :param int robot_id: Robot ID (required)
        :param str x_request_id: An unique ID for the request
        :param bool x_is_resource_name: The flag to indicate whether the parameter which supports both name and id in the path is the name of the resource. When the X-Is-Resource-Name is false and the parameter can be converted to an integer, the parameter will be as an id, otherwise, it will be as a name.
        :return: Robot
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['project_name_or_id', 'robot_id', 'x_request_id', 'x_is_resource_name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_robot_by_idv1" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'project_name_or_id' is set
        if self.api_client.client_side_validation and ('project_name_or_id' not in params or
                                                       params['project_name_or_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `project_name_or_id` when calling `get_robot_by_idv1`")  # noqa: E501
        # verify the required parameter 'robot_id' is set
        if self.api_client.client_side_validation and ('robot_id' not in params or
                                                       params['robot_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `robot_id` when calling `get_robot_by_idv1`")  # noqa: E501

        if self.api_client.client_side_validation and ('x_request_id' in params and
                                                       len(params['x_request_id']) < 1):
            raise ValueError("Invalid value for parameter `x_request_id` when calling `get_robot_by_idv1`, length must be greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'project_name_or_id' in params:
            path_params['project_name_or_id'] = params['project_name_or_id']  # noqa: E501
        if 'robot_id' in params:
            path_params['robot_id'] = params['robot_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'x_request_id' in params:
            header_params['X-Request-Id'] = params['x_request_id']  # noqa: E501
        if 'x_is_resource_name' in params:
            header_params['X-Is-Resource-Name'] = params['x_is_resource_name']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basic']  # noqa: E501

        return self.api_client.call_api(
            '/projects/{project_name_or_id}/robots/{robot_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Robot',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_robot_v1(self, project_name_or_id, **kwargs):  # noqa: E501
        """Get all robot accounts of specified project  # noqa: E501

        Get all robot accounts of specified project  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_robot_v1(project_name_or_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str project_name_or_id: The name or id of the project (required)
        :param str x_request_id: An unique ID for the request
        :param bool x_is_resource_name: The flag to indicate whether the parameter which supports both name and id in the path is the name of the resource. When the X-Is-Resource-Name is false and the parameter can be converted to an integer, the parameter will be as an id, otherwise, it will be as a name.
        :param int page: The page number
        :param int page_size: The size of per page
        :param str q: Query string to query resources. Supported query patterns are \"exact match(k=v)\", \"fuzzy match(k=~v)\", \"range(k=[min~max])\", \"list with union releationship(k={v1 v2 v3})\" and \"list with intersetion relationship(k=(v1 v2 v3))\". The value of range and list can be string(enclosed by \" or '), integer or time(in format \"2020-04-09 02:36:00\"). All of these query patterns should be put in the query string \"q=xxx\" and splitted by \",\". e.g. q=k1=v1,k2=~v2,k3=[min~max]
        :param str sort: Sort the resource list in ascending or descending order. e.g. sort by field1 in ascending orderr and field2 in descending order with \"sort=field1,-field2\"
        :return: list[Robot]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_robot_v1_with_http_info(project_name_or_id, **kwargs)  # noqa: E501
        else:
            (data) = self.list_robot_v1_with_http_info(project_name_or_id, **kwargs)  # noqa: E501
            return data

    def list_robot_v1_with_http_info(self, project_name_or_id, **kwargs):  # noqa: E501
        """Get all robot accounts of specified project  # noqa: E501

        Get all robot accounts of specified project  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_robot_v1_with_http_info(project_name_or_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str project_name_or_id: The name or id of the project (required)
        :param str x_request_id: An unique ID for the request
        :param bool x_is_resource_name: The flag to indicate whether the parameter which supports both name and id in the path is the name of the resource. When the X-Is-Resource-Name is false and the parameter can be converted to an integer, the parameter will be as an id, otherwise, it will be as a name.
        :param int page: The page number
        :param int page_size: The size of per page
        :param str q: Query string to query resources. Supported query patterns are \"exact match(k=v)\", \"fuzzy match(k=~v)\", \"range(k=[min~max])\", \"list with union releationship(k={v1 v2 v3})\" and \"list with intersetion relationship(k=(v1 v2 v3))\". The value of range and list can be string(enclosed by \" or '), integer or time(in format \"2020-04-09 02:36:00\"). All of these query patterns should be put in the query string \"q=xxx\" and splitted by \",\". e.g. q=k1=v1,k2=~v2,k3=[min~max]
        :param str sort: Sort the resource list in ascending or descending order. e.g. sort by field1 in ascending orderr and field2 in descending order with \"sort=field1,-field2\"
        :return: list[Robot]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['project_name_or_id', 'x_request_id', 'x_is_resource_name', 'page', 'page_size', 'q', 'sort']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_robot_v1" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'project_name_or_id' is set
        if self.api_client.client_side_validation and ('project_name_or_id' not in params or
                                                       params['project_name_or_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `project_name_or_id` when calling `list_robot_v1`")  # noqa: E501

        if self.api_client.client_side_validation and ('x_request_id' in params and
                                                       len(params['x_request_id']) < 1):
            raise ValueError("Invalid value for parameter `x_request_id` when calling `list_robot_v1`, length must be greater than or equal to `1`")  # noqa: E501
        if self.api_client.client_side_validation and ('page_size' in params and params['page_size'] > 100):  # noqa: E501
            raise ValueError("Invalid value for parameter `page_size` when calling `list_robot_v1`, must be a value less than or equal to `100`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'project_name_or_id' in params:
            path_params['project_name_or_id'] = params['project_name_or_id']  # noqa: E501

        query_params = []
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'page_size' in params:
            query_params.append(('page_size', params['page_size']))  # noqa: E501
        if 'q' in params:
            query_params.append(('q', params['q']))  # noqa: E501
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501

        header_params = {}
        if 'x_request_id' in params:
            header_params['X-Request-Id'] = params['x_request_id']  # noqa: E501
        if 'x_is_resource_name' in params:
            header_params['X-Is-Resource-Name'] = params['x_is_resource_name']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basic']  # noqa: E501

        return self.api_client.call_api(
            '/projects/{project_name_or_id}/robots', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Robot]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_robot_v1(self, project_name_or_id, robot_id, robot, **kwargs):  # noqa: E501
        """Update status of robot account.  # noqa: E501

        Used to disable/enable a specified robot account.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_robot_v1(project_name_or_id, robot_id, robot, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str project_name_or_id: The name or id of the project (required)
        :param int robot_id: Robot ID (required)
        :param Robot robot: The JSON object of a robot account. (required)
        :param str x_request_id: An unique ID for the request
        :param bool x_is_resource_name: The flag to indicate whether the parameter which supports both name and id in the path is the name of the resource. When the X-Is-Resource-Name is false and the parameter can be converted to an integer, the parameter will be as an id, otherwise, it will be as a name.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_robot_v1_with_http_info(project_name_or_id, robot_id, robot, **kwargs)  # noqa: E501
        else:
            (data) = self.update_robot_v1_with_http_info(project_name_or_id, robot_id, robot, **kwargs)  # noqa: E501
            return data

    def update_robot_v1_with_http_info(self, project_name_or_id, robot_id, robot, **kwargs):  # noqa: E501
        """Update status of robot account.  # noqa: E501

        Used to disable/enable a specified robot account.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_robot_v1_with_http_info(project_name_or_id, robot_id, robot, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str project_name_or_id: The name or id of the project (required)
        :param int robot_id: Robot ID (required)
        :param Robot robot: The JSON object of a robot account. (required)
        :param str x_request_id: An unique ID for the request
        :param bool x_is_resource_name: The flag to indicate whether the parameter which supports both name and id in the path is the name of the resource. When the X-Is-Resource-Name is false and the parameter can be converted to an integer, the parameter will be as an id, otherwise, it will be as a name.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['project_name_or_id', 'robot_id', 'robot', 'x_request_id', 'x_is_resource_name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_robot_v1" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'project_name_or_id' is set
        if self.api_client.client_side_validation and ('project_name_or_id' not in params or
                                                       params['project_name_or_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `project_name_or_id` when calling `update_robot_v1`")  # noqa: E501
        # verify the required parameter 'robot_id' is set
        if self.api_client.client_side_validation and ('robot_id' not in params or
                                                       params['robot_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `robot_id` when calling `update_robot_v1`")  # noqa: E501
        # verify the required parameter 'robot' is set
        if self.api_client.client_side_validation and ('robot' not in params or
                                                       params['robot'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `robot` when calling `update_robot_v1`")  # noqa: E501

        if self.api_client.client_side_validation and ('x_request_id' in params and
                                                       len(params['x_request_id']) < 1):
            raise ValueError("Invalid value for parameter `x_request_id` when calling `update_robot_v1`, length must be greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'project_name_or_id' in params:
            path_params['project_name_or_id'] = params['project_name_or_id']  # noqa: E501
        if 'robot_id' in params:
            path_params['robot_id'] = params['robot_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'x_request_id' in params:
            header_params['X-Request-Id'] = params['x_request_id']  # noqa: E501
        if 'x_is_resource_name' in params:
            header_params['X-Is-Resource-Name'] = params['x_is_resource_name']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'robot' in params:
            body_params = params['robot']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basic']  # noqa: E501

        return self.api_client.call_api(
            '/projects/{project_name_or_id}/robots/{robot_id}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)