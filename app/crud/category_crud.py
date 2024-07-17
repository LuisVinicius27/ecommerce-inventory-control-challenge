from sqlalchemy.orm import Session
from app.models import Category
from app.schemas import CategoryCreate

def get_category(db: Session, category_id: int):
    return db.query(Category).filter(Category.id == category_id).first()

def create_category(db: Session, category: CategoryCreate):
    db_category = Category(description=category.description)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category