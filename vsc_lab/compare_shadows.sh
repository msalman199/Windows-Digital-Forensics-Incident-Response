#!/bin/bash

echo "=== Shadow Copy Comparison Report ==="
echo "Generated: $(date)"
echo

# Compare file counts between shadow copies
if [ -d ~/vsc_lab/shadow_mounts/vsc1 ] && [ -d ~/vsc_lab/shadow_mounts/vsc2 ]; then
    echo "File count in VSC1: $(find ~/vsc_lab/shadow_mounts/vsc1 -type f | wc -l)"
    echo "File count in VSC2: $(find ~/vsc_lab/shadow_mounts/vsc2 -type f | wc -l)"
fi

# List unique files in each shadow copy
echo -e "\n=== Files unique to each shadow copy ==="
if [ -d ~/vsc_lab/shadow_mounts/vsc1 ]; then
    find ~/vsc_lab/shadow_mounts/vsc1 -type f > /tmp/vsc1_files.txt
fi
if [ -d ~/vsc_lab/shadow_mounts/vsc2 ]; then
    find ~/vsc_lab/shadow_mounts/vsc2 -type f > /tmp/vsc2_files.txt
fi
