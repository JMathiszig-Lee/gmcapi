
from flask_sqlalchemy import SQLAlchemy
from flask_login import Usermixin

db = SQLAlchemy()

#comments are from the gmc database document
#coloumns in order of gmc register
class Register(db.Model)
    __tablename__ = "register"

    id = db.Column(db.Integer, primary_key=True)
    GMC_no = db.Column(db.Integer, unique=True ) #VARCHAR2 max size 7
    Surname = db.Column(db.string(50)) #varchar2 max 50
    Given Name = db.Column(db.string(50)) #varchar2 max 50
    Gender = db.Column(db.string(1)) # 'M' for man or 'W' for woman
    Qualification = db.Column(db.string(30)) #varchar2 max 30
    Year_qual= db.Column(db.string(4)) #varchar2 max 4
    Place_qual = db.Column(db.string(100)) #varchar2 max 100

    #datestuff will probably need looking at in the future
    pr_date = db.Column(db.Date)) #ddmmyyyy
    fr_date = db.Column(db.Date)) #ddmmyyyy
    sr_date = db.Column(db.Date)) #ddmmyyyy
    gp_date = db.Column(db.Date)) #ddmmyyyy

    reg_status = db.Column(db.string(100)) #varchar2 max 100
    arf_date = db.Column(db.Date)) #ddmmyyyy

    #specialties, might need looking at once we've got actual data
    Specialty1 = db.Column(db.string(100)) #varchar2 max 100
    Sub_Specialty1 = db.Column(db.string(100)) #varchar2 max 100
    Specialty2 = db.Column(db.string(100)) #varchar2 max 100
    Sub_Specialty2 = db.Column(db.string(100)) #varchar2 max 100
    Specialty3 = db.Column(db.string(100)) #varchar2 max 100
    Sub_Specialty3 = db.Column(db.string(100)) #varchar2 max 100
    Specialty4 = db.Column(db.string(100)) #varchar2 max 100
    Sub_Specialty4 = db.Column(db.string(100)) #varchar2 max 100
    Specialty5 = db.Column(db.string(100)) #varchar2 max 100
    Sub_Specialty5 = db.Column(db.string(100)) #varchar2 max 100
    Specialty6 = db.Column(db.string(100)) #varchar2 max 100
    Sub_Specialty6 = db.Column(db.string(100)) #varchar2 max 100
    Specialty7 = db.Column(db.string(100)) #varchar2 max 100
    Sub_Specialty7 = db.Column(db.string(100)) #varchar2 max 100

    ftp_conditions = db.Column(db.Boolean) #varchar2 max 1 y=yes n=no
    ftp_undertakings = db.Column(db.Boolean) #varchar2 max 1 y=yes n=no
    other_names = db.Column(db.string(150)) #varchar2 max 150
    ftp_warnings = db.Column(db.Boolean) #varchar2 max 1 y=yes n=no
    qual_country = db.Column(db.string(100)) #varchar2 max 100

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(60 )    #bcrypt hash
    api_key = db.Column(db.String(64), unique=True, index=True)
    #role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
