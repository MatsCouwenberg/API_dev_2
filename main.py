from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

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

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create a Driver
@app.post("/drivers/new/", response_model=schemas.Driver)
def create_driver(driver: schemas.DriverCreate, db: Session = Depends(get_db)):
    return crud.create_driver(db=db, driver=driver)

#Get a driver by number
@app.get("/drivers/number/{number}", response_model=schemas.Driver)
def read_driver(number: int, db: Session = Depends(get_db)):
    driver = crud.get_driver_by_number(db, number=number)
    if driver is None:
        raise HTTPException(status_code=404, detail="Driver not found")
    return driver

#Get a driver by name
@app.get("/drivers/name/{name}", response_model=schemas.Driver)
def read_driver_by_name(name: str, db: Session = Depends(get_db)):
    driver = crud.get_driver_by_name(db, name=name)
    if driver is None:
        raise HTTPException(status_code=404, detail="Driver not found")
    return driver

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

# Get a team by name
@app.get("/teams/name/{name}", response_model=schemas.Team)
def read_team_by_name(name: str, db: Session = Depends(get_db)):
    team = crud.get_team_by_name(db, name=name)
    if team is None:
        raise HTTPException(status_code=404, detail="Team not found")
    return team

# Get a name by country
@app.get("/teams/country/{country}", response_model=schemas.Team)
def read_team_by_country(country: str, db: Session = Depends(get_db)):
    team = crud.get_team_by_country(db, country=country)
    if team is None:
        raise HTTPException(status_code=404, detail="Team not found")
    return team

# Delete driver by number
@app.delete("/drivers/delete/{number}")
def delete_driver(number: int, db: Session = Depends(get_db)):
    driver = crud.get_driver_by_number(db, number)
    if driver is None:
        raise HTTPException(status_code=404, detail="Driver not found")
    crud.delete_driver(db, driver)
    return {"message": "Driver deleted"}

# Delete all drivers
@app.delete("/drivers/delete-all")
def delete_all_drivers(db: Session = Depends(get_db)):
    crud.delete_all_drivers(db)
    return {"message": "All drivers deleted"}

# Delete all teams
@app.delete("/teams/delete-all")
def delete_all_teams(db: Session = Depends(get_db)):
    crud.delete_all_teams(db)
    return {"message": "All teams deleted"}

# Delete team by ID
@app.delete("/teams/delete/{id}")
def delete_team(id: int, db: Session = Depends(get_db)):
    team = crud.get_team_by_id(db, id)
    if team is None:
        raise HTTPException(status_code=404, detail="Team not found")
    crud.delete_driver(db, team)
    return {"message": "Team deleted"}