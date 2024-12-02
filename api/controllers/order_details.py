from sqlalchemy.orm import Session
from api.models import models, schemas

def create_order_detail(db: Session, order_detail: schemas.OrderDetailCreate):
    db_order_detail = models.OrderDetail(order_id=order_detail.order_id, sandwich_id=order_detail.sandwich_id, quantity=order_detail.quantity)
    db.add(db_order_detail)
    db.commit()
    db.refresh(db_order_detail)
    return db_order_detail

def get_all_order_details(db: Session):
    return db.query(models.OrderDetail).all()

def get_order_detail_by_id(db: Session, order_detail_id: int):
    return db.query(models.OrderDetail).filter(models.OrderDetail.id == order_detail_id).first()

def update_order_detail(db: Session, order_detail_id: int, order_detail: schemas.OrderDetailUpdate):
    db_order_detail = db.query(models.OrderDetail).filter(models.OrderDetail.id == order_detail_id)
    if not db_order_detail.first():
        return None
    db_order_detail.update(order_detail.dict(), synchronize_session=False)
    db.commit()
    return db_order_detail.first()

def delete_order_detail(db: Session, order_detail_id: int):
    db_order_detail = db.query(models.OrderDetail).filter(models.OrderDetail.id == order_detail_id)
    if not db_order_detail.first():
        return None
    db_order_detail.delete(synchronize_session=False)
    db.commit()
    return True
