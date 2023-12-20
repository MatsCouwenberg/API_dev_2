from sqlalchemy.orm import Session

import models
import schemas

def delete_driver(db: Session, driver: models.Driver):
    db.delete(driver)
    db.commit()

def delete_team(db: Session, team: models.Team):
    db.delete(team)
    db.commit()

def delete_all_drivers(db: Session):
    drivers = db.query(models.Driver).all()
    for driver in drivers:
        db.delete(driver)
    db.commit()

def delete_all_teams(db: Session):
    teams = db.query(models.Team).all()
    for team in teams:
        db.delete(team)
    db.commit()

def create_driver(db: Session, driver: schemas.DriverCreate):
    db_driver = models.Driver(**driver.dict())
    db.add(db_driver)
    db.commit()
    db.refresh(db_driver)
    return db_driver

def get_drivers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Driver).offset(skip).limit(limit).all()

def get_driver_by_number(db: Session, number: int):
    return db.query(models.Driver).filter(models.Driver.number == number).first()

def get_driver_by_name(db: Session, name: str):
    return db.query(models.Driver).filter(models.Driver.name == name).first()

def create_team(db: Session, team: schemas.TeamCreate):
    db_team = models.Team(**team.dict())
    db.add(db_team)
    db.commit()
    db.refresh(db_team)
    return db_team

def get_teams(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Team).offset(skip).limit(limit).all()

def get_team_by_id(db: Session, id: int):
    return db.query(models.Team).filter(models.Team.id == id).first()

def get_team_by_name(db: Session, name: str):
    return db.query(models.Team).filter(models.Team.name == name).first()

def get_team_by_country(db: Session, country: str):
    return db.query(models.Team).filter(models.Team.country == country).first()

def create_circuit(db: Session, circuit: schemas.CircuitCreate):
    db_circuit = models.Circuit(**circuit.dict())
    db.add(db_circuit)
    db.commit()
    db.refresh(db_circuit)
    return db_circuit

def get_circuits(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Circuit).offset(skip).limit(limit).all()

def delete_all_circuits(db: Session):
    circuits = db.query(models.Circuit).all()
    for circuit in circuits:
        db.delete(circuit)
    db.commit()
