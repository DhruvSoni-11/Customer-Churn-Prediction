# Customer Churn Prediction

## About Dataset:
URL: https://www.kaggle.com/datasets/blastchar/telco-customer-churn

### Context
"Predict behavior to retain customers. You can analyze all relevant customer data and develop focused customer retention programs." [IBM Sample Data Sets]


## 📌 Project Overview  
This project predicts whether a customer will churn (leave the service) based on their demographic details, account information, and service usage. It helps businesses identify at-risk customers and take preventive actions.

---

## 🎯 Objective  
- Analyze customer behavior and churn patterns  
- Build machine learning models for prediction  
- Provide insights to improve customer retention  

---

## 🔍 Key Insights  
- Customers with month-to-month contracts are more likely to churn  
- Higher monthly charges increase churn probability  
- Customers with longer tenure are less likely to churn  
- Lack of services like online security and tech support increases churn  
- Fiber optic users have higher churn compared to DSL users  

---

## 🧾 Dataset Description  

Each row represents one customer.

- **CustomerID** – Unique customer identifier  
- **Gender** – Male or Female  
- **SeniorCitizen** – 0 = No, 1 = Yes  
- **Partner** – Has a partner or not  
- **Dependents** – Has dependents or not  
- **Tenure** – Number of months with the company  
- **PhoneService** – Has phone service or not  
- **MultipleLines** – Multiple phone lines or not  
- **InternetService** – DSL, Fiber optic, or No  
- **OnlineSecurity** – Security service status  
- **OnlineBackup** – Backup service status  
- **DeviceProtection** – Device protection plan  
- **TechSupport** – Technical support availability  
- **StreamingTV** – Streaming TV service  
- **StreamingMovies** – Streaming Movies service  
- **Contract** – Month-to-month, One year, Two year  
- **PaperlessBilling** – Billing method  
- **PaymentMethod** – Payment mode  
- **MonthlyCharges** – Monthly bill amount  
- **TotalCharges** – Total amount paid  
- **Churn** – Target variable (Yes/No)  

---

## ⚙️ Workflow  

1. **Data Collection**  
   - Used telecom customer dataset  

2. **Data Cleaning**  
   - Handled missing values  
   - Converted categorical data into numerical format  

3. **Exploratory Data Analysis (EDA)**  
   - Analyzed relationships between features and churn  
   - Identified key patterns  

4. **Feature Engineering**  
   - Encoded categorical variables  
   - Selected important features  

5. **Model Building**  
   - Logistic Regression  
   - Decision Tree  
   - Random Forest  

6. **Model Evaluation**  
   - Compared models using accuracy metrics  
   - Selected best-performing model  

7. **Deployment (Streamlit App)**  
   - Built interactive user interface  
   - Inputs: Tenure, Monthly Charges, Total Charges, Contract Type, Internet Service  
   - Output: Churn prediction  
   (7. not done till now)


---

## Tech Stack  
- Python  
- Pandas, NumPy  
- Matplotlib, Seaborn  
- Scikit-learn  
- Streamlit  
