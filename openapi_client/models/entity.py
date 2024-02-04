# coding: utf-8

"""
    Querido Diário

    API to access the gazettes from all Brazilian cities

    The version of the OpenAPI document: 0.17.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import List
from pydantic import BaseModel, Field, StrictStr, conlist

class Entity(BaseModel):
    """
    Entity
    """
    entity_type: StrictStr = Field(...)
    entity_type_description: StrictStr = Field(...)
    entities: conlist(StrictStr) = Field(...)
    __properties = ["entity_type", "entity_type_description", "entities"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Entity:
        """Create an instance of Entity from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Entity:
        """Create an instance of Entity from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Entity.parse_obj(obj)

        _obj = Entity.parse_obj({
            "entity_type": obj.get("entity_type"),
            "entity_type_description": obj.get("entity_type_description"),
            "entities": obj.get("entities")
        })
        return _obj


