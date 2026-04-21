
# Heart Disease Prediction Project

This project uses Machine Learning to predict the likelihood of heart disease in patients based on medical clinical records.

##  Project Overview
The goal is to build a high-accuracy classifier using the Cleveland Heart Disease dataset. We performed extensive feature engineering and compared multiple models, including KNN and Gradient Boosting, to find the most reliable diagnostic tool.

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

  

