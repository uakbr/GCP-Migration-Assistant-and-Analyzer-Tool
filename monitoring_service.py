import time
import logging
from threading import Thread

class MigrationMonitoringService:
    def __init__(self):
        self._running = False
        self._logs = []
        self.logger = logging.getLogger('MigrationMonitoringService')
        self.logger.setLevel(logging.INFO)
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def start_monitoring(self):
        self._running = True
        self.logger.info("Migration monitoring started.")
        self._monitor_thread = Thread(target=self._monitor_migration)
        self._monitor_thread.start()

    def _monitor_migration(self):
        while self._running:
            # Simulate checking the migration status
            # In a real-world scenario, this would involve API calls to check the status of resources
            # and other relevant metrics.
            time.sleep(5)  # Polling interval
            self.logger.info("Checking migration status...")
            # Here you would include the logic to check the migration status and log relevant information.
            # For example:
            # status = check_migration_status()
            # self.logger.info(f"Current migration status: {status}")
            # self._logs.append(status)
            # You could also implement error checking and logging:
            # if status == 'error':
            #     self.logger.error("Error detected during migration!")
            #     self._running = False  # Stop monitoring if a critical error is detected

    def stop_monitoring(self):
        self._running = False
        self._monitor_thread.join()
        self.logger.info("Migration monitoring stopped.")

    def get_logs(self):
        return self._logs

# Example usage:
if __name__ == "__main__":
    monitoring_service = MigrationMonitoringService()
    try:
        monitoring_service.start_monitoring()
        # Perform migration tasks...
        # For demonstration purposes, we'll just sleep for a short time
        time.sleep(20)
    finally:
        monitoring_service.stop_monitoring()
        logs = monitoring_service.get_logs()
        for log in logs:
            print(log)
