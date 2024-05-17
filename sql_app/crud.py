from sqlalchemy.orm import Session

from . import models, schemas

def get_expresion(db: Session, expresion_id: int):
    return db.query(models.Expresion).filter(models.Expresion.id == expresion_id).first()

def get_expresiones(db: Session):
    return db.query(models.Expresion).all()

def create_expresion(db: Session, expresion: schemas.ExpresionCreate):
    db_expresion = models.Expresion(fecha=expresion.fecha,
        resolucion=expresion.resolucion,
        clasificacion=expresion.clasificacion,
        expresion=expresion.expresion,
        contenido=expresion.contenido,
        departamento=expresion.departamento,
        provincia=expresion.provincia,
        distrito=expresion.distrito)
    db.add(db_expresion)
    db.commit()
    db.refresh(db_expresion)
    return db_expresion