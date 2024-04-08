from marshmallow import Schema, fields


class TemperatureSchema(Schema):
    id = fields.Integer(dump_only=True)
    temperature = fields.Decimal(required=True)
    datetime = fields.DateTime()
    city_id = fields.Integer(required=True)
