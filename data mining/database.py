from sqlalchemy import create_engine #for db connection
from sqlalchemy.orm import sessionmaker # for db opening and closing
from sqlalchemy.orm import declarative_base # for db table
from sqlalchemy import Column # for db columns
from sqlalchemy import Integer,String,Float # for column types

Base = declarative_base()

class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    price = Column(Float)
    discount = Column(Float)
    oprice = Column(Float)
    sold = Column(Integer)
    qty = Column(Integer)

    # to string method
    def __str__(self):
        return self.name
    
# necessary function
def opendb():
    engine = create_engine('sqlite:///data.sqlite')
    return sessionmaker(bind=engine)()

def save_product(db,product):
    db.add(product)
    db.commit()
    db.close()

def get_products(db):
    return db.query(Product).all()
if __name__ == '__main__':
    #create db engine
    engine = create_engine('sqlite:///data.sqlite')
    # create db tables
    Base.metadata.create_all(engine)