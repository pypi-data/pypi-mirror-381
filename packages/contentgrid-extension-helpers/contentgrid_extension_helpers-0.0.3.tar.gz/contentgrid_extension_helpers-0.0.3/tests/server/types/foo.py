from typing import Optional, List
from pydantic import Field as PydanticField
from sqlmodel import Field, SQLModel, Relationship


class FooBase(SQLModel):
    # Base model for Foo
    # Not used on its own, but as a base for Foo, FooCreate, and FooUpdate
    # All fields set here will be inherited so are therefore publicly accessible
    # For private fields that should not be publicly accessible, use the main Foo class
    name: str = Field(index=True, description="Name of the Foo")
    description : str = Field(default=None, index=True, description="Description of the Foo")

class Foo(FooBase, table=True):
    # Main Foo model, this is the model where you will code your business logic with
    # Note that this model inherits from FooBase, so it has the same fields
    id : Optional[int] = Field(default=None, primary_key=True)
    secret_s3_path : Optional[str]


class FooPublic(FooBase):
    # A read-only version of the Foo model that can be used for public API responses
    # Note that this model inherits from FooBase, so it has the same fields
    # and also explicitly defined the id field so that is also publicly accessible
    # id is not added in the BaseModel because on creation it is not known yet
    id : int

class FooCreate(FooBase):
    # Model for creating a new Foo
    secret_s3_path : str = Field(..., description="S3 path where the Foo is stored")

class FooUpdate(FooBase):
    # Model for updating an existing Foo
    # All fields are optional, so you can only update the fields you want
    name : Optional[str] = Field(None, description="New name of the dataset")
    description : Optional[str] = Field(None, description="New description of the dataset")
    secret_s3_path : Optional[str] = Field(None, description="New secret s3 path of the dataset") 
