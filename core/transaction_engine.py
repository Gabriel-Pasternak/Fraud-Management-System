from datetime import datetime
import uuid
from typing import Dict, Any

class TransactionProcessor:
    def __init__(self, ml_engine, rules_engine, alert_system):
        self.ml_engine = ml_engine
        self.rules_engine = rules_engine
        self.alert_system = alert_system

    def process(self, transaction_data: Dict[str, Any]) -> Dict[str, Any]:
        """Process a transaction and check for fraud"""
        transaction_id = str(uuid.uuid4())
        
        # Enrich transaction data
        enriched_data = self._enrich_transaction(transaction_data)
        
        # Run ML detection
        ml_score = self.ml_engine.predict(enriched_data)
        
        # Apply rules
        rules_result = self.rules_engine.evaluate(enriched_data)
        
        # Combine results
        is_fraudulent = ml_score > 0.7 or rules_result['is_suspicious']
        
        if is_fraudulent:
            self.alert_system.create_alert(
                transaction_id=transaction_id,
                risk_score=ml_score,
                rules_triggered=rules_result['triggered_rules']
            )
        
        return {
            'transaction_id': transaction_id,
            'timestamp': datetime.now().isoformat(),
            'risk_score': ml_score,
            'is_fraudulent': is_fraudulent,
            'rules_triggered': rules_result['triggered_rules']
        }
    
    def _enrich_transaction(self, transaction_data: Dict[str, Any]) -> Dict[str, Any]:
        """Add additional context to transaction data"""
        enriched = transaction_data.copy()
        if 'timestamp' not in enriched:
            enriched['timestamp'] = datetime.now().isoformat()
        return enriched