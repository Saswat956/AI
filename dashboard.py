import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data from Excel file
@st.cache_data
def load_data():
    # Replace 'data.xlsx' with your actual file path if needed
    df = pd.read_excel('data.xlsx', engine='openpyxl')
    return df

# Load data
df = load_data()

# Streamlit dashboard setup
st.set_page_config(page_title="Data Policy Dashboard", layout="wide")

# Title of the dashboard
st.title("Data Policy Dashboard")

# Sidebar for filtering options
st.sidebar.header("Filter Options")
policy_filter = st.sidebar.multiselect("Select EDM Policy:", options=df["EDM Policy"].unique())
risk_type_filter = st.sidebar.multiselect("Select Data Risk Type:", options=df["Data Risk Type"].unique())

# Filter DataFrame based on user input
if policy_filter:
    df = df[df["EDM Policy"].isin(policy_filter)]
if risk_type_filter:
    df = df[df["Data Risk Type"].isin(risk_type_filter)]

# Display the filtered DataFrame
st.subheader("Filtered Records")
st.dataframe(df)

# Visualization 1: Policy Type Distribution (Bar Chart)
st.subheader("1. Policy Type Distribution")
policy_type_counts = df['Policy Type'].value_counts()
st.bar_chart(policy_type_counts)

# Visualization 2: Unique Policy Numbers by Data Risk Type (Bar Chart)
st.subheader("2. Unique Policy Numbers by Data Risk Type")
policy_by_risk_type = df.groupby('Data Risk Type')['Policy Number'].nunique()
st.bar_chart(policy_by_risk_type)

# Visualization 3: Standard Name Count by Policy Type (Bar Chart)
st.subheader("3. Standard Name Count by Policy Type")
standard_name_counts = df['Standard Name'].value_counts()
st.bar_chart(standard_name_counts)

# Visualization 4: Non-Conformance Status Distribution (Bar Chart)
st.subheader("4. Non-Conformance Status Distribution")
non_conformance_counts = df['Non-Conformance Status'].value_counts()
st.bar_chart(non_conformance_counts)

# Visualization 5: Average Disposal Timeframe by Standard Name (Bar Chart)
if 'Disposal Timeframe' in df.columns:
    st.subheader("5. Average Disposal Timeframe by Standard Name")
    avg_disposal_by_standard = df.groupby('Standard Name')['Disposal Timeframe'].mean()
    st.bar_chart(avg_disposal_by_standard)

# Visualization 6: Pie Chart for EDM Policies
st.subheader("6. Pie Chart of EDM Policies")
edm_policy_counts = df['EDM Policy'].value_counts()
fig, ax = plt.subplots()
ax.pie(edm_policy_counts, labels=edm_policy_counts.index, autopct='%1.1f%%', startangle=90)
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
st.pyplot(fig)

# Visualization 7: Heatmap of Non-Conformance Status vs Data Risk Type
st.subheader("7. Heatmap of Non-Conformance Status vs Data Risk Type")
heatmap_data = pd.crosstab(df['Non-Conformance Status'], df['Data Risk Type'])
sns.heatmap(heatmap_data, annot=True, fmt="d", cmap="YlGnBu")
plt.title('Non-Conformance Status vs Data Risk Type')
st.pyplot()

# Visualization 8: Line Chart for Records Last Updated Over Time
if 'Records Last Updated' in df.columns:
    st.subheader("8. Records Last Updated Over Time")
    df['Records Last Updated'] = pd.to_datetime(df['Records Last Updated'])
    records_over_time = df.groupby(df['Records Last Updated'].dt.to_period('M')).size()
    st.line_chart(records_over_time)

# Visualization 9: Box Plot for Disposal Timeframe by Business Rule ID (if available)
if 'Business Rule ID' in df.columns and 'Disposal Timeframe' in df.columns:
    st.subheader("9. Box Plot for Disposal Timeframe by Business Rule ID")
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='Business Rule ID', y='Disposal Timeframe', data=df)
    plt.xticks(rotation=45)
    plt.title('Disposal Timeframe by Business Rule ID')
    st.pyplot()

# Visualization 10: Count of Records by Standard ID (Bar Chart)
if 'Standard ID' in df.columns:
    st.subheader("10. Count of Records by Standard ID")
    standard_id_counts = df['Standard ID'].value_counts()
    st.bar_chart(standard_id_counts)
