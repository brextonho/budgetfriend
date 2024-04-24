from flask import Flask, flash, request, redirect, url_for, jsonify, current_app
from werkzeug.utils import secure_filename
from app.utils import process_csv
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

@app.route('/upload-csv', methods=['POST'])
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
    
        # process file after saving
        # try:
        #     df = process_csv(filepath)

        #     # Here you can aggregate and process data as per the requirements
        #     # For example, aggregate data by week, month, or year, and by category
        #     # And then generate JSON for charting
        #     # processed_data = some_aggregation_function(df)

        #     # Let's assume processed_data is a dictionary containing the data you want to visualize
        #     # You would then send this data back in the response
        #     # return jsonify(processed_data)
        
        # except Exception as e:
        #     # Handle exceptions that may occur during file processing
        #     return jsonify(error=str(e)), 500
    
    else:
        return jsonify(error="Invalid file type"), 400


@app.route('/data', methods=['GET'])
def get_data():
    # TODO: Assume 'data' is the processed data ready for charting

    data = [
        {'Month': 'January 2019', 'TotalExpenditure': 2457.76},
        {'Month': 'February 2019', 'TotalExpenditure': 3299.60},
        { 'Month': 'March 2019', 'TotalExpenditure': 2457.76 },
        { 'Month': 'April 2019', 'TotalExpenditure': 3299.60 },
        { 'Month': 'May 2019', 'TotalExpenditure': 2457.76 },
        { 'Month': 'June 2019', 'TotalExpenditure': 3299.60 },
    ]


    return jsonify(data)
