# BudgetFriend

BudgetFriend is a simple web application designed to help users track personal expenses and analyze spending patterns. The application is built using React with Tailwind CSS for styling on the frontend and Python Flask on the backend. It allows users to input expense data via a `.csv` file, and visualizes this data through interactive charts.

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

## Possible Improvements
1. **Support for Excel Files:** Extend file upload capabilities to include .xlsx files by modifying the ALLOWED_EXTENSIONS in the Flask application.
2. **Date Range Filtering:**  Implement a calendar date picker on the frontend for selecting specific date ranges, and adjust the backend pandas datetime to filter data accordingly.
3. **Security:**  If this application is adapted for medical purposes involving sensitive data, it should be hosted locally or on an internal server, rather than on a remote server or cloud. This precaution helps prevent unauthorized access to or caching of sensitive information.