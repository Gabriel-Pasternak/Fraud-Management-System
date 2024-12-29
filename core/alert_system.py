from datetime import datetime
import uuid

class AlertSystem:
    def __init__(self):
        self.alerts = []  # In-memory storage for demo
    
    def create_alert(self, transaction_id, risk_score, rules_triggered):
        """Create a new fraud alert"""
        alert = {
            'alert_id': str(uuid.uuid4()),
            'transaction_id': transaction_id,
            'timestamp': datetime.now().isoformat(),
            'risk_score': risk_score,
            'rules_triggered': rules_triggered,
            'status': 'NEW'
        }
        self.alerts.append(alert)
        return alert
    
    def get_alerts(self, status=None):
        """Retrieve alerts with optional status filter"""
        if status:
            return [alert for alert in self.alerts if alert['status'] == status]
        return self.alerts
    
    def update_alert_status(self, alert_id, new_status):
        """Update alert status"""
        for alert in self.alerts:
            if alert['alert_id'] == alert_id:
                alert['status'] = new_status
                alert['updated_at'] = datetime.now().isoformat()
                return alert
        return None