"""
ABIDE Data Explorer - A Streamlit application for exploring ABIDE II Composite Phenotypic data.

This module provides a comprehensive GUI for data analysis and visualization.
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
import pickle as pk
import xml.etree.ElementTree as ET
import os
import pkg_resources


def load_sample_data():
    """Load sample ABIDE data or allow user to upload their own."""
    st.sidebar.header("Data Source")
    data_option = st.sidebar.radio(
        "Choose data source:",
        ["Upload your own CSV", "Use sample data (if available)"]
    )
    
    if data_option == "Upload your own CSV":
        uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type="csv")
        if uploaded_file is not None:
            return pd.read_csv(uploaded_file)
        else:
            st.warning("Please upload a CSV file to continue.")
            return None
    else:
        # Try to load sample data from package
        try:
            data_path = pkg_resources.resource_filename('abide_data_explorer', 'data/sample_data.csv')
            if os.path.exists(data_path):
                return pd.read_csv(data_path)
            else:
                st.error("Sample data not found. Please upload your own CSV file.")
                return None
        except:
            st.error("Sample data not available. Please upload your own CSV file.")
            return None


def prepare_dataframe(df):
    """Prepare DataFrame for Streamlit display to avoid Arrow conversion issues."""
    df = df.copy()
    
    # Convert problematic columns to appropriate types
    for col in df.columns:
        if df[col].dtype == 'object':
            # Keep string columns as strings
            df[col] = df[col].astype(str)
        elif df[col].dtype in ['int64', 'float64']:
            # Keep numeric columns but handle NaN values
            df[col] = pd.to_numeric(df[col], errors='coerce')
    
    return df


def create_display_dataframe(df):
    """Create a safe display version of DataFrame."""
    display_df = df.copy()
    for col in display_df.select_dtypes(include=['object']).columns:
        display_df[col] = display_df[col].astype(str)
    return display_df


def main():
    """Main application function."""
    st.set_page_config(
        page_title="ABIDE Data Explorer",
        page_icon="📊",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    st.title("📊 ABIDE Data Explorer")
    st.markdown("""
    A comprehensive tool for exploring and analyzing ABIDE II Composite Phenotypic data.
    Upload your CSV file or use sample data to get started.
    """)
    
    # Load data
    df = load_sample_data()
    if df is None:
        st.stop()
    
    # Prepare DataFrame
    df = prepare_dataframe(df)
    
    # Use Streamlit session state to persist DataFrame changes
    if 'df' not in st.session_state:
        st.session_state.df = df.copy()
    df = st.session_state.df
    
    # Create tabs for different functionalities
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "📋 Data Overview", 
        "🔧 Data Processing", 
        "📊 Visualization", 
        "💾 File Operations",
        "ℹ️ About"
    ])
    
    with tab1:
        data_overview_tab(df)
    
    with tab2:
        data_processing_tab(df)
    
    with tab3:
        visualization_tab(df)
    
    with tab4:
        file_operations_tab(df)
    
    with tab5:
        about_tab()


def data_overview_tab(df):
    """Data overview tab content."""
    st.header("Dataset Overview")
    
    # Dataset preview
    st.subheader("Dataset Preview")
    display_df = create_display_dataframe(df)
    st.dataframe(display_df.head(10), use_container_width=True)
    
    # Basic statistics
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Rows", df.shape[0])
    with col2:
        st.metric("Columns", df.shape[1])
    with col3:
        st.metric("Memory Usage", f"{df.memory_usage(deep=True).sum() / 1024:.1f} KB")
    
    # Summary statistics
    st.subheader("Summary Statistics")
    try:
        summary_df = df.describe(include='all')
        # Convert summary to string to avoid Arrow issues
        for col in summary_df.select_dtypes(include=['object']).columns:
            summary_df[col] = summary_df[col].astype(str)
        st.dataframe(summary_df, use_container_width=True)
    except Exception as e:
        st.error(f"Error displaying summary statistics: {e}")
        # Fallback: show basic info
        st.write("**Dataset Shape:**", df.shape)
        st.write("**Column Names:**", df.columns.tolist())
        st.write("**Data Types:**")
        st.write(df.dtypes)
    
    # Missing values analysis
    st.subheader("Missing Values Analysis")
    missing_data = df.isnull().sum()
    missing_data = missing_data[missing_data > 0].sort_values(ascending=False)
    if len(missing_data) > 0:
        st.write("Columns with missing values:")
        st.dataframe(missing_data.to_frame('Missing Count'), use_container_width=True)
    else:
        st.success("No missing values found in the dataset!")


def data_processing_tab(df):
    """Data processing tab content."""
    st.header("Data Processing")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Data type conversion
        st.subheader("Convert Column Data Type")
        col_to_convert = st.selectbox("Select column to convert", df.columns)
        dtype = st.selectbox("Select new data type", ["int", "float", "str"])
        if st.button("Convert", key="convert_btn"):
            try:
                if dtype == "int":
                    st.session_state.df[col_to_convert] = st.session_state.df[col_to_convert].astype(int)
                elif dtype == "float":
                    st.session_state.df[col_to_convert] = st.session_state.df[col_to_convert].astype(float)
                else:
                    st.session_state.df[col_to_convert] = st.session_state.df[col_to_convert].astype(str)
                st.success(f"Converted {col_to_convert} to {dtype}")
                st.rerun()
            except Exception as e:
                st.error(f"Error: {e}")
        
        # Sorting
        st.subheader("Sort Data")
        sort_col = st.selectbox("Select column to sort", df.columns, key="sort")
        sort_order = st.radio("Sort order", ["Ascending", "Descending"])
        if st.button("Sort", key="sort_btn"):
            try:
                ascending = sort_order == "Ascending"
                st.session_state.df = st.session_state.df.sort_values(by=sort_col, ascending=ascending)
                st.success(f"Data sorted by {sort_col} in {sort_order.lower()} order")
                st.rerun()
            except Exception as e:
                st.error(f"Error sorting data: {e}")
    
    with col2:
        # Grouping
        st.subheader("Group By Analysis")
        group_col = st.selectbox("Select column to group by", df.columns, key="group")
        agg_func = st.selectbox("Aggregation function", ["mean", "sum", "count", "std"])
        if st.button("Group", key="group_btn"):
            try:
                if agg_func == "mean":
                    result = df.groupby(group_col).mean(numeric_only=True)
                elif agg_func == "sum":
                    result = df.groupby(group_col).sum(numeric_only=True)
                elif agg_func == "std":
                    result = df.groupby(group_col).std(numeric_only=True)
                else:
                    result = df.groupby(group_col).count()
                
                # Convert result for safe display
                result_display = result.copy()
                result_display = result_display.reset_index()
                for col in result_display.select_dtypes(include=['object']).columns:
                    result_display[col] = result_display[col].astype(str)
                st.dataframe(result_display, use_container_width=True)
                st.success(f"Grouped by {group_col} using {agg_func}")
            except Exception as e:
                st.error(f"Error in grouping: {e}")
        
        # Filtering
        st.subheader("Filter Data")
        filter_col = st.selectbox("Select column to filter", df.columns, key="filter")
        try:
            unique_vals = df[filter_col].dropna().unique()
            # Limit unique values to avoid memory issues
            if len(unique_vals) > 50:
                unique_vals = unique_vals[:50]
                st.warning(f"Showing first 50 unique values for {filter_col}")
            filter_val = st.selectbox("Select value", unique_vals)
            if st.button("Filter", key="filter_btn"):
                filtered_df = df[df[filter_col] == filter_val].copy()
                display_filtered = create_display_dataframe(filtered_df)
                st.dataframe(display_filtered, use_container_width=True)
                st.info(f"Filtered dataset shape: {filtered_df.shape}")
        except Exception as e:
            st.error(f"Error in filtering: {e}")
    
    # Slicing
    st.subheader("Slice Data")
    col1, col2, col3 = st.columns(3)
    with col1:
        start = st.number_input("Start row", min_value=0, max_value=len(df)-1, value=0)
    with col2:
        end = st.number_input("End row", min_value=1, max_value=len(df), value=min(10, len(df)))
    with col3:
        if st.button("Slice", key="slice_btn"):
            try:
                sliced_df = df.iloc[int(start):int(end)].copy()
                display_sliced = create_display_dataframe(sliced_df)
                st.dataframe(display_sliced, use_container_width=True)
                st.info(f"Showing rows {int(start)} to {int(end)}")
            except Exception as e:
                st.error(f"Error slicing data: {e}")


def visualization_tab(df):
    """Visualization tab content."""
    st.header("Data Visualization")
    
    # Plot type selection
    plot_type = st.selectbox("Select plot type", ["Histogram", "Scatter Plot", "Bar Chart", "Box Plot", "Correlation Heatmap"])
    
    if plot_type == "Histogram":
        col = st.selectbox("Select column for histogram", df.select_dtypes(include=[np.number]).columns)
        if st.button("Create Histogram", key="hist_btn"):
            try:
                fig = px.histogram(df, x=col, nbins=30, title=f"Distribution of {col}")
                st.plotly_chart(fig, use_container_width=True)
            except Exception as e:
                st.error(f"Error creating histogram: {e}")
    
    elif plot_type == "Scatter Plot":
        col1, col2 = st.columns(2)
        with col1:
            x_col = st.selectbox("X-axis", df.select_dtypes(include=[np.number]).columns, key="scatter_x")
        with col2:
            y_col = st.selectbox("Y-axis", df.select_dtypes(include=[np.number]).columns, key="scatter_y")
        
        color_col = st.selectbox("Color by (optional)", ["None"] + list(df.columns))
        
        if st.button("Create Scatter Plot", key="scatter_btn"):
            try:
                color = None if color_col == "None" else color_col
                fig = px.scatter(df, x=x_col, y=y_col, color=color, title=f"{y_col} vs {x_col}")
                st.plotly_chart(fig, use_container_width=True)
            except Exception as e:
                st.error(f"Error creating scatter plot: {e}")
    
    elif plot_type == "Bar Chart":
        x_col = st.selectbox("X-axis (categorical)", df.columns, key="bar_x")
        y_col = st.selectbox("Y-axis (numerical)", df.select_dtypes(include=[np.number]).columns, key="bar_y")
        
        if st.button("Create Bar Chart", key="bar_btn"):
            try:
                # For bar plots, limit the number of categories to avoid overcrowding
                if df[x_col].nunique() > 20:
                    st.warning(f"Too many unique values in {x_col}. Showing top 20.")
                    top_categories = df[x_col].value_counts().head(20).index
                    plot_df = df[df[x_col].isin(top_categories)]
                else:
                    plot_df = df
                fig = px.bar(plot_df, x=x_col, y=y_col, title=f"{y_col} by {x_col}")
                st.plotly_chart(fig, use_container_width=True)
            except Exception as e:
                st.error(f"Error creating bar chart: {e}")
    
    elif plot_type == "Box Plot":
        col1, col2 = st.columns(2)
        with col1:
            y_col = st.selectbox("Y-axis (numerical)", df.select_dtypes(include=[np.number]).columns, key="box_y")
        with col2:
            x_col = st.selectbox("X-axis (categorical, optional)", ["None"] + list(df.columns), key="box_x")
        
        if st.button("Create Box Plot", key="box_btn"):
            try:
                x = None if x_col == "None" else x_col
                fig = px.box(df, x=x, y=y_col, title=f"Box Plot of {y_col}")
                st.plotly_chart(fig, use_container_width=True)
            except Exception as e:
                st.error(f"Error creating box plot: {e}")
    
    elif plot_type == "Correlation Heatmap":
        if st.button("Create Correlation Heatmap", key="corr_btn"):
            try:
                numeric_df = df.select_dtypes(include=[np.number])
                if numeric_df.empty:
                    st.error("No numeric columns found for correlation analysis.")
                else:
                    corr_matrix = numeric_df.corr()
                    fig = px.imshow(corr_matrix, 
                                  color_continuous_scale='RdBu',
                                  title="Correlation Heatmap",
                                  aspect="auto")
                    st.plotly_chart(fig, use_container_width=True)
            except Exception as e:
                st.error(f"Error creating correlation heatmap: {e}")


def file_operations_tab(df):
    """File operations tab content."""
    st.header("File Operations")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Export Data")
        export_format = st.selectbox("Select export format", ["CSV", "JSON", "Excel", "Pickle"])
        
        if st.button("Export", key="export_btn"):
            try:
                if export_format == "CSV":
                    df.to_csv("exported_data.csv", index=False)
                    st.success("Data exported as CSV successfully!")
                elif export_format == "JSON":
                    df.to_json("exported_data.json", orient='records', indent=2)
                    st.success("Data exported as JSON successfully!")
                elif export_format == "Excel":
                    df.to_excel("exported_data.xlsx", index=False)
                    st.success("Data exported as Excel successfully!")
                elif export_format == "Pickle":
                    df.to_pickle("exported_data.pkl")
                    st.success("Data exported as Pickle successfully!")
            except Exception as e:
                st.error(f"Export error: {e}")
    
    with col2:
        st.subheader("File Operations")
        file_op = st.selectbox("File operation", ["Write Binary", "Append Text", "Write XML"])
        
        if st.button("Execute", key="file_op_btn"):
            try:
                if file_op == "Write Binary":
                    df.head().to_csv("data.csv", index=False)
                    with open("data.csv", "rb") as f_in, open("data.bin", "wb") as f_out:
                        f_out.write(f_in.read())
                    st.success("Wrote binary file successfully.")
                
                elif file_op == "Append Text":
                    with open("data.txt", "a", encoding='utf-8') as f:
                        f.write("\n" + "="*50 + "\n")
                        f.write("Data Export - " + pd.Timestamp.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
                        f.write("="*50 + "\n")
                        f.write(df.head().to_string())
                        f.write("\n")
                    st.success("Appended to text file successfully.")
                
                elif file_op == "Write XML":
                    root = ET.Element("Data")
                    for _, row in df.head().iterrows():
                        item = ET.SubElement(root, "Row")
                        for col in df.columns:
                            # Clean column names for XML (remove spaces and special chars)
                            clean_col = col.replace(" ", "_").replace("-", "_").replace("(", "").replace(")", "")
                            child = ET.SubElement(item, clean_col)
                            child.text = str(row[col]) if pd.notna(row[col]) else ""
                    tree = ET.ElementTree(root)
                    tree.write("data.xml", encoding='utf-8', xml_declaration=True)
                    st.success("Wrote XML file successfully.")
                    
            except Exception as e:
                st.error(f"Error: {e}")


def about_tab():
    """About tab content."""
    st.header("About ABIDE Data Explorer")
    
    st.markdown("""
    ### Overview
    The ABIDE Data Explorer is a comprehensive Streamlit application designed for exploring and analyzing 
    ABIDE II (Autism Brain Imaging Data Exchange) Composite Phenotypic data.
    
    ### Features
    - **Data Overview**: View dataset statistics, missing values analysis, and basic information
    - **Data Processing**: Sort, filter, group, slice data, and convert data types
    - **Visualization**: Create various plots including histograms, scatter plots, bar charts, box plots, and correlation heatmaps
    - **File Operations**: Export data in multiple formats (CSV, JSON, Excel, Pickle) and perform file operations
    
    ### Requirements
    - Python 3.7+
    - Streamlit
    - Pandas
    - NumPy
    - Plotly
    - Matplotlib
    
    ### Installation
    ```bash
    pip install abide-data-explorer
    ```
    
    ### Usage
    ```bash
    abide-data-explorer
    ```
    
    ### Data Requirements
    The application works with CSV files. For ABIDE II data, ensure your CSV contains the standard phenotypic columns.
    
    ### Version
    1.0.0
    
    ### Author
    Developed for data exploration and analysis tasks.
    """)


if __name__ == "__main__":
    main()


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