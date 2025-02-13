from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..core.database import get_db
from . import schemas, crud
from ..auth.utils import oauth2_scheme

router = APIRouter()

@router.post("/", response_model=schemas.CMDBItem)
def create_cmdb_item(
    item: schemas.CMDBItemCreate,
    db: Session = Depends(get_db),
    token: str = Depends(oauth2_scheme)
):
    return crud.create_cmdb_item(db=db, item=item, owner_id=1)  # 简化版本，应该从token获取用户ID

@router.get("/", response_model=list[schemas.CMDBItem])
def read_cmdb_items(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    token: str = Depends(oauth2_scheme)
):
    items = crud.get_cmdb_items(db, skip=skip, limit=limit)
    return items

@router.get("/{item_id}", response_model=schemas.CMDBItem)
def read_cmdb_item(
    item_id: int,
    db: Session = Depends(get_db),
    token: str = Depends(oauth2_scheme)
):
    db_item = crud.get_cmdb_item(db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item 