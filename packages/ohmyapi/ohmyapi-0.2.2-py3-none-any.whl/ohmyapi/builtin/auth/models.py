from functools import wraps
from typing import List, Optional
from uuid import UUID

from passlib.context import CryptContext
from tortoise.contrib.pydantic import pydantic_queryset_creator

from ohmyapi.db import Model, field, pre_delete, pre_save
from ohmyapi.router import HTTPException

pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")


class Group(Model):
    id: UUID = field.data.UUIDField(pk=True)
    name: str = field.CharField(max_length=42, index=True)


class User(Model):
    id: UUID = field.data.UUIDField(pk=True)
    email: str = field.CharField(max_length=255, unique=True, index=True)
    username: str = field.CharField(max_length=150, unique=True)
    password_hash: str = field.CharField(max_length=128)
    is_admin: bool = field.BooleanField(default=False)
    is_staff: bool = field.BooleanField(default=False)
    groups: field.ManyToManyRelation[Group] = field.ManyToManyField(
        "ohmyapi_auth.Group", related_name="users", through="usergroups"
    )

    class Schema:
        exclude = ("password_hash",)

    def set_password(self, raw_password: str) -> None:
        """Hash and store the password."""
        self.password_hash = pwd_context.hash(raw_password)

    def verify_password(self, raw_password: str) -> bool:
        """Verify a plaintext password against the stored hash."""
        return pwd_context.verify(raw_password, self.password_hash)

    @classmethod
    async def authenticate(cls, username: str, password: str) -> Optional["User"]:
        """Authenticate a user by username and password."""
        user = await cls.filter(username=username).first()
        if user and user.verify_password(password):
            return user
        return None
