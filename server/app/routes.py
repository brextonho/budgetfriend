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
    # if request.method == 'POST':
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
            #     # Assuming process_csv returns data in the expected format for LineGraph
            #     processed_data = utils.process_csv(filepath)

            #     # TODO change this
            #     # test
            #     line_df = utils.sum_expenditure_by_month(processed_data)

            #     return jsonify(line_df)
            # except Exception as e:
            #     return jsonify(error=str(e)), 500
        
        else:
            return jsonify(error="Invalid file type"), 400
    
    # return '''
    # <!doctype html>
    # <title>Upload new File</title>
    # <h1>Upload new File</h1>
    # <form method=post enctype=multipart/form-data>
    #   <input type=file name=file>
    #   <input type=submit value=Upload>
    # </form>
    # '''


# @app.route('/data', methods=['GET'])
# def get_data():
#     # TODO: Assume 'data' is the processed data ready for charting

#     data = [
#         {'Month': 'January 2019', 'TotalExpenditure': 2457.76},
#         {'Month': 'February 2019', 'TotalExpenditure': 3299.60},
#         { 'Month': 'March 2019', 'TotalExpenditure': 2457.76 },
#         { 'Month': 'April 2019', 'TotalExpenditure': 3299.60 },
#         { 'Month': 'May 2019', 'TotalExpenditure': 2457.76 },
#         { 'Month': 'June 2019', 'TotalExpenditure': 3299.60 },
#     ]

#     return jsonify(data)

@app.route('/linechart', methods=['GET'])
def linechart():
    try:
        latest_file = utils.find_latest_file(current_app.config['UPLOAD_FOLDER'])
        if not latest_file:
            return jsonify(error="No files found."), 404
        
        chart_data = utils.sum_expenditure_by_month(latest_file)
        print(chart_data)

        print("TEST")
        print(jsonify(chart_data))
        return jsonify(chart_data)
    except Exception as e:
        return jsonify(error=str(e)), 500



@app.route('/barchart', methods=['GET'])
def barchart():
    return (utils.aggregate_spending_by_category_long_form())

