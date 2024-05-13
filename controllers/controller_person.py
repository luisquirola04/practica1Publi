from flask import current_app
from models.person import Person
from models.account import Account
from utils.verification import validate_email

import uuid
from app import Base
import jwt
from datetime import datetime, timedelta

class ControllerPerson:

    def list(self):
        return Person.query.all()
    #SE REALIZARA EN CASO DE SER NECESARIO FACTURAR
    '''
    def savePerson(self,data):
        person = Person()
        account = Account.query.filter_by(correo=data["correo"]).first()
        if account:
                return -2
        else:
            if validate_email(data["correo"]):
                person.lastName = data['last_name'] #parte izquierda viene de la bd y apellidos viene del frontend del usuario
                person.name = data['name']
                person.dni = data['dni']
                person.uid = uuid.uuid4()
                
                Base.session.add(person)
                Base.session.commit()
                #cuenta
                return person.id
                    # Resto de tu lógica para guardar la persona y la cuenta

            else:
                return -1
    '''