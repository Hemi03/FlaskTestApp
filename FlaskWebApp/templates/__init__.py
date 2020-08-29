from flask import render_template, Blueprint

ROUTES = Blueprint("routes", __name__)


@ROUTES.route('/test', methods=['GET'])
def test():
    return render_template("test.html")


@ROUTES.route('/', methods=['GET'])
def main_page():
    return render_template("index.html")
