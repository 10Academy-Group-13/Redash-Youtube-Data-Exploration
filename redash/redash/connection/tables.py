from sqlalchemy import create_engine, Column, Integer, String, Float, Date
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from postgres_conn import ConnectToPostgres
from datetime import datetime

Base = declarative_base()

class CityChart(Base):
    
    __tablename__ = 'city_chart'
    date = Column('date', datetime)
    city_id = Column('city_id',String,primary_id=True)
    city_name = Column('city_name', String)
    Views = Column('Views',Integer)

    def __init__(self,date,city_id,city_name,Views):
      self.date = date
      self.city_id = city_id
      self.city_name = city_name
      self.Views = Views
      
class Content_type_info(Base):
    __tablename__ = "content_type_info"

    id = Column("id", Integer, primary_key=True)
    content_type = Column("content_type", String)
    watch_time = Column("watch_time_in_hours", Integer)
    average_time_duration = Column("average_time_duration", String)

    def __init__(self, id, content_type, watch_time, average_time_duration):
        id = self.id
        self.content_type = content_type
        self.watch_time = watch_time
        self.average_time_duration = average_time_duration

class Content_type_chart(Base):
    __tablename__ = "content_type_chart"

    id = Column("id", Integer, primary_key=True)
    date = Column("date", Date)
    views = Column("views", Integer)
    content_types = Column(Integer, ForeignKey("content_type_info.id"))

    def __init__(self, id, date, view, content_types):
        self.id = id
        self.date  = date
        self.view = view
        self.content_types = content_types

class Device_type_info(Base):
    __tablename__ = "device_type_info"

    id = Column("id", Integer, primary_key=True)
    device_type = Column("device_type", String)
    watch_time = Column("watch_time_in_hours", Integer)
    average_time_duration = Column("average_time_duration", String)

    def __init__(self, id, content_type, watch_time, average_time_duration):
        id = self.id
        self.device_type = device_type
        self.watch_time = watch_time
        self.average_time_duration = average_time_duration
class Device_type_chart(Base):
    __tablename__ = "device_type_chart"

    id = Column("id", Integer, primary_key=True)
    date = Column("date", Date)
    views = Column("views", Integer)
    device_types = Column(Integer, ForeignKey("device_type_info.id"))

    def __init__(self, id, date, view, content_types):
        self.id = id
        self.date  = date
        self.view = view
        self.device_types = device_types

conn = ConnectToPostgres()
engine = conn.get_engine()
Base.metadata.create_all(bind=engine, checkfirst=True)