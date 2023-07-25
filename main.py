from flask import *
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import *
from api.tes import *
import algorithm.matkul as matkul
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
    mulai_kuliah = matkul.convertJadwalToInt(int(form.hari_kuliah.data), int(form.jam_mulai.data), int(form.menit_mulai.data))
    selesai_kuliah = matkul.convertJadwalToInt(int(form.hari_kuliah.data), int(form.jam_selesai.data), int(form.menit_selesai.data))
    mulai_ujian = matkul.convertJadwalToInt(int(form.hari_ujian.data), int(form.jam_mulai_ujian.data), int(form.menit_mulai_ujian.data), int(form.minggu_ujian.data))
    selesai_ujian = matkul.convertJadwalToInt(int(form.hari_ujian.data), int(form.jam_selesai_ujian.data), int(form.menit_selesai_ujian.data), int(form.minggu_ujian.data))

    if form.validate() and (selesai_kuliah > mulai_kuliah) and (selesai_ujian > mulai_ujian):
        return insert_matkul(request.form)
    
    return "0"

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
    nama = StringField('Nama Mata Kuliah', validators=[validators.InputRequired(), validators.length(max=64)])
    sing = StringField("Nama Singkatan", validators=[validators.InputRequired(), validators.length(max=10)])
    par = StringField("Kelas Paralel", validators=[validators.InputRequired(), validators.length(max=1)])
    dos = StringField("Nama Dosen", validators=[validators.InputRequired(), validators.length(max=64)])
    rua = StringField("Ruangan", validators=[validators.InputRequired(), validators.length(max=25)])

    hari_kuliah = SelectField(
        "Hari Kuliah", 
        validators=[validators.InputRequired(), validators.NumberRange(min=0, max=5)],
        choices=[(0, 'Senin'), (1, 'Selasa'), (2, 'Rabu'), (3, 'Kamis'), (4, 'Jumat'), (5, 'Sabtu')],
        coerce=int
    )
    jam_mulai = SelectField(
        'Jam Mulai', 
        validators=[validators.InputRequired(), validators.NumberRange(min=7, max=20)],
        choices=[(7, '07'), (8, '08'), (9, '09'), (10, '10'), (11, '11'), (12, '12'), (13, '13'), (14, '14'), (15, '15'), (16, '16'), (17, '17'), (18, '18'), (19, '19'), (20, '20')],
        coerce=int
    )
    menit_mulai = SelectField(
        'Menit Mulai', 
        validators=[validators.InputRequired(), validators.AnyOf([0, 30])],
        choices=[(0, '00'), (30, '30')],
        coerce=int
    )
    jam_selesai = SelectField(
        'Jam Selesai', 
        validators=[validators.InputRequired(), validators.NumberRange(min=7, max=20)],
        choices=[(7, '07'), (8, '08'), (9, '09'), (10, '10'), (11, '11'), (12, '12'), (13, '13'), (14, '14'), (15, '15'), (16, '16'), (17, '17'), (18, '18'), (19, '19'), (20, '20')],
        coerce=int
    )
    menit_selesai = SelectField(
        'Menit Selesai', 
        validators=[validators.InputRequired(), validators.AnyOf([0, 30])],
        choices=[(0, '00'), (30, '30')],
        coerce=int
    )

    minggu_ujian = SelectField(
        'Minggu Ujian', 
        validators=[validators.InputRequired(), validators.NumberRange(min=0, max=1)],
        choices=[(0, 'Minggu ke-1'), (1, 'Minggu ke-2')],
        coerce=int
    )
    hari_ujian = SelectField(
        "Hari Ujian", 
        validators=[validators.InputRequired(), validators.NumberRange(min=0, max=5)],
        choices=[(0, 'Senin'), (1, 'Selasa'), (2, 'Rabu'), (3, 'Kamis'), (4, 'Jumat'), (5, 'Sabtu')],
        coerce=int
    )
    jam_mulai_ujian = SelectField(
        'Jam Mulai', 
        validators=[validators.InputRequired(), validators.NumberRange(min=7, max=20)],
        choices=[(7, '07'), (8, '08'), (9, '09'), (10, '10'), (11, '11'), (12, '12'), (13, '13'), (14, '14'), (15, '15'), (16, '16'), (17, '17'), (18, '18'), (19, '19'), (20, '20')],
        coerce=int
    )
    menit_mulai_ujian = SelectField(
        'Menit Mulai', 
        validators=[validators.InputRequired(), validators.AnyOf([0, 30])],
        choices=[(0, '00'), (30, '30')],
        coerce=int
    )
    jam_selesai_ujian = SelectField(
        'Jam Selesai', 
        validators=[validators.InputRequired(), validators.NumberRange(min=7, max=20)],
        choices=[(7, '07'), (8, '08'), (9, '09'), (10, '10'), (11, '11'), (12, '12'), (13, '13'), (14, '14'), (15, '15'), (16, '16'), (17, '17'), (18, '18'), (19, '19'), (20, '20')],
        coerce=int
    )
    menit_selesai_ujian = SelectField(
        'Menit Selesai', 
        validators=[validators.InputRequired(), validators.AnyOf([0, 30])],
        choices=[(0, '00'), (30, '30')],
        coerce=int
    )

    sks = IntegerField('Jumlah SKS', validators=[validators.InputRequired(), validators.NumberRange(min=1)])