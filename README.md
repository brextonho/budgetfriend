# BudgetFriend

BudgetFriend is a simple web application designed to help users track personal expenses and analyze spending patterns. The application is built using React with Tailwind CSS for styling on the frontend and Python Flask on the backend. It allows users to input expense data via a `.csv` file, and visualizes this data through interactive charts.

![app_interface](https://github.com/brextonho/budgetfriend/assets/88436113/1a0590ad-7f88-4dd3-a22b-4c06d70711f3)


## Installation

Follow these steps to set up and run BudgetFriend on your local machine:

### Prerequisites

- Python 3.8+
- Node.js 12.0+
- npm

### Setting Up the Project

1. **Clone the GitHub repository:**
    ```bash
    git clone https://github.com/yourusername/BudgetFriend.git
    cd BudgetFriend
    ```

2. **Set up the Python virtual environment:**
Navigate to the server directory if not already there and create virtual environment
    ```bash
    cd server
    python -m venv venv
    ```

Activate virtual environment
Windows
```bash
.\venv\Scripts\activate
```

macOS or Linux
```bash
source venv/bin/activate
```

3. **Install backend dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up and run the Flask server:**
    ```bash
    python run.py
    ```


5. **Install frontend dependencies and run the React app:**
Open a new terminal window/tab
    ```bash
    cd ui
    npm install
    npm start
    ```

## Feature Description
BudgetFriend is primarily a local application, ensuring user data privacy and security by processing and storing all data locally. Key features include:

**Image Download:** You may right click on graph to ‘Save image as’ to save to local machine

**CSV File Upload:** Users can upload their expense data in CSV format.

**Expense Visualization:** Interactive charts built with Chart.js display spending patterns over time and by category.

**Local Data Processing:** All data is processed on the user's machine to ensure privacy.

Additional tools:
A Jupyter notebook (server/charttesting.ipynb) was used for initial data exploration using Plotly.

### Workflow
Upon uploading the .csv file in React frontend, the <code>FileUpload</code> component calls the <code>/upload-csv POST</code> function in Flask <code>routes.py</code> to upload the csv file into /uploads folder. If successful, it will call the <code>/linechart</code> and <code>/barchart</code> <code>GET</code> functions in Flask for the json data, for it to be passed to the <code>LineChart</code> and <code>StackedBarChart</code> react-chartjs-2 components, which would then render on the main page.

1. **File Upload Initiation:**
Users select a .csv file to upload via the React frontend's <code>FileUpload</code> component. This component includes input validation to ensure that the file format is correct before it is sent to the backend.

2. **File Transmission to Backend:**
The selected file is sent to the backend Flask server by making a <code>POST</code> request to the <code>/upload-csv</code> endpoint in Flask <code>routes.py</code>. This endpoint is responsible for handling incoming file uploads.

3. **Server-Side File Handling:**
Upon receiving the file, the Flask application verifies its type and integrity. If the file is not a valid .csv, an error response is generated and sent back to the frontend.
Valid files are saved to the <code>/uploads</code> folder on the server. The server then responds with a success status if the file has been successfully saved.

4. **Data Processing and Visualization:**
Once the file is successfully uploaded, the frontend makes two <code>GET</code> requests to <code>/linechart</code> and <code>/barchart</code> endpoints in Flask <code>routes.py</code> to fetch the processed data for visualization.
The Flask backend processes the uploaded file with the help of functions in <code>utils.py</code> to generate the data needed for the charts:
- The <code>/linechart</code> endpoint processes the data to extract time-series information suitable for the line chart.
- The <code>/barchart</code> endpoint aggregates the data by categories and months, formatting it for the stacked bar chart.
Each endpoint returns JSON data that encapsulates the chart-ready information.

5. **Rendering Charts:**
Upon receiving the JSON data from each respective <code>GET</code> request, the frontend uses this data to render the <code>LineChart</code> and <code>StackedBarChart</code> components using react-chartjs-2.
These charts are then displayed on the main page, allowing users to visually analyze their expense patterns over time and by category.


## Possible Improvements
1. **Support for Excel Files:** Extend file upload capabilities to include .xlsx files by modifying the <code>ALLOWED_EXTENSIONS</code> in the Flask application.
2. **Date Range Filtering:**  Implement a calendar date picker on the frontend for selecting specific date ranges, and adjust the backend pandas datetime to filter data accordingly.


![date_picker](https://github.com/brextonho/budgetfriend/assets/88436113/ba7d8910-884c-4548-b29f-aa9e0f6efb7b)


3. **Security:**  If this application is adapted for medical purposes involving sensitive data, it should be hosted locally or on an internal server, rather than on a remote server or cloud. This precaution helps prevent unauthorized access to or caching of sensitive information.
4. **Proper handling of endpoints:** Change localhost to <code>{ API_ENDPOINT } from "$env/static/private</code> in <code>FileUpload</code> to allow for variable endpoints and security purposes
