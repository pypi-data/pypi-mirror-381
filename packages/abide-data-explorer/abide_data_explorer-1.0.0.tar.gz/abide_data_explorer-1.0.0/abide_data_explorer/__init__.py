"""
ABIDE Data Explorer - A Streamlit application for exploring ABIDE II data.

This package provides a comprehensive GUI for data analysis and visualization
of ABIDE II Composite Phenotypic data.
"""

__version__ = "1.0.0"
__author__ = "Data Explorer Team"
__email__ = "contact@example.com"

from .app import main

__all__ = ['main']



"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
import pickle as pk
import xml.etree.ElementTree as ET

df=pd.read_csv('ABIDEII_Composite_Phenotypic.csv')

# Fix data types to avoid Arrow conversion issues
df = df.copy()

# Convert problematic columns to appropriate types
for col in df.columns:
    if df[col].dtype == 'object':
        # Keep string columns as strings
        df[col] = df[col].astype(str)
    elif df[col].dtype in ['int64', 'float64']:
        # Keep numeric columns but handle NaN values
        df[col] = pd.to_numeric(df[col], errors='coerce')

# Use Streamlit session state to persist DataFrame changes
if 'df' not in st.session_state:
    st.session_state.df = df.copy()
df = st.session_state.df

# Display the dataset
st.title("ABIDEII Composite Phenotypic Data Explorer")
st.write("## Dataset Preview") 
# Force convert all object columns to string to avoid Arrow conversion issues
display_df = df.copy()
for col in display_df.select_dtypes(include=['object']).columns:
    display_df[col] = display_df[col].astype(str)
st.dataframe(display_df.head())

# Summary statistics
st.write("## Summary Statistics")
try:
    summary_df = df.describe(include='all')
    # Convert summary to string to avoid Arrow issues
    for col in summary_df.select_dtypes(include=['object']).columns:
        summary_df[col] = summary_df[col].astype(str)
    st.dataframe(summary_df)
except Exception as e:
    st.error(f"Error displaying summary statistics: {e}")
    # Fallback: show basic info
    st.write("Dataset Shape:", df.shape)
    st.write("Column Names:", df.columns.tolist())
    st.write("Data Types:")
    st.write(df.dtypes)

# Data type conversion
st.write("## Convert Column Data Type")
col = st.selectbox("Select column to convert", df.columns)
dtype = st.selectbox("Select new data type", ["int", "float", "str"])
if st.button("Convert"):
    try:
        if dtype == "int":
            st.session_state.df[col] = st.session_state.df[col].astype(int)
        elif dtype == "float":
            st.session_state.df[col] = st.session_state.df[col].astype(float)
        else:
            st.session_state.df[col] = st.session_state.df[col].astype(str)
        st.success(f"Converted {col} to {dtype}")
    except Exception as e:
        st.error(f"Error: {e}")

# Sorting
st.write("## Sort Data")
sort_col = st.selectbox("Select column to sort", df.columns, key="sort")
if st.button("Sort"):
    try:
        st.session_state.df = st.session_state.df.sort_values(by=sort_col)
        # Create display version
        display_sorted = st.session_state.df.copy()
        for col in display_sorted.select_dtypes(include=['object']).columns:
            display_sorted[col] = display_sorted[col].astype(str)
        st.dataframe(display_sorted.head(20))  # Show first 20 rows
        st.success(f"Data sorted by {sort_col}")
    except Exception as e:
        st.error(f"Error sorting data: {e}")
        
# Grouping
st.write("## Group By")
group_col = st.selectbox("Select column to group by", df.columns, key="group")
agg_func = st.selectbox("Aggregation function", ["mean", "sum", "count"])
if st.button("Group"):
    try:
        if agg_func == "mean":
            # Only apply mean to numeric columns
            result = df.groupby(group_col).mean(numeric_only=True)
        elif agg_func == "sum":
            # Only apply sum to numeric columns
            result = df.groupby(group_col).sum(numeric_only=True)
        else:
            result = df.groupby(group_col).count()
        
        # Convert result for safe display
        result_display = result.copy()
        result_display = result_display.reset_index()
        for col in result_display.select_dtypes(include=['object']).columns:
            result_display[col] = result_display[col].astype(str)
        st.dataframe(result_display)
        st.success(f"Grouped by {group_col} using {agg_func}")
    except Exception as e:
        st.error(f"Error in grouping: {e}")
        st.write("Please select a valid column for grouping.")

