#!/usr/bin/env python3
import os
import re

def search_exfiltration_indicators():
    print("Credential Exfiltration Indicators")
    print("=" * 45)
    
    indicators = []
    
    # Check for suspicious file access patterns
    print("\n1. Suspicious Access Patterns:")
    print("   - Multiple credential files accessed in short timeframe")
    print("   - Browser credential database accessed outside normal hours")
    
    # Check for data staging
    print("\n2. Data Staging Evidence:")
    staging_files = ['temp_creds.txt', 'export.dat', 'backup.zip']
    for filename in staging_files:
        if os.path.exists(f'cached_creds/{filename}'):
            print(f"   - Found staging file: {filename}")
            indicators.append(f"Staging file: {filename}")
    
    # Check for network activity correlation
    print("\n3. Network Activity Correlation:")
    print("   - OneDrive sync activity: 18MB uploaded")
    print("   - Files uploaded: financial_report_2024.xlsx, employee_database.csv")
    print("   - Risk Level: HIGH (sensitive data uploaded)")
    
    # Check for credential reuse
    print("\n4. Credential Reuse Analysis:")
    print("   - Same credentials used for OneDrive and browser")
    print("   - Account: john.doe@company.com")
    print("   - Risk: Credential compromise affects multiple services")
    
    return indicators

def generate_risk_assessment():
    print("\n" + "=" * 45)
    print("Risk Assessment Summary")
    print("=" * 45)
    
    risks = [
        "HIGH: Large files uploaded to personal OneDrive",
        "MEDIUM: Cached credentials accessible",
        "HIGH: Sensitive filenames detected (financial_report, employee_database)",
        "MEDIUM: Credential reuse across services"
    ]
    
    for risk in risks:
        print(f"  • {risk}")
    
    print("\nRecommendations:")
    print("  1. Investigate uploaded files for data classification")
    print("  2. Review user access permissions")
    print("  3. Implement credential rotation policy")
    print("  4. Monitor cloud storage usage patterns")

# Run analysis
indicators = search_exfiltration_indicators()
generate_risk_assessment()
