from flask import Flask, request, jsonify
from pydantic import ValidationError
import mysql.connector
from werkzeug.security import generate_password_hash

from helpers.validations import SignupModel

app = Flask(__name__)


db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'root',
    'database': 'CSC312_db'
}

def get_db_connection():
    return mysql.connector.connect(**db_config)
@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

@app.route('/api/signup', methods=['POST'])
def signup():
    try:
        data = SignupModel(**request.get_json())
        username = data.username
        password = data.password
        hashed_password = generate_password_hash(password)

        # check if username already exist
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT username FROM tbl_user WHERE username = %s", (username,)
        )
        user_exist = cursor.fetchone()

        if user_exist:
            return jsonify({
                'status': False,
                'message': 'Username already exists'
            }), 400

        cursor.execute(
            "INSERT INTO tbl_user (username, password) VALUES (%s, %s)",
            (username, hashed_password,)
        )
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({
            'status': True,
            'message': 'Signup successful'
        }), 201

    except mysql.connector.Error as err:
        return jsonify({
            'status': False,
            'message': "Somthing went wrong: {}".format(err)
        })

    except ValidationError as e:
        return jsonify({
            'error': str(e),
            'message': 'Invalid request',
        })



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081, debug=True)
