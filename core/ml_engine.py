from core.ml.feature_engineering import FeatureEngineer
from core.ml.models import FraudDetectionModel
from core.ml.training import ModelTrainer
import os

class MLDetectionEngine:
    def __init__(self):
        self.feature_engineer = FeatureEngineer()
        self.model = FraudDetectionModel()
        self.trainer = ModelTrainer(self.feature_engineer, self.model)
        
        # Initialize with sample data if no saved models exist
        self._initialize_models()
        
    def _initialize_models(self):
        """Initialize models with sample data if needed"""
        model_path = 'models'
        if not os.path.exists(f'{model_path}/scaler.joblib'):
            # Create sample training data
            sample_transactions = self._get_sample_transactions()
            self.trainer.train(sample_transactions)
            
            # Save initialized models
            os.makedirs(model_path, exist_ok=True)
            self.model.save_models(model_path)
        else:
            self.model.load_models(model_path)
    
    def _get_sample_transactions(self):
        """Generate sample transactions for initial training"""
        return [
            # Legitimate transactions
            {
                'amount': 100.0,
                'merchant_category': 'retail',
                'merchant_country': 'US',
                'payment_method': 'card',
                'timestamp': '2024-01-01T12:00:00',
                'is_fraud': 0
            },
            {
                'amount': 250.0,
                'merchant_category': 'restaurant',
                'merchant_country': 'US',
                'payment_method': 'card',
                'timestamp': '2024-01-01T13:00:00',
                'is_fraud': 0
            },
            {
                'amount': 1000.0,
                'merchant_category': 'electronics',
                'merchant_country': 'UK',
                'payment_method': 'card',
                'timestamp': '2024-01-01T14:00:00',
                'is_fraud': 0
            },
            # Fraudulent transactions
            {
                'amount': 5000.0,
                'merchant_category': 'gambling',
                'merchant_country': 'XX',
                'payment_method': 'crypto',
                'timestamp': '2024-01-01T02:00:00',
                'is_fraud': 1
            },
            {
                'amount': 3000.0,
                'merchant_category': 'money_transfer',
                'merchant_country': 'YY',
                'payment_method': 'wire',
                'timestamp': '2024-01-01T03:00:00',
                'is_fraud': 1
            },
            {
                'amount': 7500.0,
                'merchant_category': 'jewelry',
                'merchant_country': 'ZZ',
                'payment_method': 'crypto',
                'timestamp': '2024-01-01T04:00:00',
                'is_fraud': 1
            }
        ]
    
    def predict(self, transaction_data):
        """Predict fraud probability for a transaction"""
        features = self.feature_engineer.transform(transaction_data)
        return self.model.predict_proba(features)
    
    def train(self, transactions):
        """Train models with new data"""
        return self.trainer.train(transactions)
    
    def save_models(self, path='models'):
        """Save trained models"""
        os.makedirs(path, exist_ok=True)
        self.model.save_models(path)