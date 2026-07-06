#!/bin/bash

echo "=== Windows Registry Run Keys Analysis ==="
echo "Date: $(date)"
echo ""

echo "SUSPICIOUS INDICATORS TO LOOK FOR:"
echo "- Executables in unusual locations (temp, public folders)"
echo "- PowerShell commands with hidden windows"
echo "- Rundll32.exe with suspicious DLLs"
echo "- Base64 encoded commands"
echo "- Scripts in system directories"
echo ""

echo "=== HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run ==="
grep -A 10 "CurrentVersion\\\\Run" ~/registry_samples/sample_software.reg | grep -E "^\".*\"="

echo ""
echo "=== HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\RunOnce ==="
grep -A 10 "CurrentVersion\\\\RunOnce" ~/registry_samples/sample_software.reg | grep -E "^\".*\"="

echo ""
echo "=== Analysis Complete ==="
