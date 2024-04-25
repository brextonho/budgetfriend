from flask import Flask, flash, request, redirect, url_for, jsonify, current_app
from werkzeug.utils import secure_filename
import app.utils as utils
import os

from app import app

ALLOWED_EXTENSIONS = {'csv'} # allows for future extensions

app.config['UPLOAD_FOLDER'] = 'uploads'

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def home():
    return jsonify(message="Welcome to the BudgetFriend API!")

@app.route('/upload-csv', methods=['POST']) # ,'GET'
def upload_csv():
    if 'file' not in request.files:
        return jsonify(error="No file part"), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify(error="No selected file"), 400
    
    if file and allowed_file(file.filename):
        # sanitize the file name
        filename = secure_filename(file.filename)
        filepath = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        return jsonify(success="File uploaded successfully", filename=filename), 200
    
    else:
        return jsonify(error="Invalid file type"), 400
    
 

@app.route('/linechart', methods=['GET'])
def linechart():
    try:
        latest_file = utils.find_latest_file(current_app.config['UPLOAD_FOLDER'])
        if not latest_file:
            return jsonify(error="No files found."), 404
        
        chart_data = utils.sum_expenditure_by_month(latest_file)
        # print(chart_data)
        print("TEST line")
        print(jsonify(chart_data))
        return chart_data # (jsonify(chart_data))
    except Exception as e:
        return jsonify(error=str(e)), 500


@app.route('/barchart', methods=['GET'])
def barchart():
    try:
        latest_file = utils.find_latest_file(current_app.config['UPLOAD_FOLDER'])
        if not latest_file:
            print('No files found')
            return jsonify(error="No files found."), 404
        
        # chart_data = utils.aggregate_spending_by_category_long_form(latest_file) # TODO test
        chart_data = utils.barchart(latest_file)
        print(chart_data)
        print("TEST bar")
        print(jsonify(chart_data))
        return chart_data # (jsonify(chart_data))
    except Exception as e:
        return jsonify(error=str(e)), 500

