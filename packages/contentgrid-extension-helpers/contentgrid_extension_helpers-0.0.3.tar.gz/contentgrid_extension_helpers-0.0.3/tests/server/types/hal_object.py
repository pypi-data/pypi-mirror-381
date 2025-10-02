from typing import Optional, List
from pydantic import Field as PydanticField
from sqlmodel import Field, SQLModel, Relationship


class HALObjectBase(SQLModel):
    # Base model for HALObject
    # Not used on its own, but as a base for HALObject, HALObjectCreate, and HALObjectUpdate
    # All fields set here will be inherited so are therefore publicly accessible
    # For private fields that should not be publicly accessible, use the main HALObject class
    name: str = Field(index=True, description="Name of the HALObject")
    description : str = Field(default=None, index=True, description="Description of the HALObject")
    version_id : int = Field(default=0, index=True, description="int identifier version of the halobject")

class HALObject(HALObjectBase, table=True):
    # Main HALObject model, this is the model where you will code your business logic with
    # Note that this model inherits from HALObjectBase, so it has the same fields
    id : Optional[int] = Field(default=None, primary_key=True)


class HALObjectPublic(HALObjectBase):
    # A read-only version of the HALObject model that can be used for public API responses
    # Note that this model inherits from HALObjectBase, so it has the same fields
    # and also explicitly defined the id field so that is also publicly accessible
    # id is not added in the BaseModel because on creation it is not known yet
    id : int

class HALObjectCreate(HALObjectBase):
    # Model for creating a new HALObject
    secret_s3_path : str = Field(..., description="S3 path where the HALObject is stored")

class HALObjectUpdate(HALObjectBase):
    # Model for updating an existing HALObject
    # All fields are optional, so you can only update the fields you want
    name : Optional[str] = Field(None, description="New name of the dataset")
    description : Optional[str] = Field(None, description="New description of the dataset")
    secret_s3_path : Optional[str] = Field(None, description="New secret s3 path of the dataset") 
