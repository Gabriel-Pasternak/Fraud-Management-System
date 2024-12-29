from datetime import datetime, timedelta

class FraudPatterns:
    def __init__(self):
        self.velocity_window = timedelta(hours=24)
        self.amount_threshold = 5000
        self.velocity_threshold = 5
        
    def check_amount_pattern(self, amount):
        """Check for suspicious amount patterns"""
        patterns = []
        
        if amount > self.amount_threshold:
            patterns.append('large_transaction')
            
        if amount == round(amount, -2):  # Round numbers
            patterns.append('round_amount')
            
        if str(amount).endswith('99'):  # Testing amounts
            patterns.append('test_amount')
            
        return patterns
    
    def check_velocity_pattern(self, transactions):
        """Check transaction velocity patterns"""
        patterns = []
        recent_count = sum(1 for t in transactions 
                          if datetime.now() - datetime.fromisoformat(t['timestamp']) <= self.velocity_window)
        
        if recent_count > self.velocity_threshold:
            patterns.append('high_velocity')
            
        return patterns
    
    def check_location_pattern(self, transactions):
        """Check for suspicious location patterns"""
        patterns = []
        
        if len(transactions) >= 2:
            latest = transactions[-1]
            previous = transactions[-2]
            
            # Impossible travel
            if (latest['location'] != previous['location'] and 
                datetime.fromisoformat(latest['timestamp']) - 
                datetime.fromisoformat(previous['timestamp']) < timedelta(hours=2)):
                patterns.append('impossible_travel')
                
        return patterns