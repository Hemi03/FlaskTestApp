from json import dumps

from sqlalchemy import Column, Integer, String

from ..db_Model import DB


class Names(DB.Model):
    Name = Column(String, primary_key=True)
    Address = Column(String, nullable=False)

    def toJson(self):
        return dumps((self.Name, self.Address))

    def delete(self):
        DB.session.delete(self)
        DB.session.commit()

    def commit(self):
        DB.session.commit()

    @classmethod
    def new_Names(cli, name: str, address: str):
        output = cli(Name=name, Address=address)
        DB.session.add(output)
        DB.session.commit()
        return new


class Event(DB.Model):
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
