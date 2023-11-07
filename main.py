from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud
import models
import schemas
from database import SessionLocal, engine
import os

if not os.path.exists('./sqlitedb'):
    os.makedirs('./sqlitedb')

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create a Driver
@app.post("/drivers/new/", response_model=schemas.Driver)
def create_driver(driver: schemas.DriverCreate, db: Session = Depends(get_db)):
    return crud.create_driver(db=db, driver=driver)

# Get a list of Drivers
@app.get("/drivers/", response_model=list[schemas.Driver])
def read_drivers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    drivers = crud.get_drivers(db, skip=skip, limit=limit)
    return drivers

# Create a Team
@app.post("/teams/new/", response_model=schemas.Team)
def create_team(team: schemas.TeamCreate, db: Session = Depends(get_db)):
    return crud.create_team(db=db, team=team)

# Get a list of Teams
@app.get("/teams/", response_model=list[schemas.Team])
def read_teams(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    teams = crud.get_teams(db, skip=skip, limit=limit)
    return teams

# Delete driver by ID
@app.delete("/drivers/delete/{driver_id}")
def delete_driver(driver_id: int, db: Session = Depends(get_db)):
    driver = crud.get_driver_by_number(db, driver_id)
    if driver is None:
        raise HTTPException(status_code=404, detail="Driver not found")
    crud.delete_driver(db, driver)
    return {"message": "Driver deleted"}

# Delete all drivers
@app.delete("/drivers/delete-all")
def delete_all_drivers(db: Session = Depends(get_db)):
    crud.delete_all_drivers(db)
    return {"message": "All drivers deleted"}