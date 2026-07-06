#!/bin/bash

echo "=== DETAILED PERSISTENCE ANALYSIS ==="
echo ""

echo "LEGITIMATE ENTRIES (Typical):"
echo "- Windows Defender: MSASCuiL.exe"
echo "- System services: svchost.exe with proper parameters"
echo ""

echo "SUSPICIOUS ENTRIES IDENTIFIED:"
echo ""

echo "1. SUSPICIOUS: MaliciousApp"
echo "   Path: C:\\Users\\Public\\malware.exe"
echo "   Risk: HIGH - Executable in Public folder"
echo "   Reason: Public folders are commonly used by malware"
echo ""

echo "2. SUSPICIOUS: SystemCheck"
echo "   Command: powershell.exe -WindowStyle Hidden -ExecutionPolicy Bypass"
echo "   Risk: HIGH - Hidden PowerShell execution"
echo "   Reason: Bypasses execution policy, runs hidden"
echo ""

echo "3. SUSPICIOUS: SuspiciousOnce"
echo "   Path: C:\\Users\\Public\\Downloads\\update.bat"
echo "   Risk: MEDIUM - Batch file in Downloads"
echo "   Reason: Unusual location for system updates"
echo ""

echo "4. SUSPICIOUS: BackdoorService"
echo "   Command: rundll32.exe C:\\Windows\\System32\\malicious.dll,StartService"
echo "   Risk: HIGH - Suspicious DLL execution"
echo "   Reason: DLL name suggests malicious intent"
echo ""

echo "INVESTIGATION RECOMMENDATIONS:"
echo "- Verify file existence and digital signatures"
echo "- Check file creation/modification timestamps"
echo "- Analyze network connections from these processes"
echo "- Review parent process relationships"
echo "- Examine file hashes against threat intelligence"
