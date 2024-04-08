from marshmallow import Schema, fields


class CitySchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String(required=True)
    additional_info = fields.String(required=True)
