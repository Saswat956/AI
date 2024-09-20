import streamlit as st

# Breadcrumb placeholder at the top of the page
breadcrumb_placeholder = st.empty()

# Define options for each level
level_1_options = ['AEMP79', 'AEMP80', 'AEMP81']
level_2_options = ['Data Quality', 'Data Governance', 'Data Security']
level_3_options = ['AEMP08', 'AEMP09', 'AEMP10']
level_4_options = ['DQ01', 'DQ02', 'DQ03']
level_5_options = ['DS02', 'DS03', 'DS04']
level_6_options = ['BR001', 'BR002', 'BR003']

# Initialize an empty list to store breadcrumb values
breadcrumb_parts = []

# Step 1: Select Level 1
level_1 = st.selectbox("Select Level 1", level_1_options)
breadcrumb_parts.append(level_1)

# Display the updated breadcrumb
breadcrumb_placeholder.markdown(f"**{' >> '.join(breadcrumb_parts)}**")

# Step 2: Show Level 2 dropdown after Level 1 is selected
if level_1:
    level_2 = st.selectbox("Select Level 2", level_2_options)
    breadcrumb_parts.append(level_2)
    breadcrumb_placeholder.markdown(f"**{' >> '.join(breadcrumb_parts)}**")

# Step 3: Show Level 3 dropdown after Level 2 is selected
if level_2:
    level_3 = st.selectbox("Select Level 3", level_3_options)
    breadcrumb_parts.append(level_3)
    breadcrumb_placeholder.markdown(f"**{' >> '.join(breadcrumb_parts)}**")

# Step 4: Show Level 4 dropdown after Level 3 is selected
if level_3:
    level_4 = st.selectbox("Select Level 4", level_4_options)
    breadcrumb_parts.append(level_4)
    breadcrumb_placeholder.markdown(f"**{' >> '.join(breadcrumb_parts)}**")

# Step 5: Show Level 5 dropdown after Level 4 is selected
if level_4:
    level_5 = st.selectbox("Select Level 5", level_5_options)
    breadcrumb_parts.append(level_5)
    breadcrumb_placeholder.markdown(f"**{' >> '.join(breadcrumb_parts)}**")

# Step 6: Show Level 6 dropdown after Level 5 is selected
if level_5:
    level_6 = st.selectbox("Select Level 6", level_6_options)
    breadcrumb_parts.append(level_6)
    breadcrumb_placeholder.markdown(f"**{' >> '.join(breadcrumb_parts)}**")
