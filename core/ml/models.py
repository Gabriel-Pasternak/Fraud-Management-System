from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.preprocessing import StandardScaler
import joblib
import os

class FraudDetectionModel:
    def __init__(self):
        self.rf_model = RandomForestClassifier(
            n_estimators=100,
            max_depth=10,
            min_samples_split=5,
            random_state=42,
            class_weight='balanced'  # Handle class imbalance
        )
        self.gb_model = GradientBoostingClassifier(
            n_estimators=100,
            learning_rate=0.1,
            max_depth=5,
            random_state=42
        )
        self.scaler = StandardScaler()
        
    def predict_proba(self, features):
        """Ensemble prediction combining RF and GB models"""
        # Ensure features is a list
        feature_list = list(features.values())
        
        # Scale features
        scaled_features = self.scaler.transform([feature_list])
        
        # Get predictions from both models
        rf_pred = self.rf_model.predict_proba(scaled_features)[0][1]
        gb_pred = self.gb_model.predict_proba(scaled_features)[0][1]
        
        # Weighted average of predictions
        return 0.6 * rf_pred + 0.4 * gb_pred
        
    def save_models(self, path):
        """Save models to disk"""
        if not os.path.exists(path):
            os.makedirs(path)
            
        joblib.dump(self.rf_model, f'{path}/rf_model.joblib')
        joblib.dump(self.gb_model, f'{path}/gb_model.joblib')
        joblib.dump(self.scaler, f'{path}/scaler.joblib')
        
    def load_models(self, path):
        """Load models from disk"""
        self.rf_model = joblib.load(f'{path}/rf_model.joblib')
        self.gb_model = joblib.load(f'{path}/gb_model.joblib')
        self.scaler = joblib.load(f'{path}/scaler.joblib')