# Slicing
st.write("## Slice Data")
start = st.number_input("Start row", min_value=0, max_value=len(df)-1, value=0)
end = st.number_input("End row", min_value=1, max_value=len(df), value=5)
if st.button("Slice"):
    try:
        sliced_df = df.iloc[int(start):int(end)].copy()
        # Convert object columns to string for display
        for col in sliced_df.select_dtypes(include=['object']).columns:
            sliced_df[col] = sliced_df[col].astype(str)
        st.dataframe(sliced_df)
        st.write(f"Showing rows {int(start)} to {int(end)}")
    except Exception as e:
        st.error(f"Error slicing data: {e}")

# Filtering
st.write("## Filter Data")
filter_col = st.selectbox("Select column to filter", df.columns, key="filter")
try:
    unique_vals = df[filter_col].dropna().unique()
    # Limit unique values to avoid memory issues
    if len(unique_vals) > 50:
        unique_vals = unique_vals[:50]
        st.warning(f"Showing first 50 unique values for {filter_col}")
    filter_val = st.selectbox("Select value", unique_vals)
    if st.button("Filter"):
        filtered_df = df[df[filter_col] == filter_val].copy()
        # Convert object columns to string for display
        for col in filtered_df.select_dtypes(include=['object']).columns:
            filtered_df[col] = filtered_df[col].astype(str)
        st.dataframe(filtered_df)
        st.write(f"Filtered dataset shape: {filtered_df.shape}")
except Exception as e:
    st.error(f"Error in filtering: {e}")

# Plotting
st.write("## Plot Relationships")
plot_type = st.selectbox("Select plot type", ["Bar", "Histogram", "Scatter"])
x_col = st.selectbox("X-axis", df.columns, key="x")
if plot_type != "Histogram":
    y_col = st.selectbox("Y-axis", df.columns, key="y")

if st.button("Plot"):
    try:
        if plot_type == "Bar":
            # For bar plots, limit the number of categories to avoid overcrowding
            if df[x_col].nunique() > 20:
                st.warning(f"Too many unique values in {x_col}. Showing top 20.")
                top_categories = df[x_col].value_counts().head(20).index
                plot_df = df[df[x_col].isin(top_categories)]
            else:
                plot_df = df
            fig = px.bar(plot_df, x=x_col, y=y_col)
            st.plotly_chart(fig, use_container_width=True)
        elif plot_type == "Histogram":
            fig = px.histogram(df, x=x_col, nbins=30)
            st.plotly_chart(fig, use_container_width=True)
        else:  # Scatter plot
            fig = px.scatter(df, x=x_col, y=y_col)
            st.plotly_chart(fig, use_container_width=True)
    except Exception as e:
        st.error(f"Error creating plot: {e}")
        st.write("Please check if the selected columns are appropriate for the chosen plot type.")

# Binary, text, and XML file operations
st.write("## File Operations")
file_op = st.selectbox("File operation", ["Read Binary", "Write Binary", "Append Text", "Write XML"])
if file_op == "Read Binary":
    try:
        with open("data.bin", "rb") as f:
            data = f.read()
        st.success("Read binary file successfully.")
    except Exception as e:
        st.error(f"Error: {e}")
elif file_op == "Write Binary":
    try:
        df.head().to_csv("data.csv", index=False)
        with open("data.csv", "rb") as f_in, open("data.bin", "wb") as f_out:
            f_out.write(f_in.read())
        st.success("Wrote binary file successfully.")
    except Exception as e:
        st.error(f"Error: {e}")
elif file_op == "Append Text":
    try:
        with open("data.txt", "a") as f:
            f.write(df.head().to_string())
        st.success("Appended to text file successfully.")
    except Exception as e:
        st.error(f"Error: {e}")
elif file_op == "Write XML":
    try:
        root = ET.Element("Data")
        for _, row in df.head().iterrows():
            item = ET.SubElement(root, "Row")
            for col in df.columns:
                # Clean column names for XML (remove spaces and special chars)
                clean_col = col.replace(" ", "_").replace("-", "_")
                child = ET.SubElement(item, clean_col)
                child.text = str(row[col]) if pd.notna(row[col]) else ""
        tree = ET.ElementTree(root)
        tree.write("data.xml", encoding='utf-8', xml_declaration=True)
        st.success("Wrote XML file successfully.")
    except Exception as e:
        st.error(f"Error: {e}")

"""