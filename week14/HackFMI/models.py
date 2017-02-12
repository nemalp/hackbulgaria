from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
from sqlalchemy import Table, Column, Integer, String, Boolean, ForeignKey
from sqlalchemy import create_engine
from settings import DB_NAME

engine = create_engine(DB_NAME)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

mentor_teams = Table('mentorship', Base.metadata,
                     Column('mentor_id', ForeignKey('mentor.id')),
                     Column('team_id', ForeignKey('team.id')))

team_skills = Table('teamskill', Base.metadata,
                    Column('team_id', ForeignKey('team.id')),
                    Column('technology_id', ForeignKey('skill.id')))


class Team(Base):
    __tablename__ = 'team'

    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    idea_description = Column(String(500))
    repository = Column(String(500))
    need_more_members = Column(Boolean)
    members_needed_desc = Column(String(250))
    room = Column(String(250))
    place = Column(Integer, default=None)
    skill = relationship('Skill', back_populates='team',
                         secondary=team_skills)
    mentor = relationship('Mentor', back_populates='team',
                          secondary=mentor_teams)


class Mentor(Base):
    __tablename__ = 'mentor'

    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    description = Column(String(500))
    picture = Column(String(250))
    team = relationship('Team', secondary=mentor_teams,
                        back_populates='mentor')


class Skill(Base):
    __tablename__ = 'skill'

    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    team = relationship('Team', secondary=team_skills,
                        back_populates='skill')

Base.metadata.create_all(engine)
