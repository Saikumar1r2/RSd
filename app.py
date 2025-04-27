import streamlit as st
import sqlite3
import pandas as pd
from datetime import datetime

# Function to create and connect to the database
def create_connection():
    conn = sqlite3.connect('lims.db')
    return conn

# Function to create the table (if it doesn't exist)
def create_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS samples (
            sample_id TEXT PRIMARY KEY,
            sample_name TEXT,
            received_date TEXT
        )
    ''')
    conn.commit()
    conn.close()

# Function to add a new sample to the database
def add_sample(sample_id, sample_name, received_date):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO samples (sample_id, sample_name, received_date)
        VALUES (?, ?, ?)
    ''', (sample_id, sample_name, received_date))
    conn.commit()
    conn.close()

# Function to get all samples from the database
def get_all_samples():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM samples')
    samples = cursor.fetchall()
    conn.close()
    return samples

# Streamlit UI
st.title("LIMS - Sample Tracking")

# Create the table if it doesn't exist
create_table()

# Sidebar: Add new sample
st.sidebar.header("Add New Sample")
sample_id = st.sidebar.text_input("Sample ID")
sample_name = st.sidebar.text_input("Sample Name")
received_date = st.sidebar.date_input("Received Date", value=datetime.today())

# Button to save the sample
if st.sidebar.button("Add Sample"):
    if sample_id and sample_name:
        add_sample(sample_id, sample_name, received_date)
        st.sidebar.success(f"Sample {sample_id} added successfully!")
    else:
        st.sidebar.error("Please provide both Sample ID and Name.")

# Display the list of all samples
st.header("All Samples")
samples = get_all_samples()

# Convert the sample data into a DataFrame
df = pd.DataFrame(samples, columns=["Sample ID", "Sample Name", "Received Date"])

# Display the DataFrame
st.write(df)

# Button to refresh data
if st.button("Refresh Data"):
    st.experimental_rerun()
