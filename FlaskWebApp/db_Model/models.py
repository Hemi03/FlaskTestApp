from json import dumps

from sqlalchemy import Column, Integer, String

from ..db_Model import DB


class Names(DB.Model):
    """Name Database Table
    """
    Name = Column(String(50), primary_key=True)
    Address = Column(String, nullable=False)

    def toJson(self):
        """return the Object in Json Format {"Name": name, "Address": address}

        Returns:
            dict: the Name Object as a Dictionary
        """
        return {"Name": self.Name, "Address": self.Address}

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
    def new_Names(cli, name: str, address: str):
        """create a new Name and add it to the Database

        Args:
            name (str): the Name of the new Object
            address (str): The Address of the new Object

        Returns:
            Name: the just created Name Object
        """
        new = cli(Name=name, Address=address)
        DB.session.add(new)
        DB.session.commit()
        return new


class Event(DB.Model):
    """Event Database Table
    """
    Name = Column(String(25), primary_key=True)
    Theme = Column(String(25), nullable=False)

    def toJson(self):
        return {"Name": self.Name, "Theme": self.Theme}

    def delete(self):
        DB.session.delete(self)
        DB.session.commit()

    @classmethod
    def new_Event(cli, name: str, theme: str):
        new = cli(Name=name, Theme=theme)
        DB.session.add(new)
        DB.session.commit()
        return new
