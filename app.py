import streamlit as st
import pandas as pd

# Initialize session state for sample management
if 'samples' not in st.session_state:
    st.session_state.samples = []

# Function to add new sample
def add_sample():
    sample = {
        "Sample ID": st.text_input("Enter Sample ID:"),
        "Sample Type": st.selectbox("Select Sample Type:", ["Blood", "Urine", "Saliva"]),
        "Collection Date": st.date_input("Collection Date:"),
        "Status": st.selectbox("Sample Status:", ["Received", "Under Testing", "Completed"])
    }
    st.session_state.samples.append(sample)

# Function to add test result for a sample
def add_test_result(sample_id):
    test_result = st.text_area(f"Enter test result for Sample {sample_id}:")
    return test_result

# Display Sample Management Interface
st.title("Simple LIMS - Sample Manager")

# Add a new sample
if st.button("Add New Sample"):
    add_sample()

# Display all samples in a table
st.write("## Sample List")
if st.session_state.samples:
    sample_df = pd.DataFrame(st.session_state.samples)
    st.dataframe(sample_df)

    # Option to add test result for each sample
    sample_id = st.selectbox("Select Sample to Add Test Result:", sample_df["Sample ID"].tolist())
    test_result = add_test_result(sample_id)

    # Button to save the test result
    if st.button(f"Save Test Result for Sample {sample_id}"):
        st.write(f"Test Result for Sample {sample_id}: {test_result}")
else:
    st.write("No samples added yet.")
