#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey, Float, Integer, Table
from sqlalchemy.orm import relationship
from os import getenv
from models.review import Review
from models.amenity import Amenity


place_amenity = Table("place_amenity", Base.metadata, 
                      Column("place_id", String(60),
                             ForeignKey("places.id"),
                             nullable=False),
                      Column("amenity_id", String(60),
                             ForeignKey("amenities.id"), nullable=False))

class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []

    if (getenv('HBNB_TYPE_STORAGE') == 'db'):
        reviews = relationship("Review", backref="place", cascade="all, delete")
        amenities = relationship("Amenity", secondary=place_amenity, viewonly=False)

    else:
        @property
        def reviews(self):
            from models import storage
            to_return = []
            for review in storage.all(Review):
                if review.place_id == self.id:
                    to_return.append(review)
            return to_return
    

        @property
        def amenities(self):
            from models import storage
            to_return = []
            for amenity in storage.all(Amenity).values():
                if amenity.id in self.amenity_ids:
                    to_return.append(amenity)
            return to_return


        @amenities.setter
        def amenities(self, obj):
            if type(obj) == Amenity:
                self.amenity_ids.append(obj.id)