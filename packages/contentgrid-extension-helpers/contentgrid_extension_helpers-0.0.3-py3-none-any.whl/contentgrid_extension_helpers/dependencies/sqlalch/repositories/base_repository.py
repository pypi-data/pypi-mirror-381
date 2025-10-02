from typing import Dict, Generic, List, Type, TypeVar
from contentgrid_hal_client import NotFound
from sqlmodel import SQLModel, Session, select


T = TypeVar('T', bound=SQLModel)
CreateT = TypeVar('CreateT', bound=SQLModel)
UpdateT = TypeVar('UpdateT', bound=SQLModel)

class BaseRepository(Generic[T, CreateT, UpdateT]):
    """Generic base repository for database operations"""

    def __init__(self, session: Session, model_class: Type[T]):
        self.session = session
        self.model_class = model_class

    def create(self, create_model: CreateT) -> T:
        """Create a new entity"""
        db_entity = self.model_class.model_validate(create_model)
        self.session.add(db_entity)
        self.session.commit()
        self.session.refresh(db_entity)
        return db_entity

    def get_by_id(self, entity_id: int) -> T:
        """Get entity by ID"""
        entity = self.session.get(self.model_class, entity_id)
        if not entity:
            raise NotFound(f"{self.model_class.__name__} with id {entity_id} not found")
        return entity

    def get_all(self, offset: int = 0, limit: int = 100) -> List[T]:
        # user filter has to be pre query for no error pagination 
        """Get all entities with pagination"""
        return self.session.exec(select(self.model_class).offset(offset).limit(limit)).all()

    def update(self, entity_id: int, update_model: UpdateT) -> T:
        """Update entity by ID"""
        db_entity = self.get_by_id(entity_id)
        update_data = update_model.model_dump(exclude_unset=True)
        db_entity.sqlmodel_update(update_data)
        self.session.add(db_entity)
        self.session.commit()
        self.session.refresh(db_entity)
        return db_entity

    def delete(self, entity_id: int) -> Dict[str, bool]:
        """Delete entity by ID"""
        db_entity = self.get_by_id(entity_id)
        self.session.delete(db_entity)
        self.session.commit()
        return {"ok": True}