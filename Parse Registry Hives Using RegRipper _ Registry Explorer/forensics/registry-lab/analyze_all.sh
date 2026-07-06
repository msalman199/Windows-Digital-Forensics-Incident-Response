#!/bin/bash
echo "=== SYSTEM ANALYSIS ===" > full_report.txt
rip -r SYSTEM.hiv -p compname >> full_report.txt
rip -r SYSTEM.hiv -p services >> full_report.txt
echo -e "\n=== SOFTWARE ANALYSIS ===" >> full_report.txt
rip -r SOFTWARE.hiv -p uninstall >> full_report.txt
echo -e "\n=== USER ANALYSIS ===" >> full_report.txt
rip -r NTUSER.DAT -p userassist >> full_report.txt
rip -r NTUSER.DAT -p recentdocs >> full_report.txt
echo "Analysis complete. Report saved to full_report.txt"
