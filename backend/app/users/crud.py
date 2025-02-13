from sqlalchemy.orm import Session
from ..core import models
from ..core.crud import CRUDBase
from . import schemas
from ..core.security import get_password_hash

class CRUDUser(CRUDBase[models.User, schemas.UserCreate, schemas.UserUpdate]):
    def get_by_email(self, db: Session, email: str):
        return db.query(models.User).filter(models.User.email == email).first()

    def create(self, db: Session, *, obj_in: schemas.UserCreate):
        db_obj = models.User(
            email=obj_in.email,
            hashed_password=get_password_hash(obj_in.password),
            is_active=True
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

# 创建 CRUD 实例
user = CRUDUser(models.User)