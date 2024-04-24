import pandas as pd
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


# for the line chart
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
    result_df = df_grouped[['Month', 'Amount']].rename(columns={'Amount': 'Total Expenditure'})

    return result_df.to_dict(orient='records') # .to_json()

# for the stacked bar chart, old
def aggregate_spending_by_category(df):
    """
    Aggregate spending by category for each month.

    Parameters:
    - df: pandas DataFrame with columns 'Date', 'Category', and 'Amount'.

    Returns:
    - A new DataFrame with months as rows, categories as columns, and the sum of expenditures as values.
    """

    # Extract year and month from 'Date' and create a new column for it
    df['YearMonth'] = df['Date'].dt.to_period('M')
    
    # Group by the new 'YearMonth' column and 'Category', and sum 'Amount'
    result_df = df.groupby(['YearMonth', 'Category'])['Amount'].sum().unstack(fill_value=0)

    # Reset the index to make 'YearMonth' a column again
    result_df.reset_index(inplace=True)
    
    # Optionally format 'YearMonth' to 'Month Year' for better readability
    result_df['YearMonth'] = result_df['YearMonth'].dt.strftime('%B %Y')

    return result_df

# for the stacked bar chart
def aggregate_spending_by_category_long_form(df):
    """
    Aggregate spending by category for each month in a long form.

    Parameters:
    - df: pandas DataFrame with columns 'Date', 'Category', and 'Amount'.

    Returns:
    - A new DataFrame in long form with 'YearMonth', 'Category', and 'Amount'.
    """
    
    # Extract year and month from 'Date' and create a new column for it
    df['YearMonth'] = df['Date'].dt.to_period('M')
    
    # Group by the new 'YearMonth' column and 'Category', and sum 'Amount'
    result_df = df.groupby(['YearMonth', 'Category'])['Amount'].sum().reset_index()
    
    # Optionally format 'YearMonth' to 'Month Year' for better readability
    result_df['YearMonth'] = result_df['YearMonth'].dt.strftime('%B %Y')

    return result_df
