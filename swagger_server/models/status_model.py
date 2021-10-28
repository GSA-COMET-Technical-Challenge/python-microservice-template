# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class StatusModel(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, status: str=None):  # noqa: E501
        """StatusModel - a model defined in Swagger

        :param status: The status of this StatusModel.  # noqa: E501
        :type status: str
        """
        self.swagger_types = {
            'status': str
        }

        self.attribute_map = {
            'status': 'status'
        }
        self._status = status

    @classmethod
    def from_dict(cls, dikt) -> 'StatusModel':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The StatusModel of this StatusModel.  # noqa: E501
        :rtype: StatusModel
        """
        return util.deserialize_model(dikt, cls)

    @property
    def status(self) -> str:
        """Gets the status of this StatusModel.


        :return: The status of this StatusModel.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status: str):
        """Sets the status of this StatusModel.


        :param status: The status of this StatusModel.
        :type status: str
        """

        self._status = status