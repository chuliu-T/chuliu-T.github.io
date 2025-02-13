from pydantic import BaseModel

class CMDBItemBase(BaseModel):
    name: str
    type: str
    description: str | None = None

class CMDBItemCreate(CMDBItemBase):
    pass

class CMDBItem(CMDBItemBase):
    id: int
    owner_id: int

    class Config:
        from_attributes = True 