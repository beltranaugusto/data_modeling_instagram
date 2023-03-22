import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)

class Follower(Base):
    __tablename__ = 'follower'
    id = Column(Integer, primary_key=True)
    follower_id = Column(Integer, ForeignKey("user.id"))
    followed_id = Column(Integer, ForeignKey("user.id"))

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    author = Column(Integer, ForeignKey("user.id"))
    description = Column(String(500), nullable=True)

class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    comment_author = Column(Integer, ForeignKey("user.id"))
    post = Column(Integer, ForeignKey("post.id"))
    content = Column(String(500), nullable=False)

class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)
    post = Column(Integer, ForeignKey("post.id"))
    url = Column(String(250), nullable=False)

    



## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
