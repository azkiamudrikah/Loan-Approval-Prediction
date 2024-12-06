import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Function to run EDA
def run_eda():
    st.header("Exploratory Data Analysis")

    # Load the dataset
    df = pd.read_csv("data_pinjaman.csv")

    # Filter data for different segments
    df_first_12 = df.iloc[:, :12]
    df_middle_12 = df.iloc[:, 12:24]
    df_last_12 = df.iloc[:, 24:36]
    df_categorical = df.select_dtypes(include='object')

    # Display descriptive statistics
    st.subheader("Descriptive Statistics (First 12 Columns)")
    st.write(df_first_12.describe())

    st.subheader("Descriptive Statistics (Middle 12 Columns)")
    st.write(df_middle_12.describe())

    st.subheader("Descriptive Statistics (Last 12 Columns)")
    st.write(df_last_12.describe())

    # Categorical plots
    st.subheader("Categorical Features")
    bar = sns.color_palette('pastel')
    fig, axes = plt.subplots(nrows=3, ncols=2, figsize=(12, 12))

    columns = ['LoanPurpose', 'HomeOwnershipStatus', 'MaritalStatus', 'EducationLevel', 'EmploymentStatus']
    titles = ['Loan Purpose', 'Home Ownership Status', 'Marital Status', 'Education Level', 'Employment Status']

    for i, ax in enumerate(axes.flat[:5]):
        df_categorical[columns[i]].value_counts().plot(kind='bar', ax=ax, color=bar, rot=0)
        ax.set_title(titles[i])
        ax.set_xlabel('')
        ax.set_ylabel('Frequency')

    fig.delaxes(axes[2, 1])
    plt.tight_layout()
    st.pyplot(fig)

    # Numerical plots
    st.subheader("Loan Amount vs Loan Duration")
    plt.figure(figsize=(8, 6))
    plt.scatter(df['LoanAmount'], df['LoanDuration'], alpha=0.5, c='blue')
    plt.title('Loan Amount vs Loan Duration')
    plt.xlabel('Loan Amount')
    plt.ylabel('Loan Duration')
    st.pyplot(plt)

    st.subheader("Debt to Income Ratio vs Payment History")
    plt.figure(figsize=(8, 6))
    plt.scatter(df['DebtToIncomeRatio'], df['PaymentHistory'], alpha=0.5, c='blue')
    plt.title('Debt to Income Ratio vs Payment History')
    plt.xlabel('Debt to Income Ratio')
    plt.ylabel('Payment History')
    st.pyplot(plt)
