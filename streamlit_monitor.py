import streamlit as st
import pandas as pd

# Load the data from Excel file
@st.cache_data
def load_data():
    # Replace 'data.xlsx' with your actual file path if needed
    df = pd.read_excel('data.xlsx', engine='openpyxl')
    return df

# Load data
df = load_data()

# Streamlit dashboard setup
st.set_page_config(page_title="Record Management Dashboard", layout="wide")

# Title of the dashboard
st.title("Record Management Dashboard")

# Sidebar for filtering options
st.sidebar.header("Filter Options")
status_filter = st.sidebar.multiselect("Select Record Status:", options=df["Record Status"].unique())
department_filter = st.sidebar.multiselect("Select Department:", options=df["Department"].unique())

# Filter DataFrame based on user input
if status_filter:
    df = df[df["Record Status"].isin(status_filter)]
if department_filter:
    df = df[df["Department"].isin(department_filter)]

# Display the filtered DataFrame
st.subheader("Filtered Records")
st.dataframe(df)

# Display statistics or metrics if needed
st.subheader("Statistics")
st.write(f"Total Records: {len(df)}")
st.write(f"Unique Departments: {df['Department'].nunique()}")
if 'Disposal Timeframe' in df.columns:
    st.write(f"Average Disposal Timeframe: {df['Disposal Timeframe'].mean()} days")

# Example of visualizing some data (e.g., bar chart of record statuses)
if 'Record Status' in df.columns:
    st.subheader("Record Status Distribution")
    status_counts = df['Record Status'].value_counts()
    st.bar_chart(status_counts)

# Example of visualizing Disposal Timeframe by Department if available
if 'Disposal Timeframe' in df.columns and 'Department' in df.columns:
    st.subheader("Disposal Timeframe by Department")
    disposal_timeframe_by_dept = df.groupby('Department')['Disposal Timeframe'].mean()
    st.bar_chart(disposal_timeframe_by_dept)
