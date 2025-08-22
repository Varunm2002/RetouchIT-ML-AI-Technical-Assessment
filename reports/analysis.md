<<<<<<< HEAD
# Fraud Detection Business Report

## Key Decisions
-Preprocessing: Used `ColumnTransformer` for scaling numeric fields and one-hot encoding transaction type. Leakage column `isFlaggedFraud` removed.
-Class imbalance: Addressed in two ways:
  1. Algorithmic → `class_weight="balanced"`.
  2. Resampling → SMOTE oversampling (0.5 ratio).
-Model selection: Compared Logistic Regression, Random Forest, and XGBoost using **PR-AUC**.

## Results
- Logistic Regression → interpretable but lowest PR-AUC.
- Random Forest → good performance, robust but slower.
- XGBoost → best PR-AUC and best balance of precision vs recall.

## Explainability
- SHAP analysis shows transaction amount, oldbalanceOrg, and type are the top fraud drivers.

## Business Impact
- Precision is prioritized over recall: fewer false alarms (false positives are 5× more costly).
- Final pipeline = Preprocessing + SMOTE + XGBoost.
- Full runtime < 15 minutes → satisfies constraint.

**Conclusion**: XGBoost chosen as final model. Logistic Regression performed worst. Fraud detection now balances explainability, speed, and business cost sensitivity.
=======
# Fraud Detection Analysis Report

## Preprocessing
- Used ColumnTransformer with StandardScaler for numeric features and OneHotEncoder for categorical features
- Handled missing values using SimpleImputer with median strategy
- Removed isFlaggedFraud column to prevent data leakage and identifier columns (nameOrig, nameDest)

## Class Imbalance Handling
- Algorithmic approach: Used class_weight='balanced' in Logistic Regression and Random Forest
- Resampling approach: Applied **SMOTE (Synthetic Minority Over-sampling Technique) to generate synthetic fraud samples

## Models Compared
1. Logistic Regression with L2 regularization and balanced class weighting
2. Random Forest with balanced class weighting and 100 estimators  
3. XGBoost with scale_pos_weight for imbalance handling

## Results
- Best Model: XGBoost achieved 0.9998 PR-AUC
- Fraud Detection Rate: 99.73% of fraudulent transactions identified
- Business Impact: $43,730 total error cost with $12.6M savings vs blocking all transactions

## Key Insight
Used Precision-Recall AUC instead of accuracy because fraud detection requires measuring rare class detection capability, not overall accuracy which would be misleading with 0.2% fraud rate.
>>>>>>> 42e0a7c8a6362955cbb2a7fe8f7062c02c5ea26d
