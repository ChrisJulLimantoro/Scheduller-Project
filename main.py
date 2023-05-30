from flask import *
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import *
from flask import *
from api.tes import *
from algorithm.matkul import *

# initiate app (flask based)
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = getSQLAlchemyURI()


# initiate database connection (using sqlachemy)
db = SQLAlchemy(app)

# initiate migration (using Migrate)
migrate = Migrate(app,db)

@app.route("/")
def home():
    return "<h1>CO membosankan</h1>"

# routing and semi-controller
@app.route("/pilihJadwal")
def testing():
    return render_template('pilihJadwal.html');

@app.route("/test/",methods = ["POST"])
def api_test():
    data = json.loads(request.data)
    
    return convertIntToJadwal(int(data['jadwal']),int(data['lama']))

@app.route("/insert/",methods = ["POST"])
# api buat insert mata kuliah ke DB
def insert():
    data = json.loads(request.data)
    return insert_matkul(data)

@app.route("/get_dosen/",methods =["POST"])
# api buat get_dosen
def get():
    return get_dosen()

@app.route("/get_matkul/",methods =["POST"])
# api buat get_matkul
def get_mat():
    return get_matkul()

@app.route("/get/",methods=["POST"])
# api buat get_jadwal
def get_jad():
    return get_jadwal()

@app.route("/generate/",methods=["POST"])
# api buat generate
def gener():
    return request.data
    data = json.loads(request.data)
    return generate(data['active'],data['filter'],3)

@app.route("/load")
def load():
    return render_template('loader.html')

# Model untuk DB & migration


class db_matkul(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64),nullable=False)
    singkatan = db.Column(db.String(10),nullable=False)
    paralel = db.Column(db.String(1),nullable=False)
    dosen = db.Column(db.String(64),nullable=False)
    ruangan = db.Column(db.String(25),nullable=False)
    jadwal_kuliah = db.Column(db.Integer,nullable=False)
    lama_kuliah = db.Column(db.Integer,nullable=False)
    jadwal_ujian = db.Column(db.Integer,nullable=False)
    sks = db.Column(db.Integer,nullable=False)