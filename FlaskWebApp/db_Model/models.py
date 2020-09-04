from json import dumps

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from ..db_Model import DB


class Names(DB.Model):
    """Name Database Table
    """
    Name = Column(String(50), primary_key=True)
    Event_ID = Column(String, nullable=False)
    event = relationship("event", back_populates="namesUsed")

    def toJson(self):
        """return the Object in Json Format {"Name": name, "Event": event}

        Returns:
            dict: the Name Object as a Dictionary
        """
        return {"Name": self.Name, "Event": self.Event}

    def delete(self):
        """delete yourself from the Database
        """
        DB.session.delete(self)
        DB.session.commit()

    def commit(self):
        """commit a change to the Database
        """
        DB.session.commit()

    @classmethod
    def new_Names(cli, name: str, event: str):
        """create a new Name and add it to the Database

        Args:
            name (str): the Name of the new Object
            event (str): The Event of the new Object

        Returns:
            Name: the just created Name Object
        """
        new = cli(Name=name, Event=event)
        DB.session.add(new)
        DB.session.commit()
        return new


class Event(DB.Model):
    """Event Database Table
    """
    Name = Column(String(25), primary_key=True)
    Theme = Column(String(25), ForeignKey(Names.Name), nullable=False)
    namesUsed = relationship(Names, back_populates=Names.event)

    def toJson(self):
        return {"Event": self.Name, "Theme": self.Theme}

    def delete(self):
        DB.session.delete(self)
        DB.session.commit()

    def commit(self):
        DB.session.commit()

    @classmethod
    def new_Event(cli, name: str, theme: str):
        new = cli(Name=name, Theme=theme)
        DB.session.add(new)
        DB.session.commit()
        return new
