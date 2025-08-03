import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set page configuration
st.set_page_config(
    page_title="Chest Pain Data Analysis",
    page_icon="❤️",
    layout="wide"
)

# Title and description
st.title("❤️ Chest Pain Data Analysis Dashboard")
st.markdown("---")
st.write("Welcome to the Chest Pain Data Analysis Dashboard. Explore various visualizations of healthcare data.")

# Sidebar
st.sidebar.header("📊 Plot Selection")
plot_type = st.sidebar.selectbox(
    "Select Plot Type",
    ['Violin Plot', 'Heat Map', 'Pair Plot', 'Swarm Plot', 'Distribution Plot']
)

# Data loading with error handling
@st.cache_data
def load_data():
    try:
        # Try to load the data - you may need to adjust the path
        df = pd.read_csv(r"D:\sir gen Ai\EDA\24th, 25th- Advanced EDA project\24th, 25th- Advanced EDA project\EDA- HEALTHCARE DOMAIN\heart.csv")
        return df
    except FileNotFoundError:
        st.error("❌ Heart data file not found. Please ensure 'heart.csv' is in the same directory.")
        st.info("💡 If you don't have the data file, you can download a sample heart disease dataset.")
        return None

df = load_data()

if df is not None:
    # Display basic data info
    st.subheader("📋 Dataset Overview")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Total Records", len(df))
    with col2:
        st.metric("Features", len(df.columns))
    with col3:
        st.metric("Target Distribution", f"{df['target'].value_counts().to_dict()}")
    
    # Show first few rows
    with st.expander("👀 View First 5 Rows"):
        st.dataframe(df.head())
    
    # Generate plots based on selection
    st.subheader(f"📈 {plot_type}")
    
    if plot_type == "Violin Plot":
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.violinplot(x='target', y='thalach', data=df, hue='target', ax=ax)
        ax.set_title('Violin Plot: Heart Rate vs Target')
        ax.set_xlabel('Target (0: No Disease, 1: Disease)')
        ax.set_ylabel('Maximum Heart Rate (thalach)')
        st.pyplot(fig)
        
    elif plot_type == "Heat Map":
        fig, ax = plt.subplots(figsize=(12, 10))
        correlation = df.corr()
        sns.heatmap(correlation, square=True, annot=True, fmt='.2f', cmap='coolwarm', ax=ax)
        ax.set_title('Correlation Heatmap')
        st.pyplot(fig)
        
    elif plot_type == "Pair Plot":
        st.info("Pair plot may take a moment to load...")
        num_vars = ['age', 'trestbps', 'chol', 'thalach', 'oldpeak', 'target']
        fig = sns.pairplot(df[num_vars], kind='scatter', diag_kind='hist', hue='target')
        st.pyplot(fig)
        
    elif plot_type == "Swarm Plot":
        fig, ax = plt.subplots(figsize=(12, 6))
        sns.swarmplot(x='thalach', data=df, hue='target', ax=ax)
        ax.set_title('Swarm Plot: Heart Rate Distribution')
        ax.set_xlabel('Maximum Heart Rate (thalach)')
        st.pyplot(fig)
        
    elif plot_type == "Distribution Plot":
        col1, col2 = st.columns(2)
        
        with col1:
            fig, ax = plt.subplots(figsize=(8, 6))
            sns.histplot(data=df, x='age', hue='target', bins=20, ax=ax)
            ax.set_title('Age Distribution by Target')
            st.pyplot(fig)
            
        with col2:
            fig, ax = plt.subplots(figsize=(8, 6))
            sns.histplot(data=df, x='thalach', hue='target', bins=20, ax=ax)
            ax.set_title('Heart Rate Distribution by Target')
            st.pyplot(fig)
    
    # Additional insights
    st.subheader("🔍 Data Insights")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("**Target Distribution:**")
        target_counts = df['target'].value_counts()
        st.write(f"- Disease Present (1): {target_counts.get(1, 0)}")
        st.write(f"- No Disease (0): {target_counts.get(0, 0)}")
        
    with col2:
        st.write("**Key Statistics:**")
        st.write(f"- Average Age: {df['age'].mean():.1f}")
        st.write(f"- Average Heart Rate: {df['thalach'].mean():.1f}")
        st.write(f"- Average Cholesterol: {df['chol'].mean():.1f}")

else:
    st.warning("⚠️ Please ensure you have the heart.csv file in the same directory as this script.")
    st.markdown("""
    ### Sample Data Structure
    The heart.csv file should contain columns like:
    - age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal, target
    """)

# Footer
st.markdown("---")
st.markdown("Made with ❤️ using Streamlit")