
from app import Base

from models.person import Person
from models.account import Account
from flask import current_app
import uuid
from controllers.utils import verification
import jwt
from datetime import datetime, timedelta
import bcrypt
from .controller_product import ControllerProduct



class ControllerAccount:
    def list(self):
        return Account.query.all()
    
    def hash_password(self, password):
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        return hashed_password
    
    def save_account_person(self, data):
        account = Account.query.filter_by(email=data["email"]).first()
        if account:
            return -2
        else:
            if verification.validate_email(data["email"]):
                # Crear la persona primero 
                person = Person(
                    last_name=data['last_name'],
                    name=data['name'],
                    dni=data['dni'],
                    uid=uuid.uuid4()
                )
                Base.session.add(person)
                Base.session.flush()  # GENERA EL ID
                
                # Crear la cuenta y asignar el ID de la pesrsona
                account = Account(
                    email=data['email'],
                    password=self.hash_password(data['password']),
                    status= True,
                    uid=uuid.uuid4(),
                    person_id=person.id  
                )
                
                Base.session.add(account)
                Base.session.commit()
                
                return account.id
            else:
                return -1
            
            
    def login(self, data):
        cuentaA = Account.query.filter_by(email=data["email"]).first()
        if cuentaA:
            # Verificar la contraseña
            if bcrypt.checkpw(data["password"].encode('utf-8'), cuentaA.password.encode('utf-8')):

                token = jwt.encode(
                    {
                        "uid": cuentaA.uid,
                        "exp": datetime.utcnow() + timedelta(minutes= 60)
                    },
                    key=current_app.config["SECRET_KEY"],
                    algorithm="HS512"
                )

                persona = Person.query.filter_by(id= cuentaA.person_id).first()
          

                info = {
                    "token": token,
                    "user":  persona.last_name + "   "+  persona.name,
                    "exp": datetime.now() + timedelta(days = 60),
                    "uid": cuentaA.uid
                }
                #SE ACTUALIZAN LOS ESTADOS CADA QUE EL USUARIO INICIA SESION
                controller_product = ControllerProduct()
                controller_product.updates_status()
                return info
            else:
                return -13  # Contraseña incorrecta
        else:
            return -7  # Usuario no encontrado
            
        

        
