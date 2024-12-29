from datetime import datetime, timedelta
from core.rules.patterns import FraudPatterns

class RulesEngine:
    def __init__(self):
        self.patterns = FraudPatterns()
        self.rules = [
            self._check_amount_patterns,
            self._check_velocity_patterns,
            self._check_location_patterns,
            self._check_high_risk_merchant,
            self._check_time_patterns
        ]
    
    def evaluate(self, transaction_data, historical_transactions=None):
        """Evaluate transaction against all rules"""
        triggered_rules = []
        
        for rule in self.rules:
            patterns = rule(transaction_data, historical_transactions)
            triggered_rules.extend(patterns)
        
        return {
            'is_suspicious': len(triggered_rules) > 0,
            'triggered_rules': triggered_rules
        }
    
    def _check_amount_patterns(self, transaction_data, _):
        """Check amount-related patterns"""
        amount = float(transaction_data.get('amount', 0))
        return self.patterns.check_amount_pattern(amount)
    
    def _check_velocity_patterns(self, _, historical_transactions):
        """Check velocity-related patterns"""
        if historical_transactions:
            return self.patterns.check_velocity_pattern(historical_transactions)
        return []
    
    def _check_location_patterns(self, _, historical_transactions):
        """Check location-related patterns"""
        if historical_transactions and len(historical_transactions) >= 2:
            return self.patterns.check_location_pattern(historical_transactions)
        return []
    
    def _check_high_risk_merchant(self, transaction_data, _):
        """Check if merchant is high-risk"""
        high_risk_categories = {
            'gambling', 'cryptocurrency', 'money_transfer',
            'adult_entertainment', 'high_value_goods'
        }
        merchant_category = transaction_data.get('merchant_category', '')
        return ['high_risk_merchant'] if merchant_category in high_risk_categories else []
    
    def _check_time_patterns(self, transaction_data, _):
        """Check time-based patterns"""
        patterns = []
        timestamp = transaction_data.get('timestamp')
        if timestamp:
            hour = datetime.fromisoformat(timestamp).hour
            if hour >= 1 and hour <= 4:
                patterns.append('late_night_transaction')
        return patterns