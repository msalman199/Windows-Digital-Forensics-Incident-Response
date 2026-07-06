#!/bin/bash
echo "REGISTRY FORENSICS ANALYSIS REPORT" > final_report.txt
echo "Generated on: $(date)" >> final_report.txt
echo "======================================" >> final_report.txt

echo -e "\n1. SYSTEM INFORMATION:" >> final_report.txt
head -10 system_analysis.txt >> final_report.txt

echo -e "\n2. INSTALLED SOFTWARE:" >> final_report.txt
head -15 software_analysis.txt >> final_report.txt

echo -e "\n3. USER ACTIVITY:" >> final_report.txt
head -10 user_analysis.txt >> final_report.txt

echo -e "\n4. NETWORK CONFIGURATION:" >> final_report.txt
head -10 network_config.txt >> final_report.txt

echo -e "\n5. USB DEVICES:" >> final_report.txt
head -10 usb_devices.txt >> final_report.txt

echo -e "\n6. SECURITY FINDINGS:" >> final_report.txt
cat security_findings.txt >> final_report.txt

echo -e "\nReport generation complete."
