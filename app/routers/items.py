from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import crud, models, schemas, database

router = APIRouter(prefix="/items", tags=["items"])

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[schemas.Item])
def read_items(db:Session = Depends(get_db)):
    return crud.get_items(db)

@router.get("/{item_id}", response_model=schemas.Item)
def read_item(item_id:int, db: Session=Depends(get_db)):
    return crud.get_item(db, item_id)

@router.post("/", response_model=schemas.Item)
def create_item(item:schemas.ItemCreate,db: Session = Depends(get_db)):
    return crud.create_item(db, item)

