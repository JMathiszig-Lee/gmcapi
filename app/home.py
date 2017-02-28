from flask import Flask, jsonify
from flask_login import LoginManager, login_required
from models import db, Register
from schemas import ma, register_schema

login_manager = LoginManager()

app = Flask(__name__)
db.init_app(app)
ma.init_app(app)



@app.route('/')
def index():
    return '<h1>Welcome to the open GMC API</h1>'

@app.route('/api/v0.1/<int:gmc>', methods=['GET'])
def get_gmc(gmc):
    reg = Register.query.filter(Register.GMC_no==gmc).first_or_404()
    return register_schema(reg)


if __name__ == '__main__':
    app.run(debug=True)
