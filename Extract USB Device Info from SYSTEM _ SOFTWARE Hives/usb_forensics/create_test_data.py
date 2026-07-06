#!/usr/bin/env python3
import os
import struct

def create_mock_registry_data():
    """Create mock USB registry entries for testing"""
    
    # Mock SYSTEM hive USB data
    system_data = {
        'USB_Devices': [
            {
                'VID': '0781',  # SanDisk
                'PID': '5567',  # Cruzer Blade
                'Serial': '4C530001071227117433',
                'LastWrite': '2024-01-15 14:30:22'
            },
            {
                'VID': '058F',  # Alcor Micro
                'PID': '6387',  # Flash Drive
                'Serial': '058F63876583',
                'LastWrite': '2024-01-10 09:15:45'
            }
        ]
    }
    
    # Write mock data to file
    with open('mock_system_usb.txt', 'w') as f:
        f.write("Mock USB Device Registry Data\n")
        f.write("=" * 40 + "\n")
        for device in system_data['USB_Devices']:
            f.write(f"VID: {device['VID']}\n")
            f.write(f"PID: {device['PID']}\n")
            f.write(f"Serial: {device['Serial']}\n")
            f.write(f"Last Write: {device['LastWrite']}\n")
            f.write("-" * 30 + "\n")
    
    print("Mock registry data created successfully")

if __name__ == "__main__":
    create_mock_registry_data()
