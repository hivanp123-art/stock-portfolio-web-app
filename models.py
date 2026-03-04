from sqlalchemy import Column, Integer, String, ForeignKey, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
import enum

Base = declarative_base()

class AlertType(enum.Enum):
    EMAIL = 'email'
    SMS = 'sms'
    PUSH_NOTIFICATION = 'push_notification'

class SignalStrength(enum.Enum):
    WEAK = 'weak'
    MODERATE = 'moderate'
    STRONG = 'strong'

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    portfolios = relationship('Portfolio', back_populates='owner')

class Portfolio(Base):
    __tablename__ = 'portfolios'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    owner = relationship('User', back_populates='portfolios')
    stocks = relationship('Stock', back_populates='portfolio')

class Stock(Base):
    __tablename__ = 'stocks'
    id = Column(Integer, primary_key=True)
    symbol = Column(String, unique=True, nullable=False)
    portfolio_id = Column(Integer, ForeignKey('portfolios.id'))
    portfolio = relationship('Portfolio', back_populates='stocks')

class Signal(Base):
    __tablename__ = 'signals'
    id = Column(Integer, primary_key=True)
    stock_id = Column(Integer, ForeignKey('stocks.id'))
    strength = Column(Enum(SignalStrength), nullable=False)
    stock = relationship('Stock')

class Alert(Base):
    __tablename__ = 'alerts'
    id = Column(Integer, primary_key=True)
    signal_id = Column(Integer, ForeignKey('signals.id'))
    type = Column(Enum(AlertType), nullable=False)
    signal = relationship('Signal')

