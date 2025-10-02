from typing import Type
from contentgrid_extension_helpers.dependencies.sqlalch.repositories import BaseRepository
from sqlmodel import Session
from server.types.foo import Foo, FooCreate, FooUpdate

class FooRepository(BaseRepository[Foo, FooCreate, FooUpdate]):
    def __init__(self, session: Session):
        super().__init__(session, Foo)