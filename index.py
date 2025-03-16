from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_cors import CORS
from database import data

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get-data', methods=['GET'])
def get_data():
    message = request.args.get('message', '').strip().lower()
    response = data.get(message, 'Not Found')
    return jsonify({'response':response})

if __name__ == '__main__':
    app.run(debug=True)