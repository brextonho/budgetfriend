import pandas as pd
import numpy as np
import os

def find_latest_file(directory):
    """Returns the path to the latest (most recently modified) file in the specified directory."""
    # List all files in the directory
    files = [os.path.join(directory, file) for file in os.listdir(directory)]
    # Filter out directories, only files are needed
    files = [f for f in files if os.path.isfile(f)]
    # Sort files by last modification time
    files.sort(key=os.path.getmtime, reverse=True)
    # Return the newest file
    if files:
        return files[0]
    else:
        return None

def process_csv(filepath):
    # Read the CSV file
    df = pd.read_csv(filepath)
    df['Date'] = pd.to_datetime(df['Date'], format="%d/%m/%Y")
    return df

# input year as int
def filter_by_year(df, year):
    """
    Filter a DataFrame by a given year, returning a new DataFrame
    with rows only from that year.

    Parameters:
    - df: A pandas DataFrame with a 'Date' column in datetime format.
    - year: An integer representing the year to filter by.

    Returns:
    - A pandas DataFrame with rows from the specified year.
    """

    # Filter the DataFrame for the given year
    filtered_df = df[df['Date'].dt.year == year]
    
    return filtered_df

# input month as int
def filter_by_month(df, month):
    """
    Filter a DataFrame by a given month name, returning a new DataFrame
    with rows only from that month.

    Parameters:
    - df: A pandas DataFrame with a 'Date' column in datetime format.
    - month: Integer representing the month to filter by, e.g., 2 for February

    Returns:
    - A pandas DataFrame with rows from the specified month.
    """
    
    # Get the month number for the given month name
    # month_num = month_to_num.get(month.capitalize())
    months = [1,2,3,4,5,6,7,8,9,10,11,12]


    if month not in months:
        raise ValueError(f"Invalid month name: {month}")
    
    # Filter the DataFrame for the given month number
    filtered_df = df[df['Date'].dt.month == month]
    
    return filtered_df


# for the line chart, total expenditure
def sum_expenditure_by_month(file_path):
    """
    Sum the expenditure by month, with the month and year formatted as 'January 2019', etc.

    Parameters:
    - df: pandas DataFrame with a 'Date' and 'Amount' column.

    Returns:
    - A new DataFrame with 'Month' and 'Total Expenditure' columns.
    """
    # TODO how do you have it processed once then used by all get functions?
    df = process_csv(file_path)
    # Group by year and month, and sum the amounts
    df_grouped = df.groupby(df['Date'].dt.to_period("M"))['Amount'].sum().reset_index()

    # Convert the 'Date' periods back to timestamp to format them
    df_grouped['Date'] = df_grouped['Date'].dt.to_timestamp()

    # Format the 'Date' column as 'Month Year'
    df_grouped['Month'] = df_grouped['Date'].dt.strftime('%B %Y')

    # Rename columns and select only the needed ones
    result_df = df_grouped[['Month', 'Amount']] #.rename(columns={'Amount': 'Total Expenditure'})

    return result_df.to_dict(orient='records') # .to_json()


def barchart(file_path):
    """
    Aggregate spending by category for each month in a long form suitable for creating datasets
    for a stacked bar chart in Chart.js, ensuring chronological order of months.

    Parameters:
    - df: pandas DataFrame with columns 'Date', 'Category', and 'Amount'.

    Returns:
    - JSON object with 'labels' and 'datasets' suitable for Chart.js.
    """

    df = process_csv(file_path)
    # Extract year and month from 'Date' and create a new column for it, converting to period
    df['YearMonth'] = df['Date'].dt.to_period('M')
    
    # Group by the new 'YearMonth' column and 'Category', and sum 'Amount'
    result_df = df.groupby(['YearMonth', 'Category'])['Amount'].sum().unstack(fill_value=0).reset_index()

    # Sort the DataFrame by the datetime period (implicitly does it chronologically)
    result_df['YearMonth'] = result_df['YearMonth'].dt.to_timestamp()  # Convert to timestamp for sorting
    result_df.sort_values('YearMonth', inplace=True)
    result_df['YearMonth'] = result_df['YearMonth'].dt.strftime('%B %Y')  # Convert back to string for display

    # Convert the DataFrame to a dictionary that fits the structure needed for Chart.js
    datasets = []
    colors = {
        'Dining Out':'#DE3163',
        'Utilities':'#708090',
        'Transportation':'#0047AB',
        'Groceries':'#FDDA0D',
        'Entertainment':'#C3B1E1',
        'Health':'#008000',
    }
    categories = result_df.columns[1:]  # Skip the 'YearMonth' column

    for category in categories:
        datasets.append({
            'label': category,
            'data': result_df[category].tolist(),
            'backgroundColor': colors[category]
        })

    return {
        'labels': result_df['YearMonth'].tolist(),
        'datasets': datasets
    }
