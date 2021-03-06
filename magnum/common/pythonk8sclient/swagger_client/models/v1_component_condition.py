# coding: utf-8

"""
Copyright 2015 SmartBear Software

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from pprint import pformat
from six import iteritems


class V1ComponentCondition(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        Swagger model

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'type': 'str',
            'status': 'str',
            'message': 'str',
            'error': 'str'
        }

        self.attribute_map = {
            'type': 'type',
            'status': 'status',
            'message': 'message',
            'error': 'error'
        }

        self._type = None
        self._status = None
        self._message = None
        self._error = None

    @property
    def type(self):
        """
        Gets the type of this V1ComponentCondition.
        type of component condition, currently only Healthy

        :return: The type of this V1ComponentCondition.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this V1ComponentCondition.
        type of component condition, currently only Healthy

        :param type: The type of this V1ComponentCondition.
        :type: str
        """
        self._type = type

    @property
    def status(self):
        """
        Gets the status of this V1ComponentCondition.
        current status of this component condition, one of True, False, Unknown

        :return: The status of this V1ComponentCondition.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this V1ComponentCondition.
        current status of this component condition, one of True, False, Unknown

        :param status: The status of this V1ComponentCondition.
        :type: str
        """
        self._status = status

    @property
    def message(self):
        """
        Gets the message of this V1ComponentCondition.
        health check message received from the component

        :return: The message of this V1ComponentCondition.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this V1ComponentCondition.
        health check message received from the component

        :param message: The message of this V1ComponentCondition.
        :type: str
        """
        self._message = message

    @property
    def error(self):
        """
        Gets the error of this V1ComponentCondition.
        error code from health check attempt (if any)

        :return: The error of this V1ComponentCondition.
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        """
        Sets the error of this V1ComponentCondition.
        error code from health check attempt (if any)

        :param error: The error of this V1ComponentCondition.
        :type: str
        """
        self._error = error

    def to_dict(self):
        """
        Return model properties dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Return model properties str
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()
