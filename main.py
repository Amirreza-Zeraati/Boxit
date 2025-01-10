from sqlalchemy import Boolean, Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import Session
from fastapi import FastAPI
from fastapi import HTTPException
from typing import List
from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from sqlalchemy import DateTime


DATABASE_URL = "postgresql://postgres:postgres@db:5432/steam"
engine = create_engine(DATABASE_URL)
session = Session(engine)
Base = declarative_base()


app = FastAPI()


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    wallet_balance = Column(Integer, default=0)
    profile_picture = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=True)


class UserBase(BaseModel):
    name: str
    email: str
    is_active: bool = True
    profile_picture: str = None


class UserCreate(UserBase):
    password: str


class UserResponse(UserBase):
    id: int
    name: str
    email: str
    is_active: bool
    wallet_balance: int
    profile_picture: Optional[str] = None
    created_at: Optional[datetime] = None

    class Config:
        from_attributes = True


class Game(Base):
    __tablename__ = "games"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)
    price = Column(Integer)
    release_date = Column(String)
    developer = Column(String)
    publisher = Column(String)
    genre = Column(String)
    rating = Column(Integer, default=0)
    cover_image = Column(String, nullable=True)


class GameBase(BaseModel):
    title: str
    description: str
    price: int
    release_date: str
    developer: str
    publisher: str
    genre: str
    rating: int = 0
    cover_image: str = None


class GameCreate(GameBase):
    pass


class GameResponse(GameBase):
    id: int

    class Config:
        from_attributes = True


Base.metadata.create_all(bind=engine)


@app.post("/users/", response_model=UserResponse)
def create_user(user: UserCreate):
    db_user = User(**user.dict())
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user


@app.get("/users/", response_model=List[UserResponse])
def read_users(skip: int = 0, limit: int = 100):
    users = session.query(User).offset(skip).limit(limit).all()
    return users


@app.get("/users/{user_id}", response_model=UserResponse)
def read_user(user_id: int):
    user = session.query(User).filter(User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@app.put("/users/{user_id}", response_model=UserResponse)
def update_user(user_id: int, user: UserBase):
    db_user = session.query(User).filter(User.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    for key, value in user.dict().items():
        setattr(db_user, key, value)
    session.commit()
    session.refresh(db_user)
    return db_user


@app.delete("/users/{user_id}", response_model=UserResponse)
def delete_user(user_id: int):
    user = session.query(User).filter(User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    session.delete(user)
    session.commit()
    return user


@app.post("/games/", response_model=GameResponse)
def create_game(game: GameCreate):
    db_game = Game(**game.dict())
    session.add(db_game)
    session.commit()
    session.refresh(db_game)
    return db_game


@app.get("/games/", response_model=List[GameResponse])
def read_games(skip: int = 0, limit: int = 100):
    games = session.query(Game).offset(skip).limit(limit).all()
    return games


@app.get("/games/{game_id}", response_model=GameResponse)
def read_game(game_id: int):
    game = session.query(Game).filter(Game.id == game_id).first()
    if game is None:
        raise HTTPException(status_code=404, detail="Game not found")
    return game


@app.put("/games/{game_id}", response_model=GameResponse)
def update_game(game_id: int, game: GameBase):
    db_game = session.query(Game).filter(Game.id == game_id).first()
    if db_game is None:
        raise HTTPException(status_code=404, detail="Game not found")
    for key, value in game.dict().items():
        setattr(db_game, key, value)
    session.commit()
    session.refresh(db_game)
    return db_game


@app.delete("/games/{game_id}", response_model=GameResponse)
def delete_game(game_id: int):
    game = session.query(Game).filter(Game.id == game_id).first()
    if game is None:
        raise HTTPException(status_code=404, detail="Game not found")
    session.delete(game)
    session.commit()
    return game
