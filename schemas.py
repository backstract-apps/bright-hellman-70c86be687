from pydantic import BaseModel,Field,field_validator

import datetime

import uuid

from typing import Any, Dict, List,Optional,Tuple,Union

import re

class Users(BaseModel):
    email: Optional[str]=None
    password: Optional[str]=None
    created_at_dt: Optional[Any]=None


class ReadUsers(BaseModel):
    email: Optional[str]=None
    password: Optional[str]=None
    created_at_dt: Optional[Any]=None
    class Config:
        from_attributes = True


class ContactQueries(BaseModel):
    name: Optional[str]=None
    email: Optional[str]=None
    message: Optional[str]=None
    is_read: Optional[Union[int, float]]=None
    created_at_dt: Optional[Any]=None


class ReadContactQueries(BaseModel):
    name: Optional[str]=None
    email: Optional[str]=None
    message: Optional[str]=None
    is_read: Optional[Union[int, float]]=None
    created_at_dt: Optional[Any]=None
    class Config:
        from_attributes = True




class PostContactQueries(BaseModel):
    name: Optional[str]=None
    email: Optional[str]=None
    message: Optional[str]=None
    is_read: Optional[Union[int, float]]=None
    created_at_dt: Optional[str]=None

    class Config:
        from_attributes = True



class PutContactQueriesId(BaseModel):
    id: Union[int, float] = Field(...)
    name: Optional[str]=None
    email: Optional[str]=None
    message: Optional[str]=None
    is_read: Optional[Union[int, float]]=None
    created_at_dt: Optional[str]=None

    class Config:
        from_attributes = True



class PostPlatformAuthPackageMaysonAuthUserRegister(BaseModel):
    email: str = Field(..., max_length=100)
    password: str = Field(..., max_length=100)

    class Config:
        from_attributes = True



class PostUsers(BaseModel):
    email: Optional[str]=None
    password: Optional[str]=None
    created_at_dt: Optional[str]=None

    class Config:
        from_attributes = True



class PutUsersId(BaseModel):
    id: Union[int, float] = Field(...)
    email: Optional[str]=None
    password: Optional[str]=None
    created_at_dt: Optional[str]=None

    class Config:
        from_attributes = True



class PostPlatformAuthPackageMaysonAuthUserLogin(BaseModel):
    email: str = Field(..., max_length=100)
    password: str = Field(..., max_length=100)

    class Config:
        from_attributes = True



# Query Parameter Validation Schemas

class GetContactQueriesIdQueryParams(BaseModel):
    """Query parameter validation for get_contact_queries_id"""
    id: int = Field(..., ge=1, description="Id")

    class Config:
        populate_by_name = True


class GetUsersIdQueryParams(BaseModel):
    """Query parameter validation for get_users_id"""
    id: int = Field(..., ge=1, description="Id")

    class Config:
        populate_by_name = True


class DeleteUsersIdQueryParams(BaseModel):
    """Query parameter validation for delete_users_id"""
    id: int = Field(..., ge=1, description="Id")

    class Config:
        populate_by_name = True


class DeleteContactQueriesIdQueryParams(BaseModel):
    """Query parameter validation for delete_contact_queries_id"""
    id: int = Field(..., ge=1, description="Id")

    class Config:
        populate_by_name = True
