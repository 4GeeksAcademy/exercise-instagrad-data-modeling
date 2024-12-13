import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    # Definición de columnas para la tabla 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    firstname = Column(String(250), nullable=False)
    lastname = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)

class Post(Base):
    __tablename__ = 'post'
    # Definición de columnas para la tabla 'post'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

class Media(Base):
    __tablename__ = 'media'
    # Definición de columnas para la tabla 'media'
    id = Column(Integer, primary_key=True)
    type = Column(String(250), nullable=False)
    url = Column(String(250), nullable=False)
    post_id = Column(Integer, ForeignKey('post.id'))
    post = relationship(Post)

class Comment(Base):
    __tablename__ = 'comment'
    # Definición de columnas para la tabla 'comment'
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(250), nullable=False)
    author_id = Column(Integer, ForeignKey('user.id'))
    post_id = Column(Integer, ForeignKey('post.id'))
    author = relationship(User)
    post = relationship(Post)

class Like(Base):
     __tablename__ = 'like'
    
     id = Column(Integer, primary_key=True)
     author_id = Column(Integer, ForeignKey('user.id'))
     post_id = Column(Integer, ForeignKey('post.id'))
     like = relationship (User , Post)

class Follow(Base):
     __tablename__ = 'follow'
     id = Column(Integer, primary_key=True)
     user_from_id = Column(Integer, ForeignKey('user.id'))
     user_to_id = Column(Integer, ForeignKey('user.id'))
     Follow = relationship(User)
    

class Safe(Base):
     __tablename__ = 'safe'
     id = Column(Integer, primary_key=True)
     
     
     
     
     
     
     def to_dict(self):
        return {}

# Generación del diagrama
try:
    result = render_er(Base, 'diagram.png')
    print("¡Éxito! Revisa el archivo diagram.png")
except Exception as e:
    print("Hubo un problema generando el diagrama.")
    raise e