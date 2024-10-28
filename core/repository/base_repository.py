from typing import Type, TypeVar, Generic, List, Optional

from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

T = TypeVar("T")


class BaseRepository(Generic[T]):

    def __init__(self, model: Type[T]):
        self.model = model

    def get_by_id(self, db: Session, obj_id: int) -> Optional[T]:
        try:
            return db.query(self.model).filter(self.model.id == obj_id).first()
        except SQLAlchemyError as e:
            db.rollback()
            print(f"Error retrieving record: {e}")
            return None

    def get_all(self, db: Session) -> List[T]:
        try:
            return db.query(self.model).all()
        except SQLAlchemyError as e:
            db.rollback()
            print(f"Error retrieving records: {e}")
            return []

    def create(self, db: Session, obj_data: dict) -> T:
        try:
            obj = self.model(**obj_data)
            db.add(obj)
            db.commit()
            db.refresh(obj)
            return obj
        except SQLAlchemyError as e:
            db.rollback()
            print(f"Error creating record: {e}")
            return None

    def update(self, db: Session, obj_id: int, obj_data: dict) -> Optional[T]:
        try:
            obj = db.query(self.model).filter(self.model.id == obj_id).first()
            if obj:
                for key, value in obj_data.items():
                    setattr(obj, key, value)
                db.commit()
                db.refresh(obj)
            return obj
        except SQLAlchemyError as e:
            db.rollback()
            print(f"Error updating record: {e}")
            return None

    def delete(self, db: Session, obj_id: int) -> bool:
        try:
            obj = db.query(self.model).filter(self.model.id == obj_id).first()
            if obj:
                db.delete(obj)
                db.commit()
                return True
            return False
        except SQLAlchemyError as e:
            db.rollback()
            print(f"Error deleting record: {e}")
            return False
