from sqlalchemy import DateTime,Integer,String,Text, ForeignKey
from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column,relationship
from database import Base
class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True,index=True)
    username: Mapped[str] = mapped_column(String(50),unique=True,nullable=False)
    email: Mapped[str] = mapped_column(String(150),unique=True,nullable=False)
    image_file: Mapped[str | None] = mapped_column(
        String(200),
        nullable=True,
        default=None
    )
    events: Mapped[list["Event"]] = relationship(back_populates="organizer")

class Event(Base):
    __tablename__ = "events"

    id: Mapped[int] = mapped_column(Integer, primary_key=True,index=True)
    # foreign keys
    organizer_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"),index=True)
    venue_id: Mapped[int] = mapped_column(Integer, ForeignKey("venues.id"),index=True)
    title: Mapped[str] = mapped_column(String(50),unique=False,nullable=False)
    description: Mapped[str] = mapped_column(String(250),unique=False,nullable=False)
    start_date: Mapped[datetime] = mapped_column(DateTime(timezone=True),nullable=False)
    end_date: Mapped[datetime] = mapped_column(DateTime(timezone=True),nullable=False)
    image_file: Mapped[str | None] = mapped_column(
            String(200),
            nullable=True,
            default=None
        )

    organizer: Mapped["User"] = relationship(back_populates="events")
    venue: Mapped["Venue"] = relationship( 
        back_populates="events"
    )
    ticket_types: Mapped[list["TicketType"]] = relationship(
    back_populates="event"
)

class Venue(Base):
    __tablename__="venues"
    id: Mapped[int] = mapped_column(Integer, primary_key=True,index=True)
    name: Mapped[str] = mapped_column(String(50),unique=False,nullable=False)
    location: Mapped[str] = mapped_column(String(50),unique=False,nullable=False)
    capacity: Mapped[int] = mapped_column(Integer,nullable=False)

    events: Mapped[list["Event"]]=relationship(
        back_populates="venue"
    )

class TicketType(Base):
    __tablename__="ticket_types"
    id: Mapped[int] = mapped_column(Integer, primary_key=True,index=True)
    name: Mapped[str] = mapped_column(String(50),unique=False,nullable=False)
    price: Mapped[int] = mapped_column(Integer, nullable=False)
    quantity: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str |None] = mapped_column(Text, nullable=True)
    event_id : Mapped[int] = mapped_column(Integer,ForeignKey("events.id"),nullable=False)
    event: Mapped["Event"] = relationship(
        back_populates="ticket_types"
    )
    