# Fraud Management System

A real-time fraud detection system that combines machine learning and rule-based approaches to identify potentially fraudulent transactions.

## Features

- **Real-time Transaction Processing**: Analyze transactions as they occur
- **Machine Learning Detection**: Uses ensemble learning with Random Forest and Gradient Boosting
- **Rule-based Analysis**: Configurable rules for fraud pattern detection
- **Alert Management**: Real-time alert generation for suspicious activities
- **Case Management**: Track and manage fraud cases
- **Interactive Dashboard**: Monitor alerts and cases in real-time

## Tech Stack

- **Backend**: Python, Flask
- **ML/Data Science**: scikit-learn, pandas, numpy
- **Frontend**: HTML, JavaScript
- **Storage**: In-memory storage (for demo purposes)

## Project Structure

```
├── app.py                 # Main Flask application
├── core/                  # Core business logic
│   ├── ml/               # Machine learning components
│   │   ├── models.py     # ML model definitions
│   │   ├── training.py   # Model training logic
│   │   └── feature_engineering.py
│   ├── rules/            # Rule-based detection
│   │   └── patterns.py   # Fraud patterns
│   ├── alert_system.py   # Alert management
│   ├── rules_engine.py   # Rules processing
│   └── transaction_engine.py
├── data/                 # Data management
│   └── database.py      # Database operations
├── templates/           # Frontend templates
│   └── dashboard.html   # Main dashboard
└── utils/              # Utility functions
    └── logger.py       # Logging functionality
```

## Getting Started

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Start the application:
   ```bash
   python app.py
   ```

3. Access the dashboard at `http://localhost:5000`

## API Endpoints

- `POST /api/transaction`: Process a new transaction
- `GET /api/cases`: Retrieve fraud cases
- `GET /api/alerts`: Get fraud alerts

## Transaction Processing

The system processes transactions through multiple stages:

1. **Feature Engineering**: Extract relevant features from transaction data
2. **ML Detection**: Score transaction using ensemble models
3. **Rules Evaluation**: Check against predefined fraud patterns
4. **Alert Generation**: Create alerts for suspicious activities

## Machine Learning Models

- **Random Forest**: Primary classifier for fraud detection
- **Gradient Boosting**: Secondary classifier for enhanced accuracy
- **Ensemble Approach**: Weighted combination of both models

## Rule-based Detection

Monitors various patterns including:
- Large transactions
- High-velocity trading
- Suspicious timing
- Geographic anomalies
- High-risk merchants

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

MIT License - feel free to use this project for any purpose.
