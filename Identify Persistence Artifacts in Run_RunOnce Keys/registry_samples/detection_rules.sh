#!/bin/bash

echo "=== PERSISTENCE DETECTION RULES ==="
echo ""

echo "RED FLAGS IN RUN KEYS:"
echo "1. Executables in \\Users\\Public\\"
echo "2. PowerShell with -WindowStyle Hidden"
echo "3. PowerShell with -ExecutionPolicy Bypass"
echo "4. Rundll32.exe with non-standard DLLs"
echo "5. Base64 encoded commands"
echo "6. Temporary directory executables"
echo "7. Scripts with system-like names in user directories"
echo ""

echo "YARA-STYLE DETECTION PATTERNS:"
echo 'rule Suspicious_Run_Key_PowerShell {'
echo '    strings:'
echo '        $ps1 = "powershell.exe" nocase'
echo '        $hidden = "-WindowStyle Hidden" nocase'
echo '        $bypass = "-ExecutionPolicy Bypass" nocase'
echo '    condition:'
echo '        $ps1 and ($hidden or $bypass)'
echo '}'
echo ''
echo 'rule Suspicious_Run_Key_Location {'
echo '    strings:'
echo '        $public = "\\Users\\Public\\" nocase'
echo '        $temp = "\\temp\\" nocase'
echo '        $downloads = "\\Downloads\\" nocase'
echo '    condition:'
echo '        any of them'
echo '}'
