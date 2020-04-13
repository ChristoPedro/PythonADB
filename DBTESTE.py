from flask import Flask
from flask import request
from flask import Response
import cx_Oracle
import json
import os

app = Flask(__name__)

connection = cx_Oracle.connect(os.getenv('USER'), os.getenv('PASSWORD'), "python_high")

@app.route("/data", methods=["GET"])
def response():
        cursor = connection.cursor()
        cursor.execute("""SELECT json_object( 'id' value CUST_ID, 'name' value CUST_FIRST_NAME) FROM SH.CUSTOMERS where ROWNUM < 10""")
        data = []

        for value, in cursor:
                data.append(json.loads(value,))
        data = json.dumps(data)
        return Response(data, mimetype='application/json')

if __name__ == '__main__':
    
        app.run(debug=True, host='0.0.0.0')