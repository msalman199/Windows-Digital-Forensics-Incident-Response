#!/usr/bin/env python3
from datetime import datetime

def generate_investigation_report():
    report = f"""
DIGITAL FORENSICS INVESTIGATION REPORT
OneDrive Sync Activity & Cached Credentials Analysis
Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

EXECUTIVE SUMMARY
================
Investigation of OneDrive synchronization activity and cached credentials 
revealed potential data exfiltration activities by user john.doe@company.com.

KEY FINDINGS
============
1. Data Upload Activity:
   - 18MB of data uploaded to personal OneDrive
   - Files: financial_report_2024.xlsx (2.3MB), employee_database.csv (15.7MB)
   - Upload time: 2024-01-15 10:30:15 - 10:31:02

2. Credential Access:
   - Cached credentials accessed at 2024-01-15 10:25:30
   - 4 minutes 45 seconds before sync activity began
   - Credentials stored in Windows Credential Manager and browser

3. Risk Indicators:
   - Sensitive file names suggest confidential data
   - Large file sizes indicate bulk data transfer
   - Personal cloud storage used for corporate data

TECHNICAL EVIDENCE
==================
• OneDrive sync logs show systematic upload of corporate files
• Cached credentials indicate automated authentication
• Timeline correlation suggests premeditated activity
• Browser credentials provide persistent access capability

IMPACT ASSESSMENT
=================
• HIGH: Potential exposure of financial and employee data
• MEDIUM: Credential compromise risk
• HIGH: Policy violation (personal cloud storage use)

RECOMMENDATIONS
===============
1. Immediate: Disable user account and revoke OneDrive access
2. Short-term: Audit all files in user's OneDrive account
3. Long-term: Implement DLP controls for cloud storage
4. Policy: Update acceptable use policy for cloud services

INVESTIGATION METHODOLOGY
=========================
• Log file analysis using custom Python scripts
• Credential cache examination
• Timeline correlation analysis
• Risk assessment based on file content and size

EVIDENCE PRESERVATION
====================
All artifacts preserved in: ~/lab9/analysis_output/
• sync_analysis.txt - OneDrive activity analysis
• timeline.txt - Chronological event timeline
• credential_analysis.txt - Cached credential examination
• exfiltration_analysis.txt - Risk assessment and indicators
"""
    return report

# Generate and save report
report = generate_investigation_report()
with open('analysis_output/investigation_report.txt', 'w') as f:
    f.write(report)

print("Investigation Report Generated")
print("=" * 35)
print(report)
