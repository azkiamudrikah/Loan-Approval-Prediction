import streamlit as st
import pickle
import pandas as pd

# Load the trained model
with open('best_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Function to run prediction
def run_prediction():
    st.header("Loan Prediction")

    # Input form for user data
    loan_amount = st.number_input('Loan Amount', min_value=1000, max_value=100000, step=1000)
    loan_duration = st.number_input('Loan Duration (in months)', min_value=1, max_value=60, step=1)
    debt_to_income_ratio = st.number_input('Debt to Income Ratio', min_value=0.0, max_value=1.0, step=0.01)
    payment_history = st.selectbox('Payment History', ['Good', 'Bad', 'Average'])
    loan_purpose = st.selectbox('Loan Purpose', ['Home Improvement', 'Debt Consolidation', 'Business'])
    home_ownership_status = st.selectbox('Home Ownership Status', ['Own', 'Rent', 'Mortgage'])
    marital_status = st.selectbox('Marital Status', ['Single', 'Married', 'Divorced'])
    education_level = st.selectbox('Education Level', ['High School', 'Bachelor', 'Master', 'PhD'])
    employment_status = st.selectbox('Employment Status', ['Employed', 'Self-employed', 'Unemployed'])

    # Additional missing columns input form
    checking_account_balance = st.number_input('Checking Account Balance', min_value=0, max_value=100000, step=1000)
    length_of_credit_history = st.number_input('Length of Credit History (in months)', min_value=0, max_value=600, step=1)
    interest_rate = st.number_input('Interest Rate', min_value=0.0, max_value=50.0, step=0.1)
    total_debt_to_income_ratio = st.number_input('Total Debt to Income Ratio', min_value=0.0, max_value=1.0, step=0.01)
    experience = st.number_input('Experience (in years)', min_value=0, max_value=50, step=1)
    monthly_income = st.number_input('Monthly Income', min_value=0, max_value=100000, step=1000)
    annual_income = st.number_input('Annual Income', min_value=0, max_value=1000000, step=1000)
    net_worth = st.number_input('Net Worth', min_value=0, max_value=10000000, step=1000)
    bankruptcy_history = st.selectbox('Bankruptcy History', ['Yes', 'No'])
    number_of_dependents = st.number_input('Number of Dependents', min_value=0, max_value=10, step=1)
    base_interest_rate = st.number_input('Base Interest Rate', min_value=0.0, max_value=50.0, step=0.1)
    previous_loan_defaults = st.number_input('Previous Loan Defaults', min_value=0, max_value=10, step=1)
    age = st.number_input('Age', min_value=18, max_value=100, step=1)
    monthly_debt_payments = st.number_input('Monthly Debt Payments', min_value=0, max_value=100000, step=1000)
    total_assets = st.number_input('Total Assets', min_value=0, max_value=10000000, step=1000)
    risk_score = st.number_input('Risk Score', min_value=0, max_value=1000, step=1)
    monthly_loan_payment = st.number_input('Monthly Loan Payment', min_value=0, max_value=100000, step=1000)
    credit_score = st.number_input('Credit Score', min_value=300, max_value=850, step=1)

    # Prepare data for prediction
    input_data = pd.DataFrame({
        'loan_amount': [loan_amount],
        'loan_duration': [loan_duration],
        'DebtToIncomeRatio': [debt_to_income_ratio],
        'PaymentHistory': [payment_history],
        'LoanPurpose': [loan_purpose],
        'home_ownership_status': [home_ownership_status],
        'MaritalStatus': [marital_status],
        'education_level': [education_level],
        'EmploymentStatus': [employment_status],
        'checking_account_balance': [checking_account_balance],
        'length_of_credit_history': [length_of_credit_history],
        'interest_rate': [interest_rate],
        'total_debt_to_income_ratio': [total_debt_to_income_ratio],
        'experience': [experience],
        'monthly_income': [monthly_income],
        'annual_income': [annual_income],
        'net_worth': [net_worth],
        'bankruptcy_history': [bankruptcy_history],
        'number_of_dependents': [number_of_dependents],
        'base_interest_rate': [base_interest_rate],
        'previous_loan_defaults': [previous_loan_defaults],
        'age': [age],
        'monthly_debt_payments': [monthly_debt_payments],
        'total_assets': [total_assets],
        'risk_score': [risk_score],
        'monthly_loan_payment': [monthly_loan_payment],
        'credit_score': [credit_score]
    })
    # Convert categorical columns to match the model's expectations
    input_data['bankruptcy_history'] = input_data['bankruptcy_history'].map({'Yes': 1, 'No': 0})
    input_data['PaymentHistory'] = input_data['PaymentHistory'].map({'Good': 2, 'Average': 1, 'Bad': 0})
    input_data['home_ownership_status'] = input_data['home_ownership_status'].map({'Own': 2, 'Mortgage': 1, 'Rent': 0})
    input_data['LoanPurpose'] = input_data['LoanPurpose'].map({'Home Improvement': 2, 'Debt Consolidation': 1, 'Business': 0})
    input_data['MaritalStatus'] = input_data['MaritalStatus'].map({'Married': 2, 'Single': 1, 'Divorced': 0})
    input_data['education_level'] = input_data['education_level'].map({'PhD': 3, 'Master': 2, 'Bachelor': 1, 'High School': 0})
    input_data['EmploymentStatus'] = input_data['EmploymentStatus'].map({'Employed': 2, 'Self-employed': 1, 'Unemployed': 0})

    input_data = input_data.apply(pd.to_numeric, errors='coerce')

    # Ensure correct number of columns before making the prediction
    if st.button('Predict'):
        try:
            prediction = model.predict(input_data)
            st.session_state['prediction'] = prediction[0]
        except ValueError as e:
            st.error(f"Error during prediction: {e}")

    # Display prediction result if available
    if 'prediction' in st.session_state:
        st.write(f"The predicted loan status is: {st.session_state['prediction']}")