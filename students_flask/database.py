from typing import Optional
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import String
from sqlalchemy import Integer
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy import select


class Base(DeclarativeBase):
    pass


class Address(Base):
    __tablename__ = "address"
    id: Mapped[int] = mapped_column(primary_key=True)
    street: Mapped[str] = mapped_column(String(50))
    number: Mapped[int]
    flat: Mapped[Optional[int]]

    def __repr__(self):
        return f"{self.street} - {self.number}"

engine = create_engine("postgresql+psycopg2://postgres:postgres@localhost:5432/alchemy", echo=True)
Base.metadata.create_all(engine)

with Session(engine) as session_1:
    home = Address(
        street="Chuy",
        number=363,
    )

    work = Address(
        street="7 mkrn",
        number=26,
        flat=3
    )
    session_1.add_all([home, work])
    session_1.commit()

session_2 = Session(engine)
stmt = select(Address).where(Address.street.in_(["Chuy", "7 mkrn"]))

for address_record in session_2.scalars(stmt):
    print(address_record)
