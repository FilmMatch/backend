from fastapi_sqlalchemy import db

def create(instance):
    db.session.add(instance)
    db.session.commit()
    db.session.refresh(instance)
    return instance

def delete(instance):
    db.session.add(instance)
    db.session.commit()
    db.session.refresh(instance)
    return instance

def update(instance):
    db.session.commit()
    db.session.refresh(instance)
    return instance
