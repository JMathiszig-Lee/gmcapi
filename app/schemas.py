from flask_marshmallow import MarshMallow
from models import Register

ma = Marshmallow()

class RegisterSchema(ma.ModelSchema):
    class Meta:
        model = Register

register_schema = PuppySchema()
