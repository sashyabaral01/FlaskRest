import mysql.connector
import json

from mysql.connector import Error
from flask import Flask, jsonify, render_template,request,make_response

app = Flask(__name__)



@app.route('/search')

def home():

    return render_template("index.html")







@app.route('/query')


def example():


    name = request.args['name']
 #if key doesn't exist, returns None
    name = str(name)

    print(name,"This is name")
    connection = mysql.connector.connect(host='localhost',
                                         database='test',
                                         user='sashya',
                                         password='finger11')

    cursor = connection.cursor(dictionary=True)


    sql_select_Query = "SELECT email,last_name FROM test WHERE first_name = 'sashya' "

    print(sql_select_Query,"This is the select query")

    cursor.execute(sql_select_Query)
    records = cursor.fetchall()

    data = []
    for record in records:
        first_name = record["first_name"]
        email = record["email"]
        last_name = record['last_name']

        data.append({'first_name':first_name'email': email, 'last_name': last_name})






    return jsonify(data=data)

if __name__ == '__main__':
    app.run(debug=True)
