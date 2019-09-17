import logging
import os
from flask import request
from flask_restplus import Resource

from ..util.dto.book import BookDto
from ..util.jwt import get_user_role_by_token
from ..service.book_service import get_book_by_id, list_books, update_book, delete_book
from ..util.error import Unauthorized, raiseIfExcept


api = BookDto.api
_book = BookDto.book

log = logging.getLogger("book.controller")
log.setLevel(logging.DEBUG)


# Get list of books: GET /api/v1/books?limit=5&offset=10
# Query params: limit, offset
@api.route("/")
class BookList(Resource):
    @api.doc("list_of_books")
    # @api.expect(_user, validate=True)
    @api.response(501, "Failed to load list of books")
    @api.marshal_list_with(_book)  # Serialize/Encode/Marshal JSON
    def get(self):
        """Get list of books with limit and offset"""
        limit = request.args.get("limit")
        if limit == None:
            limit = 10
        offset = request.args.get("offset")
        books = list_books(limit, offset)
        return books


#     @api.expect(_user, validate=True)
#     @api.response(201, "User successfully created.")
#     @api.doc("create a new book")
#     def post(self):
#         """Creates a new Book """
#         try:
#             data = request.json
#             return save_new_boom(data=data)
#         except Exception as e:
#             log.exception("failed to save book")


# Get book details by ID: GET /api/v1/books/:bid
# URL param: bid (book ID)
@api.route("/<int:bid>")
@api.param("bid", "Book identifier")
@api.response(404, "Book not found.")
class Book(Resource):
    @api.doc("Get book by ID")
    @api.marshal_with(_book)
    def get(self, bid):
        """Get book details by its id"""
        try:
            book = get_book_by_id(bid)
            if book is None:
                return "", 404
            else:
                return book
        except Exception as e:
            log.exception("failed to get book")

    @api.doc("Update book by ID")
    @api.param("bid", "Book identifier")
    def put(self, bid):
        """Update book details by its id"""
        token = request.headers.get("Authorization")
        role = get_user_role_by_token(token)
        if role != 1:
            raiseIfExcept(Unauthorized("Only admin allowed to update book"))
            return
        update_book(bid, request.json)
        return "", 200

    @api.doc("Delete book by ID")
    @api.param("bid", "Book identifier")
    def delete(self, bid):
        """Delete book by its id"""
        token = request.headers.get("Authorization")
        role = get_user_role_by_token(token)
        if role != 1:
            raiseIfExcept(Unauthorized("Only admin allowed to delete book"))
            return
        delete_book(bid)
        return {}


# @api.route("/<int:bid>/epub")
# @api.param("bid", "Book identifier")
# @api.response(404, "Book not found.")
# class Book(Resource):
#     @api.doc("Get EPUB file by ID")
#     def get(self, bid):
#         """Get book details by its id"""
#         log.error("HIT")
#         log.error(bid)
#         book = get_book_by_id(bid)
#         if book is None:
#             return "", 404

#         log.error(book)
#         for format in book.ebook_formats:
#             if format.type == "epub":
#                 log.error(format)
#                 return send_file(format.file_path, as_attachment=True)
#         return "", 404
