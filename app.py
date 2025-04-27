import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Function to show the steps of the wizard
def show_wizard_step(step):
    if step == 1:
        st.markdown('<div class="box">', unsafe_allow_html=True)
        st.title("Step 1: User Information")
        st.write("Please fill out your basic information:")
        name = st.text_input("What is your name?")
        age = st.number_input("How old are you?", min_value=1)
        if st.button("Next"):
            # Store data in session state and go to next step
            st.session_state.name = name
            st.session_state.age = age
            st.session_state.step = 2
        st.markdown('</div>', unsafe_allow_html=True)

    elif step == 2:
        st.markdown('<div class="box">', unsafe_allow_html=True)
        st.title("Step 2: Upload Your Data")
        st.write("Please upload a CSV file with your data:")
        file = st.file_uploader("Choose a file", type="csv")
        if file is not None:
            st.session_state.file = file
            st.session_state.step = 3
        st.markdown('</div>', unsafe_allow_html=True)

    elif step == 3:
        st.markdown('<div class="box">', unsafe_allow_html=True)
        st.title("Step 3: Data Analysis & Visualization")
        if "file" in st.session_state:
            # Read the uploaded file into a DataFrame
            df = pd.read_csv(st.session_state.file)
            st.write("Here’s a preview of your data:")
            st.dataframe(df.head())

            # Options for selecting the type of plot
            chart_type = st.selectbox("Choose chart type", ["Bar", "Line", "Scatter", "Heatmap"])
            
            if chart_type == "Bar":
                column = st.selectbox("Choose column to plot", df.columns)
                st.bar_chart(df[column])
                
            elif chart_type == "Line":
                x_column = st.selectbox("Choose X-axis column", df.columns)
                y_column = st.selectbox("Choose Y-axis column", df.columns)
                st.line_chart(df[[x_column, y_column]])

            elif chart_type == "Scatter":
                x_column = st.selectbox("Choose X-axis column", df.columns)
                y_column = st.selectbox("Choose Y-axis column", df.columns)
                fig, ax = plt.subplots()
                ax.scatter(df[x_column], df[y_column])
                ax.set_xlabel(x_column)
                ax.set_ylabel(y_column)
                st.pyplot(fig)
            
            elif chart_type == "Heatmap":
                # Filter numeric columns for heatmap
                numeric_columns = df.select_dtypes(include=np.number).columns
                heatmap_data = df[numeric_columns].corr()
                fig, ax = plt.subplots()
                sns.heatmap(heatmap_data, annot=True, cmap="coolwarm", ax=ax)
                st.pyplot(fig)

        if st.button("Finish"):
            st.success("Thank you for completing the wizard!")
            st.session_state.step = 1  # Reset the wizard
        st.markdown('</div>', unsafe_allow_html=True)

# Initialize session state variables if they don't exist
if "step" not in st.session_state:
    st.session_state.step = 1

# Custom CSS for the box styling
st.markdown("""
    <style>
        .box {
            width: 80%;
            margin: 30px auto;
            padding: 20px;
            background-color: #f7f7f7;
            border: 2px solid #ccc;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
            font-family: Arial, sans-serif;
        }
        .box:hover {
            background-color: #f1f1f1;
        }
        h1 {
            font-size: 24px;
            color: #333;
        }
        p {
            color: #555;
        }
    </style>
""", unsafe_allow_html=True)

# Show the current step inside the box
show_wizard_step(st.session_state.step)
