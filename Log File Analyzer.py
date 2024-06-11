import re
from collections import Counter

def analyze_logs(log_file):
    # Initialize counters and lists to store data
    error_404_count = 0
    requested_pages = []
    ip_address_requests = Counter()

    # Regular expression patterns to match relevant log entries
    error_404_pattern = r'\b404\b'
    requested_page_pattern = r'GET\s+([^\s]+)'
    ip_address_pattern = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'

    # Open and read the log file
    with open(log_file, 'r') as file:
        for line in file:
            # Check for 404 errors
            if re.search(error_404_pattern, line):
                error_404_count += 1
            
            # Extract requested pages
            page_match = re.search(requested_page_pattern, line)
            if page_match:
                requested_page = page_match.group(1)
                requested_pages.append(requested_page)

            # Extract IP addresses
            ip_match = re.search(ip_address_pattern, line)
            if ip_match:
                ip_address = ip_match.group()
                ip_address_requests[ip_address] += 1

    # Generate summarized report
    print("404 Errors:", error_404_count)
    print("Most Requested Pages:")
    for page, count in Counter(requested_pages).most_common(5):
        print(f"{page}: {count} requests")
    print("IP Addresses with Most Requests:")
    for ip, count in ip_address_requests.most_common(5):
        print(f"{ip}: {count} requests")

if __name__ == "__main__":
    log_file = "access.log"  # Specify the path to your web server log file
    analyze_logs(log_file)
