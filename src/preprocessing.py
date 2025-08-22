<<<<<<< HEAD
import pandas as pd
=======
# src/preprocessing.py
import pandas as pd
import numpy as np
>>>>>>> 42e0a7c8a6362955cbb2a7fe8f7062c02c5ea26d
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
<<<<<<< HEAD

def read_transactions(csv_path: str):
    """Import transaction data, remove unwanted columns, and separate features & labels."""
    data = pd.read_csv(csv_path)  

    if "isFlaggedFraud" in data.columns:
        data = data.drop(columns=["isFlaggedFraud"])

    features = data.drop(columns=["isFraud"])
    target = data["isFraud"]
    return features, target

def create_feature_processor():
    """Construct a pipeline for processing numeric and categorical variables."""
    num_cols = ["amount", "oldbalanceOrg", "newbalanceOrig",
                "oldbalanceDest", "newbalanceDest"]
    cat_cols = ["type"]

    num_pipeline = Pipeline(steps=[
        ("imputer", SimpleImputer(strategy="median")),
        ("scaler", StandardScaler())
    ])

    cat_pipeline = Pipeline(steps=[
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("onehot", OneHotEncoder(handle_unknown="ignore"))
    ])

    processor = ColumnTransformer(transformers=[
        ("numerical", num_pipeline, num_cols),
        ("categorical", cat_pipeline, cat_cols)
    ])
    return processor

def prepare_data(csv_path: str):
    """Load dataset and return processed features, target labels, and preprocessing object."""
    features, target = read_transactions(csv_path)
    processor = create_feature_processor()
    return features, target, processor
=======
from imblearn.over_sampling import SMOTE
from imblearn.under_sampling import NearMiss

def create_preprocessor():
    """
    Create a preprocessing pipeline
    """
    # Define numeric and categorical features
    numeric_features = ['amount', 'oldbalanceOrg', 'newbalanceOrig', 
                       'oldbalanceDest', 'newbalanceDest']
    categorical_features = ['type']
    
    # Create preprocessing transformers
    numeric_transformer = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='median')),
        ('scaler', StandardScaler())
    ])
    
    categorical_transformer = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='constant', fill_value='missing')),
        ('onehot', OneHotEncoder(handle_unknown='ignore', sparse_output=False))
    ])
    
    # Create column transformer
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', numeric_transformer, numeric_features),
            ('cat', categorical_transformer, categorical_features)
        ])
    
    return preprocessor

def load_and_preprocess_data(filepath, sampling_method=None):
    """
    Load and preprocess the transaction data
    """
    # Load data
    df = pd.read_csv(filepath)
    
    # Remove leakage columns and identifiers
    df = df.drop(['isFlaggedFraud', 'nameOrig', 'nameDest'], axis=1, errors='ignore')
    
    # Separate features and target
    X = df.drop('isFraud', axis=1)
    y = df['isFraud']
    
    # Create and fit preprocessor
    preprocessor = create_preprocessor()
    X_processed = preprocessor.fit_transform(X)
    
    # Apply resampling if specified
    if sampling_method == 'smote':
        sampler = SMOTE(random_state=42)
        X_resampled, y_resampled = sampler.fit_resample(X_processed, y)
        return X_resampled, y_resampled, preprocessor
    elif sampling_method == 'nearmiss':
        sampler = NearMiss(version=2, n_neighbors=3)
        X_resampled, y_resampled = sampler.fit_resample(X_processed, y)
        return X_resampled, y_resampled, preprocessor
    
    return X_processed, y, preprocessor
>>>>>>> 42e0a7c8a6362955cbb2a7fe8f7062c02c5ea26d
