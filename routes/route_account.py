from flask import Blueprint, jsonify, make_response, request
from controllers.utils.errors import Errors
from flask_expects_json import expects_json
from controllers.utils.errors import Errors
from controllers.controller_account import ControllerAccount
from .schemas.schemas_account import schema_save_account, schema_sesion

url_account = Blueprint('url_account', __name__)


accountC = ControllerAccount()

@url_account.route('/account/list')
def listBatch():
    return make_response(
        jsonify({"msg" : "OK", "code" : 200, "datos" : ([i.serialize for i in accountC.list()])}), 

        200
    )

@url_account.route('/account/save', methods = ["POST"])
@expects_json(schema_save_account)
def save_batch():
    data = request.json  
    c = accountC.save_account_person(data)  
    if c >= 0:
        return make_response(
            jsonify({"msg": "OK", "code": 200, "datos": {"tag": "datos guardados"}}),
            200
        )
    else:
        return make_response(
            jsonify({"msg": "ERROR", "code": 400, "datos": {"error": Errors.error.get(str(c))}}),
            400
        )

@url_account.route('/sesion', methods = ["POST"])
@expects_json(schema_sesion)
def sesion():
    data = request.json  
    id = accountC.login(data = data)
    print("el id es : " +str(id)) #esto no va solo es para ver errores el trazado
    if type(id) == int:
        return make_response(
                jsonify({"msg" : "ERROR", "code" : 400, "datos" :{"error" : Errors.error[str(id)]}}), 
                400
        )
    else:
        return make_response(
                jsonify({"msg" : "OK", "code" : 200, "datos" : id}), 
                200
    )