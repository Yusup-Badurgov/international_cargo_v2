from flask import Flask, render_template, request, jsonify

from flask_sqlalchemy import SQLAlchemy

from dao.dao_personal_item import personal_dao

application = Flask(__name__)
application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///price_personal_items.db'
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
application.config['JSON_AS_ASCII'] = False
application.config['RESTX_JSON'] = {'ensure_ascii': False}


@application.route('/', methods=['GET', 'POST'])
def personal_items():
    if request.method == 'GET':
        CSS = '<link rel="stylesheet" type="text/css" href="CSS/styles.css">'
        countries = personal_dao.get_country()
        return render_template('personal_items.html', countries=countries, CSS=CSS)


    elif request.method == 'POST':
        country = request.form['country']
        direction = request.form['direction']
        cubes = request.form['cubes']
        shipping_cost = calculate_shipping_cost(country, direction, cubes)
        return shipping_cost


def calculate_shipping_cost(country, direction, cubes):

    shipping_cost = personal_dao.get_price(cubes, country, direction)
    return shipping_cost



if __name__ == '__main__':
    application.run()
