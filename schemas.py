from pydantic import BaseModel


class DriverBase(BaseModel):
    number: int
    name: str
    nationality: str


class DriverCreate(BaseModel):
    number: int
    name: str
    nationality: str


class Driver(DriverBase):
    id: int

    class Config:
        orm_mode = True


class TeamBase(BaseModel):
    name: str
    country: str


class TeamCreate(TeamBase):
    pass


class Team(TeamBase):
    id: int

    class Config:
        orm_mode = True


class CircuitBase(BaseModel):
    name: str
    country: str


class CircuitCreate(CircuitBase):
    pass


class Circuit(CircuitBase):
    id: int

    class Config:
        orm_mode = True
