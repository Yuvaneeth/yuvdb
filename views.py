from flask import Flask, request, jsonify, render_template
from utils import connect_mysql, connect_redshift
import json
app = Flask(__name__)


@app.route('/mysql', methods=['GET'])
def query_mysql():
    query = request.args.get('query', 'show tables;')
    database = request.args.get('database')
    connection = connect_mysql(host='database-1.c5ov2h84nuch.us-east-2.rds.amazonaws.com', user='admin',
                               password='Awsdbs10!', db=database)
    col_name, content, query_time = connection.run_query(query)
    result = {'col_name': col_name, 'result': content, 'query_time': query_time}
    connection.disconnect()
    print(result['result'])
    return jsonify(result)


@app.route('/redshift', methods=['GET'])
def query_redshift():
    query = request.args.get('query', 'show tables;')
    print("query is " + query)
    database = request.args.get('database')
    print("database is " + database)
    connection = connect_redshift(host='redshift-cluster-1.ckay2097thwx.us-east-2.redshift.amazonaws.com', user='admin',
                                  password='Awsdbs10!',
                                  database=database)
    col_name, content, query_time = connection.run_query(query)
    result = {'col_name': col_name, 'result': content, 'query_time': query_time}
    connection.disconnect()
    print(result['result'])
    return jsonify(result)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


# @app.route('/v_timestamp')
# def v_timestamp():
#     mycursor.execute("SELECT * FROM v_timestamp1")
#     data = mycursor.fetchall()
#     return render_template('v_timestamp.html', data=data)
# https://kanchanardj.medium.com/how-to-display-database-content-in-your-flask-website-8a62492ba892