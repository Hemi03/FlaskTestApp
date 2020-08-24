from flask import render_template, Blueprint

routes = Blueprint("routes", __name__)


@routes.route('/test', methods=['GET'])
def test():
    return 'it works!'


@routes.route('/', methods=['GET'])
def main_page():
    return render_template("index.html")
