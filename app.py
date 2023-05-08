from flask import *
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# initiate app (flask based)
app = Flask(__name__)
# URI depends on [engine]://[username]:[password]@[localhost]/[database]
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Aklsa!23#21@localhost/scheduller_kb'

# initiate database connection (using sqlachemy)
db = SQLAlchemy(app)

# initiate migration (using Migrate)
migrate = Migrate(app,db)

# routing and semi-controller
@app.route("/")
def testing():
    return "<h1>hallo ngabb!</h1>"


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