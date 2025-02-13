from sqlalchemy.orm import Session
from ..core import models
from ..core.crud import CRUDBase
from . import schemas

class CRUDCMDBItem(CRUDBase[models.CMDBItem, schemas.CMDBItemCreate, schemas.CMDBItemUpdate]):
    def get_by_name(self, db: Session, name: str):
        return db.query(models.CMDBItem).filter(models.CMDBItem.name == name).first()

    def get_by_owner(self, db: Session, owner_id: int):
        return db.query(models.CMDBItem).filter(models.CMDBItem.owner_id == owner_id).all()

def get_cmdb_item(db: Session, item_id: int):
    return db.query(models.CMDBItem).filter(models.CMDBItem.id == item_id).first()

def get_cmdb_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.CMDBItem).offset(skip).limit(limit).all()

def create_cmdb_item(db: Session, item: schemas.CMDBItemCreate, owner_id: int):
    db_item = models.CMDBItem(**item.dict(), owner_id=owner_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item 