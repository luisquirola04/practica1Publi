from app import create_app
from datetime import datetime
from datetime import timedelta
app = create_app()
timeplas=timedelta(minutes=60)
#expiration_time = datetime.utcnow() + timedelta(minutes=60)  # Calcula el tiempo de expiración
now= datetime.now()+timeplas
print("la hora es",now)
print()
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")