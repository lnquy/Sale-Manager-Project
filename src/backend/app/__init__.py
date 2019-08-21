from flask_restplus import Api
from flask import Blueprint

from .main.controller.user_controller import api as user_ns
from .main.controller.book_controller import api as book_ns

blueprint = Blueprint("api", __name__)

api = Api(
    blueprint,
    title="FLASK RESTPLUS API BOILER-PLATE WITH JWT",
    version="1.0",
    description="a boilerplate for flask restplus web service",
)

api.add_namespace(user_ns, path="/api/v1/users")
api.add_namespace(book_ns, path="/api/v1/books")