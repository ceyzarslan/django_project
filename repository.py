from typing import Generic, TypeVar, Type

from sqlalchemy.orm import Session

from models import Base

T = TypeVar('T', bound=Base)
# tek bir tane yazayım hepsi için çalışsın
class GenericRepository(Generic[T]):
    def __init__(self, model: Type[T], session: Session):
        self.model = model
        self.session = session

    def read_one(self, _id: int):
        return self.session.query(self.model).filter(self.model.id == _id).first()

    def read_all(self):
        return self.session.query(self.model).all()

    def create(self, entity: T) -> T:
        self.session.add(entity)
        self.session.commit()
        self.session.refresh()
        return entity

    def update (self,entity : T) -> T:
        self.session.commit()
        self.session.refresh(entity)
        return entity
    def delete (self,entity : T) -> None:
        self.session.delete(entity)
        self.session.commit()
        return entity