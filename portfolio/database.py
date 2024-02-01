from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:vidya2812@localhost/portfolio'
db = SQLAlchemy(app)




# Inserting data into the existing 'vidya' table without using a model
def add_msg_to_db(data):
    with app.app_context():
        # Create a new entry in the 'vidya' table
        name = data.get('Name', '')  # Use get with a default value
        email = data.get('Email', '')
        message = data.get('Message', '')

        # Use parameterized query to insert data
        sql_query = "INSERT INTO contact (name, email, message) VALUES (%s, %s, %s)"
        connection = db.engine.raw_connection()
        cursor = connection.cursor()
        cursor.execute(sql_query, (name, email, message))
        connection.commit()
        cursor.close()
        connection.close()
        
        
        return jsonify({'status': 'success'})
