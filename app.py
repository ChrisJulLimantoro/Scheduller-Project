from flask import *
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import *

from algorithm.matkul import *


# initiate app (flask based)
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = getSQLAlchemyURI()


# initiate database connection (using sqlachemy)
db = SQLAlchemy(app)

# initiate migration (using Migrate)
migrate = Migrate(app,db)

# routing and semi-controller
@app.route("/")
def testing():
    return render_template('index.html');

@app.route("/test/",methods = ["POST"])
def api_test():
    data = json.loads(request.data)
    return convertIntToJadwal(int(data['jadwal']),int(data['lama']))


# Model untuk DB & migration
class db_matkul(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64),nullable=False)
    singkatan = db.Column(db.String(10),nullable=False)
    paralel = db.Column(db.String(1),nullable=False)
    dosen = db.Column(db.String(64),nullable=False)
    sks = db.Column(db.Integer,nullable=False)
    jadwal_kuliah = db.Column(db.Integer,nullable=False)
    lama_kuliah = db.Column(db.Integer,nullable=False)
    jadwal_ujian = db.Column(db.Integer,nullable=False)
    lama_ujian = db.Column(db.Integer,nullable=False)