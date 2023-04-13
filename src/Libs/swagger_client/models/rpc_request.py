# coding: utf-8

"""
    Phantasma API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class RpcRequest(object):
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
        'jsonrpc': 'str',
        'method': 'str',
        'id': 'str',
        'params': 'list[object]'
    }

    attribute_map = {
        'jsonrpc': 'jsonrpc',
        'method': 'method',
        'id': 'id',
        'params': 'params'
    }

    def __init__(self, jsonrpc=None, method=None, id=None, params=None):  # noqa: E501
        """RpcRequest - a model defined in Swagger"""  # noqa: E501
        self._jsonrpc = None
        self._method = None
        self._id = None
        self._params = None
        self.discriminator = None
        if jsonrpc is not None:
            self.jsonrpc = jsonrpc
        if method is not None:
            self.method = method
        if id is not None:
            self.id = id
        if params is not None:
            self.params = params

    @property
    def jsonrpc(self):
        """Gets the jsonrpc of this RpcRequest.  # noqa: E501


        :return: The jsonrpc of this RpcRequest.  # noqa: E501
        :rtype: str
        """
        return self._jsonrpc

    @jsonrpc.setter
    def jsonrpc(self, jsonrpc):
        """Sets the jsonrpc of this RpcRequest.


        :param jsonrpc: The jsonrpc of this RpcRequest.  # noqa: E501
        :type: str
        """

        self._jsonrpc = jsonrpc

    @property
    def method(self):
        """Gets the method of this RpcRequest.  # noqa: E501


        :return: The method of this RpcRequest.  # noqa: E501
        :rtype: str
        """
        return self._method

    @method.setter
    def method(self, method):
        """Sets the method of this RpcRequest.


        :param method: The method of this RpcRequest.  # noqa: E501
        :type: str
        """

        self._method = method

    @property
    def id(self):
        """Gets the id of this RpcRequest.  # noqa: E501


        :return: The id of this RpcRequest.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this RpcRequest.


        :param id: The id of this RpcRequest.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def params(self):
        """Gets the params of this RpcRequest.  # noqa: E501


        :return: The params of this RpcRequest.  # noqa: E501
        :rtype: list[object]
        """
        return self._params

    @params.setter
    def params(self, params):
        """Sets the params of this RpcRequest.


        :param params: The params of this RpcRequest.  # noqa: E501
        :type: list[object]
        """

        self._params = params

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
        if issubclass(RpcRequest, dict):
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
        if not isinstance(other, RpcRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
