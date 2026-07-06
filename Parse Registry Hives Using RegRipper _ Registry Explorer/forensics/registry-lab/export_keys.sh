#!/bin/bash
echo "Exporting critical registry keys..."
rip -r SYSTEM.hiv -p services | grep -A5 -B5 "svchost" > critical_services.txt
rip -r SOFTWARE.hiv -p uninstall | grep -i "microsoft" > microsoft_software.txt
echo "Export complete."
