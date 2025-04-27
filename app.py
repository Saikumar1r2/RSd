import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Function to load and display data
def load_data(file):
    try:
        df = pd.read_csv(file)
        return df
    except Exception as e:
        st.error(f"Error loading file: {e}")
        return None

# Function to display data summary statistics
def display_summary(df):
    st.write("### Summary Statistics")
    st.write(df.describe())

# Function to filter data
def filter_data(df):
    st.write("### Filter Data")
    columns = df.columns.tolist()
    selected_column = st.selectbox("Choose a column to filter by", columns)
    
    if selected_column:
        unique_values = df[selected_column].unique().tolist()
        selected_value = st.selectbox(f"Select a value from {selected_column}", unique_values)
        filtered_data = df[df[selected_column] == selected_value]
        st.write(f"Filtered Data by {selected_column}: {selected_value}")
        st.dataframe(filtered_data)
        return filtered_data
    return df

# Function to plot bar chart
def plot_bar_chart(df, x_column, y_column):
    st.write(f"### Bar Chart: {x_column} vs {y_column}")
    fig, ax = plt.subplots()
    df.groupby(x_column)[y_column].sum().plot(kind="bar", ax=ax)
    ax.set_xlabel(x_column)
    ax.set_ylabel(f"Sum of {y_column}")
    st.pyplot(fig)

# Function to plot line chart
def plot_line_chart(df, x_column, y_column):
    st.write(f"### Line Chart: {x_column} vs {y_column}")
    fig, ax = plt.subplots()
    df.plot(kind="line", x=x_column, y=y_column, ax=ax)
    ax.set_xlabel(x_column)
    ax.set_ylabel(y_column)
    st.pyplot(fig)

# Function to plot scatter plot
def plot_scatter_chart(df, x_column, y_column):
    st.write(f"### Scatter Plot: {x_column} vs {y_column}")
    fig, ax = plt.subplots()
    ax.scatter(df[x_column], df[y_column])
    ax.set_xlabel(x_column)
    ax.set_ylabel(y_column)
    st.pyplot(fig)

# Function to plot heatmap
def plot_heatmap(df):
    st.write("### Heatmap: Correlation Matrix")
    correlation = df.corr()
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(correlation, annot=True, cmap="coolwarm", ax=ax)
    st.pyplot(fig)

# Main application function
def main():
    st.title("Data Dashboard Application")

    # Upload CSV file
    file = st.file_uploader("Upload a CSV file", type="csv")
    
    if file is not None:
        df = load_data(file)

        if df is not None:
            # Display data preview
            st.write("### Data Preview")
            st.dataframe(df.head())

            # Summary statistics
            display_summary(df)

            # Filter data
            filtered_data = filter_data(df)

            # Visualizations
            st.write("### Choose a chart to visualize")
            chart_type = st.radio("Select chart type", ("Bar", "Line", "Scatter", "Heatmap"))

            if chart_type == "Bar":
                x_column = st.selectbox("Choose X-axis column", df.columns)
                y_column = st.selectbox("Choose Y-axis column", df.columns)
                plot_bar_chart(filtered_data, x_column, y_column)
            elif chart_type == "Line":
                x_column = st.selectbox("Choose X-axis column", df.columns)
                y_column = st.selectbox("Choose Y-axis column", df.columns)
                plot_line_chart(filtered_data, x_column, y_column)
            elif chart_type == "Scatter":
                x_column = st.selectbox("Choose X-axis column", df.columns)
                y_column = st.selectbox("Choose Y-axis column", df.columns)
                plot_scatter_chart(filtered_data, x_column, y_column)
            elif chart_type == "Heatmap":
                plot_heatmap(filtered_data)

            # Data export button
            st.write("### Export Data")
            if st.button("Download Filtered Data as CSV"):
                filtered_data.to_csv("filtered_data.csv", index=False)
                st.download_button(label="Download CSV", data=filtered_data.to_csv(index=False), file_name="filtered_data.csv", mime="text/csv")

if __name__ == "__main__":
    main()
