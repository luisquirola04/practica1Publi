from flask import Blueprint, jsonify, make_response, request
from controllers.utils.errors import Errors
from flask_expects_json import expects_json
from controllers.utils.errors import Errors
from controllers.controller_batch import ControllerBatch
from .schemas.schemas_batch import schema_save_batch
from controllers.authenticate import token_required


url_batch = Blueprint('url_batch', __name__)


batchC = ControllerBatch()

@url_batch.route('/batch/list')
@token_required
def listBatch():
    return make_response(
        jsonify({"msg" : "OK", "code" : 200, "datos" : ([i.serialize for i in batchC.list()])}), 

        200
    )

@url_batch.route('/batch/save', methods = ["POST"])
@expects_json(schema_save_batch)
@token_required
def save_batch():
    data = request.json  
    c = batchC.save(data)  
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

