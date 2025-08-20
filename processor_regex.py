import re
import warnings
warnings.filterwarnings('ignore')
def classify_with_regex(log_message):
    regex_patterns = {
        r"User User\d+ logged (in|out).": "User Action",
        r"Backup (started|ended) at .*": "System Notification",
        r"Backup completed successfully.": "System Notification",
        r"System updated to version .*": "System Notification",
        r"File .* uploaded successfully by user .*": "System Notification",
        r"Disk cleanup completed successfully.": "System Notification",
        r"System reboot initiated by user .*": "System Notification",
        r"Account with ID .* created by .*": "User Action"
    }
    for pattern, label in regex_patterns.items():
        if re.search(pattern, log_message,re.IGNORECASE):
            return label
    return None

if __name__ == "__main__" :
        # Example test cases for each regex
    test_cases = [
        "User User123 logged in.",
        "User User45 logged out.",
        "Backup started at 2025-08-15 14:32:10",
        "Backup ended at 2025-08-15 15:00:00",
        "Backup completed successfully.",
        "System updated to version 3.2.1",
        "File report.pdf uploaded successfully by user JohnDoe",
        "Disk cleanup completed successfully.",
        "System reboot initiated by user Admin",
        "Account with ID 987654 created by User45"
    ]

    # Run test cases
    for log in test_cases:
        print(classify_with_regex(log))