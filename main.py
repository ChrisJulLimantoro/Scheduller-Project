from flask import *
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import *
from api.tes import *
from algorithm.matkul import *
from commands import import_data_command
from wtforms import Form, StringField, validators, DateTimeField, PasswordField, BooleanField, SelectField, IntegerField
# from wtforms.fields import html5 as h5fields
# from wtforms.widgets import html5 as h5widgets
# from wtforms.widgets import TextArea

# initiate app (flask based)
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = getSQLAlchemyURI()
# app.debug = True
# toolbar = DebugToolbarExtension(app)

# Register the custom command
app.cli.add_command(import_data_command)

# initiate database connection (using sqlachemy)
db = SQLAlchemy(app)

# initiate migration (using Migrate)
migrate = Migrate(app,db)

# routing and semi-controller
@app.route("/")
def testing():
    # form = InsertForm(request.form)
    return render_template('pilihJadwal.html', form=InsertForm());

@app.route("/insert/",methods = ["POST"])
# api buat insert mata kuliah ke DB
def insert():
    form = InsertForm(request.form)
    if form.validate():
        return insert_matkul(request.form)

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
    data = json.loads(request.get_data())
    return generate(data['active'],data['filter'],3)

@app.route("/upload/",methods=["POST"])
# api buat upload
def upload():
    data = request.files['file']
    return upload_matkul(data)
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

class InsertForm(Form) :
    nama = StringField('Nama Mata Kuliah', validators=[validators.InputRequired(), validators.length(max=100)])
    sing = StringField("Nama Singkatan", validators=[validators.InputRequired(), validators.length(max=100)])
    par = StringField("Kelas Paralel", validators=[validators.InputRequired(), validators.length(max=100)])
    dos = StringField("Nama Dosen", validators=[validators.InputRequired(), validators.length(max=100)])
    rua = StringField("Ruangan", validators=[validators.InputRequired(), validators.length(max=100)])

    hari_kuliah = SelectField(
        "Hari Kuliah", 
        validators=[validators.InputRequired(), validators.NumberRange(min=1, max=6)],
        choices=[(1, 'Senin'), (2, 'Selasa'), (3, 'Rabu'), (4, 'Kamis'), (5, 'Jumat'), (6, 'Sabtu')]
    )
    jam_mulai = SelectField(
        'Jam Mulai', 
        validators=[validators.InputRequired(), validators.NumberRange(min=7, max=20)],
        choices=[(7, '07'), (8, '08'), (9, '09'), (10, '10'), (11, '11'), (12, '12'), (13, '13'), (14, '14'), (15, '15'), (16, '16'), (17, '17'), (18, '18'), (19, '19'), (20, '20')]
    )
    menit_mulai = SelectField(
        'Menit Mulai', 
        validators=[validators.InputRequired(), validators.AnyOf([0, 30])],
        choices=[(0, '00'), (30, '30')]
    )
    jam_selesai = SelectField(
        'Jam Selesai', 
        validators=[validators.InputRequired(), validators.NumberRange(min=7, max=20)],
        choices=[(7, '07'), (8, '08'), (9, '09'), (10, '10'), (11, '11'), (12, '12'), (13, '13'), (14, '14'), (15, '15'), (16, '16'), (17, '17'), (18, '18'), (19, '19'), (20, '20')]
    )
    menit_selesai = SelectField(
        'Menit Selesai', 
        validators=[validators.InputRequired(), validators.AnyOf([0, 30])],
        choices=[(0, '00'), (30, '30')]
    )

    minggu_ujian = SelectField(
        'Minggu Ujian', 
        validators=[validators.InputRequired(), validators.NumberRange(min=1, max=2)],
        choices=[(1, 'Minggu ke-1'), (2, 'Minggu ke-2')]
    )
    hari_ujian = SelectField(
        "Hari Ujian", 
        validators=[validators.InputRequired(), validators.NumberRange(min=1, max=6)],
        choices=[(1, 'Senin'), (2, 'Selasa'), (3, 'Rabu'), (4, 'Kamis'), (5, 'Jumat'), (6, 'Sabtu')]
    )
    jam_mulai_ujian = SelectField(
        'Jam Mulai', 
        validators=[validators.InputRequired(), validators.NumberRange(min=7, max=20)],
        choices=[(7, '07'), (8, '08'), (9, '09'), (10, '10'), (11, '11'), (12, '12'), (13, '13'), (14, '14'), (15, '15'), (16, '16'), (17, '17'), (18, '18'), (19, '19'), (20, '20')]
    )
    menit_mulai_ujian = SelectField(
        'Menit Mulai', 
        validators=[validators.InputRequired(), validators.AnyOf([0, 30])],
        choices=[(0, '00'), (30, '30')]
    )
    jam_selesai_ujian = SelectField(
        'Jam Selesai', 
        validators=[validators.InputRequired(), validators.NumberRange(min=7, max=20)],
        choices=[(7, '07'), (8, '08'), (9, '09'), (10, '10'), (11, '11'), (12, '12'), (13, '13'), (14, '14'), (15, '15'), (16, '16'), (17, '17'), (18, '18'), (19, '19'), (20, '20')]
    )
    menit_selesai_ujian = SelectField(
        'Menit Selesai', 
        validators=[validators.InputRequired(), validators.AnyOf([0, 30])],
        choices=[(0, '00'), (30, '30')]
    )

    sks = IntegerField('Jumlah SKS', validators=[validators.InputRequired()])