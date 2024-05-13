import uuid
from app import Base
#from models.batch import Batch
from models.batch import Batch
import uuid

class ControllerBatch:
    def list(self):
        return Batch.query.all()
    
    def save( self,data):
        batch = Batch()
        print(batch)
        batch.uid = uuid.uuid4()
        print(batch.uid)

        batch.maker = data['maker']
        print(data)
        batch.price_batch = data['price_batch']
        batch.arrive_date= data['arrive_date']
        Base.session.add(batch)
        Base.session.commit()
        return batch.id