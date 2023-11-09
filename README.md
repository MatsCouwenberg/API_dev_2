# API Development assignment: F1 API

## POST requests
````
@app.post("/drivers/new/", response_model=schemas.Driver)
def create_driver(driver: schemas.DriverCreate, db: Session = Depends(get_db)):
    return crud.create_driver(db=db, driver=driver)
````

````
@app.post("/teams/new/", response_model=schemas.Team)
def create_team(team: schemas.TeamCreate, db: Session = Depends(get_db)):
    return crud.create_team(db=db, team=team)
````

## GET requests

````
@app.get("/drivers/", response_model=list[schemas.Driver])
def read_drivers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    drivers = crud.get_drivers(db, skip=skip, limit=limit)
    return drivers

````

````
@app.get("/teams/", response_model=list[schemas.Team])
def read_teams(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    teams = crud.get_teams(db, skip=skip, limit=limit)
    return teams
````

## DELETE requests

````
@app.delete("/drivers/delete/{number}")
def delete_driver(number: int, db: Session = Depends(get_db)):
    driver = crud.get_driver_by_number(db, number)
    if driver is None:
        raise HTTPException(status_code=404, detail="Driver not found")
    crud.delete_driver(db, driver)
    return {"message": "Driver deleted"}

````

````
@app.delete("/drivers/delete-all")
def delete_all_drivers(db: Session = Depends(get_db)):
    crud.delete_all_drivers(db)
    return {"message": "All drivers deleted"}
````

````
@app.delete("/teams/delete-all")
def delete_all_teams(db: Session = Depends(get_db)):
    crud.delete_all_teams(db)
    return {"message": "All teams deleted"}
````
https://matscouwenberg.github.io/API_dev_1/