import json
from datetime import datetime
import uuid

class Database:
    def __init__(self):
        # In-memory storage for demo
        self.transactions = []
        self.cases = []
        self.alerts = []
    
    def store_transaction(self, transaction_data):
        """Store transaction data"""
        transaction = {
            'id': str(uuid.uuid4()),
            'timestamp': datetime.now().isoformat(),
            **transaction_data
        }
        self.transactions.append(transaction)
        return transaction
    
    def create_case(self, alert_id, transaction_id):
        """Create a fraud case"""
        case = {
            'case_id': str(uuid.uuid4()),
            'alert_id': alert_id,
            'transaction_id': transaction_id,
            'status': 'OPEN',
            'created_at': datetime.now().isoformat(),
            'updated_at': datetime.now().isoformat()
        }
        self.cases.append(case)
        return case
    
    def get_cases(self, status=None):
        """Retrieve cases with optional status filter"""
        if status:
            return [case for case in self.cases if case['status'] == status]
        return self.cases