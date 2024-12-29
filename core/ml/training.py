import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

class ModelTrainer:
    def __init__(self, feature_engineer, model):
        self.feature_engineer = feature_engineer
        self.model = model
        
    def prepare_training_data(self, transactions):
        """Prepare data for training"""
        features = []
        labels = []
        
        for transaction in transactions:
            features.append(self.feature_engineer.transform(transaction))
            labels.append(transaction.get('is_fraud', 0))
            
        return features, labels
    
    def train(self, transactions):
        """Train the ML models"""
        features, labels = self.prepare_training_data(transactions)
        
        # Convert to numpy arrays
        X = np.array([list(f.values()) for f in features])
        y = np.array(labels)
        
        # Fit the scaler
        self.model.scaler.fit(X)
        X_scaled = self.model.scaler.transform(X)
        
        # Split data
        X_train, X_test, y_train, y_test = train_test_split(
            X_scaled, y, test_size=0.2, random_state=42
        )
        
        # Train models
        self.model.rf_model.fit(X_train, y_train)
        self.model.gb_model.fit(X_train, y_train)
        
        return {
            'rf_score': self.model.rf_model.score(X_test, y_test),
            'gb_score': self.model.gb_model.score(X_test, y_test)
        }