from flask import Flask, jsonify, request, render_template
import json
from datetime import datetime
import uuid
from core.transaction_engine import TransactionProcessor
from core.ml_engine import MLDetectionEngine
from core.rules_engine import RulesEngine
from core.alert_system import AlertSystem
from data.database import Database
from utils.logger import Logger

app = Flask(__name__)
logger = Logger()

# Initialize core components
db = Database()
ml_engine = MLDetectionEngine()
rules_engine = RulesEngine()
alert_system = AlertSystem()
transaction_processor = TransactionProcessor(ml_engine, rules_engine, alert_system)

@app.route('/')
def dashboard():
    return render_template('dashboard.html')

@app.route('/api/transaction', methods=['POST'])
def process_transaction():
    try:
        data = request.get_json()
        result = transaction_processor.process(data)
        return jsonify(result), 200
    except Exception as e:
        logger.error(f"Transaction processing error: {str(e)}")
        return jsonify({"error": "Transaction processing failed"}), 500

@app.route('/api/cases', methods=['GET'])
def get_cases():
    try:
        cases = db.get_cases()
        return jsonify(cases), 200
    except Exception as e:
        logger.error(f"Error fetching cases: {str(e)}")
        return jsonify({"error": "Failed to fetch cases"}), 500

@app.route('/api/alerts', methods=['GET'])
def get_alerts():
    try:
        alerts = alert_system.get_alerts()
        return jsonify(alerts), 200
    except Exception as e:
        logger.error(f"Error fetching alerts: {str(e)}")
        return jsonify({"error": "Failed to fetch alerts"}), 500

if __name__ == '__main__':
    app.run(debug=True)