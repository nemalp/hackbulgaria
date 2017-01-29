import smtplib
from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy import Column, Integer, String, Float
from sqlalchemy import create_engine
from time import time
# from sqlalchemy import import ForeignKey
from sqlalchemy.orm import sessionmaker
from helpers.hash_password import hash_password, check_password
from models import Client, BannedClient


class QueryController:

    def __init__(self):
        self.base = declarative_base()
        self.engine = create_engine('sqlite:///bank.db')
        self.session = sessionmaker(bind=self.engine)()

    def change_pass(self, new_pass, logged_user):
        logged_user.password = hash_password(new_pass)
        self.session.commit()

    def register(self, username, password, email):
        hashed_password = hash_password(password)
        self.session.add(Client(username=username, password=hashed_password,
                                email='email',
                                balance=0))
        self.session.commit()

    def login(self, username, password):
        user = self.session.query(Client).filter_by(
            username=username).one()

        if check_password(user.password, password):
            return user

    def ban_client(self, username):
        ban_time = time() + 300
        self.session.add(BannedClient(username=username, ban_time=ban_time))
        self.session.commit()

    def is_banned(self, username):
        try:
            user = self.session.query(BannedClient).filter_by(
                username=username).one()

            if user:
                return user
        except:
            return False

    def remove_ban(self, username):
        user = self.session.query(BannedClient).filter_by(username=username)[0]
        self.session.delete(user)
        self.session.commit()

    def select_client(self, username):
        client = self.session.query(Client).filter_by(username=username).one()
        return client

    def send_reset_password_email(self, from_, to, password):
        try:
            content = 'Test email'
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.ehlo()
            server.starttls()
            server.login(from_, password)
            server.sendmail(from_, to, content)
            server.close()
        except:
            print('This functionality is still in beta.' +
                  'It is possible to experience some outages')


'''
q = QueryController()
q.register('Foo', '1234', 'email')
q.register('Bar', '1234', 'email')
q.ban_client('Bar')
print(q.is_banned('Bar'))
q.remove_ban('Bar')
print(q.is_banned('Bar'))
q.login('Foo', '1234')
'''
