
from typing import Annotated, List
from fastapi import APIRouter, Depends, FastAPI, Query
from fastapi.concurrency import asynccontextmanager

from server.repositories.foo_repo import FooRepository
from server.types.foo import Foo, FooCreate, FooUpdate, FooPublic
from server.dependencies import get_foo_repository, db_factory


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Lifespan of the fast API router. Code before the yield is executed when the application starts
    # and code after the yield is executed when the application stops.
    db_factory.create_db_and_tables()
    yield
    # Clean up the ML models and release the resources
    # delete_db()
    
foo_router = APIRouter(lifespan=lifespan, prefix="/foos", tags=["foo"])

@foo_router.post("/", response_model=FooPublic)
def create_foo(
    foo: FooCreate, 
    foo_repo: FooRepository = Depends(get_foo_repository)
):
    """Create new foo"""
    foo = foo_repo.create(foo)
    return foo

@foo_router.get("/", response_model=List[FooPublic])
def read_foos(
    foo_repo: FooRepository = Depends(get_foo_repository),
    offset: int = 0,
    limit: Annotated[int, Query(le=100)] = 100,
):
    """Get all foos with pagination"""
    return foo_repo.get_all(offset=offset, limit=limit)

@foo_router.get("/{foo_id}", response_model=FooPublic)
def read_foo(
    foo_id: int, 
    foo_repo: FooRepository = Depends(get_foo_repository)
):
    """Get foo by ID"""
    return foo_repo.get_by_id(foo_id)

@foo_router.patch("/{foo_id}", response_model=FooPublic)
def update_foo(
    foo_id: int, 
    foo: FooUpdate, 
    foo_repo: FooRepository = Depends(get_foo_repository)
):
    """Update foo"""
    return foo_repo.update(foo_id, foo)

@foo_router.delete("/{foo_id}")
def delete_foo(
    foo_id: int,
    foo_repo: FooRepository = Depends(get_foo_repository)
):
    """Delete foo and all related records"""
    # Get the foo first (to check if it exists and for S3 operations)
    return foo_repo.delete(foo_id)