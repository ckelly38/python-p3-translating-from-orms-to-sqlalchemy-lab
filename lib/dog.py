from models import Dog
from sqlalchemy.orm import sessionmaker

def create_table(base, engine):
    base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session();
    return session;

def save(session, dog):
    session.add(dog);
    session.commit();
    return session;

def get_all(session):
    return session.query(Dog).all();

def find_by_name(session, name):
    return session.query(Dog).filter(Dog.name == name).first();
    #filter works exactly like in javascript so it returns a list,
    #then we need to get the first item from it

def find_by_id(session, id):
    return session.query(Dog).filter(Dog.id == id).first();

def find_by_name_and_breed(session, name, breed):
    return session.query(Dog).filter(Dog.name == name, Dog.breed == breed).first();

def update_breed(session, dog, breed):
    #session.query(Dog).update({dog.breed: breed});#updates all of them not just one...
    dog.breed = breed;
    session.add(dog);#no idea why we have to do it this way...
    session.commit();
    return session;#not sure if we even need a return value here...