import requests
import time

def check_application_status(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return "up"  # Application is functioning correctly
        else:
            return "down"  # Application is unavailable or not responding
    except requests.ConnectionError:
        return "down"  # Application is unavailable or not responding

if __name__ == "__main__":
    application_url =    "https://www.flipkart.com"  # Replace with the URL of your application
    
    while True:
        status = check_application_status(application_url)
        print(f"Application status: {status}")
        time.sleep(60)  # Check application status every 60 seconds
