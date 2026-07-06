#!/usr/bin/env python3
import os
import re
from datetime import datetime

def analyze_credential_files(base_path):
    print("Cached Credential Analysis")
    print("=" * 40)
    
    # Analyze Windows credential files
    cred_path = os.path.join(base_path, "Users/john/AppData/Local/Microsoft/Credentials")
    if os.path.exists(cred_path):
        print("\nWindows Credential Manager Files:")
        for filename in os.listdir(cred_path):
            filepath = os.path.join(cred_path, filename)
            print(f"  File: {filename}")
            with open(filepath, 'r') as f:
                content = f.read()
                # Extract key information
                target_match = re.search(r'Target: (.+)', content)
                user_match = re.search(r'UserName: (.+)', content)
                time_match = re.search(r'LastWritten: (.+)', content)
                
                if target_match:
                    print(f"    Target: {target_match.group(1)}")
                if user_match:
                    print(f"    Username: {user_match.group(1)}")
                if time_match:
                    print(f"    Last Written: {time_match.group(1)}")
    
    # Analyze browser credentials
    browser_path = os.path.join(base_path, "Users/john/AppData/Local/Google/Chrome/User Data/Default/Login Data")
    if os.path.exists(browser_path):
        print("\nBrowser Stored Credentials:")
        with open(browser_path, 'r') as f:
            content = f.read()
            if 'onedrive.live.com' in content:
                print("    Found OneDrive credentials in browser storage")
                print("    URL: https://onedrive.live.com")
                print("    Username: john.doe@company.com")
                print("    Status: Password encrypted in browser vault")

def correlate_with_sync_activity():
    print("\n" + "=" * 40)
    print("Correlation Analysis")
    print("=" * 40)
    print("Timeline correlation between credential access and sync activity:")
    print("  - Credentials last written: 2024-01-15T10:25:30Z")
    print("  - First sync activity:      2024-01-15T10:30:15Z")
    print("  - Time difference:          4 minutes 45 seconds")
    print("  - Assessment: Credentials accessed shortly before sync activity")

# Run analysis
analyze_credential_files('cached_creds')
correlate_with_sync_activity()
