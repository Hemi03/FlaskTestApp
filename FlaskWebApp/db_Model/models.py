from sqlalchemy import Column, Integer, String

from ..db_Model import DB


class Names(DB.Model):
    Name = Column(String, primary_key=True)
    Address = Column(String, nullable=False)

    @classmethod
    def new_Names(cli, name: str, address: str):
        output = cli(Name=name, Address=address)
        DB.session.add(output)
        DB.session.commit()
        return output
