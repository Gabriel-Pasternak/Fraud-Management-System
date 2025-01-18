import pandas as pd
import numpy as np
from datetime import datetime

class FeatureEngineer:
       
    def transform(self, transaction_data):
        """Transform raw transaction data into ML features"""
        features = {}
        
        # Amount-based features
        features['amount'] = float(transaction_data.get('amount', 0))
        features['amount_log'] = np.log1p(features['amount'])
        
        # Time-based features
        timestamp = datetime.fromisoformat(transaction_data.get('timestamp', datetime.now().isoformat()))
        features['hour'] = timestamp.hour
        features['day_of_week'] = timestamp.weekday()
        features['is_weekend'] = 1 if features['day_of_week'] >= 5 else 0
        features['is_night'] = 1 if features['hour'] >= 23 or features['hour'] <= 4 else 0
        
        # Location-based features
        features['high_risk_country'] = 1 if transaction_data.get('merchant_country') in self.get_high_risk_countries() else 0
        
        # Categorical features (one-hot encoded)
        for feature in self.categorical_features:
            value = transaction_data.get(feature, 'unknown')
            features[f'{feature}_{value}'] = 1
            
        return features
    
    @staticmethod
    def get_high_risk_countries():
        """List of high-risk countries based on fraud patterns"""
        return {'XX', 'YY', 'ZZ'}  # Replace with actual high-risk countries
