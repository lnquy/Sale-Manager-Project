from flask_restplus import Namespace, fields


class UserDto:
    api = Namespace("users", description="user related operations")
    user = api.model(
        "user",
        {
            "id": fields.String(description="user identifier"),
            "username": fields.String(required=True, description="user username"),
            "email": fields.String(required=True, description="user email address"),
            "password": fields.String(required=True, description="user password"),
            "avatar": fields.String(),
            "role": fields.Integer(),
            "display_name": fields.String(),
            "date_of_birth": fields.DateTime(),
            "created_at": fields.DateTime(),
            "updated_at": fields.DateTime(),
            "is_deleted": fields.Boolean(),
            "deleted_at": fields.DateTime(),
        },
    )
