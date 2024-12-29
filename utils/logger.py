from datetime import datetime

class Logger:
    def __init__(self):
        self.log_file = "fraud_system.log"
    
    def _log(self, level, message):
        timestamp = datetime.now().isoformat()
        log_entry = f"[{timestamp}] {level}: {message}\n"
        print(log_entry)  # For demo, just print to console
    
    def info(self, message):
        self._log("INFO", message)
    
    def error(self, message):
        self._log("ERROR", message)
    
    def warning(self, message):
        self._log("WARNING", message)
    
    def debug(self, message):
        self._log("DEBUG", message)