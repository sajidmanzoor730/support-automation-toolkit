import re
from collections import Counter
import csv

# Support Automation: Parse SIP logs and generate RCA report
LOG_FILE = "sip.log"
REPORT_FILE = "sip_rca_report.csv"

def parse_sip_logs():
    with open(LOG_FILE, 'r', errors='ignore') as f:
        content = f.read()
    
    # Count SIP error codes
    codes = re.findall(r'SIP/2\.0 (\d{3})', content)
    print(f"Total SIP Responses: {len(codes)}")
    print("Error Breakdown:", Counter(codes))
    
    # Find one-way audio (RTP without RTCP)
    one_way = len(re.findall(r'RTP.*no RTCP', content))
    print(f"Potential One-Way Audio Cases: {one_way}")

    # Generate CSV for JIRA
    counter = Counter(codes)
    with open(REPORT_FILE, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['SIP Code', 'Count', 'Action'])
        for code, count in counter.items():
            action = "Check Auth" if code in ['401','403'] else "Check NAT/Firewall" if code == '486' else "Review"
            writer.writerow([code, count, action])
    print(f"Report saved to {REPORT_FILE}")

if __name__ == "__main__":
    parse_sip_logs()
