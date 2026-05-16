🫀 Heart Disease Prediction Using Patient Health Data

Predicting the presence or absence of heart disease using clinical attributes from the Cleveland Heart Disease Dataset.


👥 Team Members
Name
1. Meera G
2. Sanika J R
3. Anamika Ponnu

This project uses Machine Learning to predict the likelihood of heart disease in patients based on medical clinical records.

##  Project Overview
Heart disease is one of the leading causes of mortality worldwide. Early and accurate prediction can significantly improve patient outcomes. This project applies machine learning classification techniques to the Cleveland Heart Disease Dataset to predict whether a patient has heart disease based on 13 clinical attributes.

##  Dataset

Source: UCI Machine Learning Repository – Cleveland Heart Disease Dataset
Instances: 303 patients
Target Variable: target — 0 (No Disease) / 1 (Disease Present)

##  Tech Stack
  Language:Python
  Libraries: Pandas, NumPy, Scikit-Learn, Matplotlib, Seaborn
  Environment: Google Colab / Jupyter Notebook

##  Workflow
1. Data Preprocessing: Handled missing values and standardized medical metrics.
2. Feature Engineering: Used Mutual Information scores to select the most impactful health indicators.
3. Model Building: Trained Gradient Boosting and K-Nearest Neighbors (KNN).
4. Evaluation: Achieved high performance as seen in the Confusion Matrix and ROC Curves below.

## Deployment
- Deployed using Streamlit Community Cloud - https://heart-disease-prediction-kepbwdmtxra68hh9gstb6o.streamlit.app/
- App accepts patient inputs (manual entry)
- Displays prediction (Heart Disease: Yes/No) with probability score
- Shows SHAP waterfall plot for individual prediction explanation
- Handles invalid inputs gracefully with clear error messages

##  Key Results
  Best Model: Logistic Regression stands more suitable that gradient boosting.
  Accuracy: 90%
  ROC-AUC: 93.4\%

  

