#PROJECT SUMMARY

## OVERVIEW
This project leverages Machine Learning to assist in the early detection of cardiovascular diseases.
By analyzing clinical parameters, the system provides a data-driven approach to identify high-risk patients, potentially aiding healthcare professionals in clinical decision-making.

## DATASET

-Source: Cleveland Heart Disease dataset (UCI Machine Learning Repository).
-Scale: 303 patient records with 14 key clinical features.
-Nature: Binary classification (0: Healthy, 1: Heart Disease presence).
-Data Quality: Validated for zero missing values and pre-processed for feature consistency.


## KEY CONTRIBUTIONS
- Feature Engineering: Correlation analysis and feature scaling to optimize model input.
- Advanced Data Balancing: Implemented SMOTE (Synthetic Minority Over-sampling Technique) to eliminate class bias, ensuring the model doesn't favor the majority class.
- Comparative Modeling: Evaluated multiple architectures including Logistic Regression, Decision Trees, and Random Forest to identify the most robust predictor.
-Diagnostic Visualization: Developed Confusion Matrices and ROC-AUC curves to visualize the trade-off between Sensitivity (catching all cases) and Specificity (reducing false alarms).

## CONCLUSION
The application of SMOTE was a turning point in this project, resolving the initial class imbalance and leading to a significant boost in the Recall score.
While Logistic Regression provided a strong baseline, the Random Forest ensemble showed superior performance in handling non-linear relationships within the medical data. 
The final model demonstrates that machine learning can achieve high diagnostic reliability, serving as an effective screening tool for heart disease.
