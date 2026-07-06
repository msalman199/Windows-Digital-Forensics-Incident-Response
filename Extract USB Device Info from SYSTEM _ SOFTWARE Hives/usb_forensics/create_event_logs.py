#!/usr/bin/env python3
import json
from datetime import datetime, timedelta

def create_mock_event_logs():
    """Create mock Windows event logs for USB correlation"""
    
    # Mock event log entries
    events = [
        {
            'event_id': 20001,
            'timestamp': '2024-01-15 14:30:20',
            'source': 'Microsoft-Windows-Kernel-PnP',
            'description': 'Device USBSTOR\\Disk&Ven_SanDisk&Prod_Cruzer_Blade&Rev_1.00\\4C530001071227117433&0 was configured.',
            'level': 'Information'
        },
        {
            'event_id': 20003,
            'timestamp': '2024-01-15 14:30:22',
            'source': 'Microsoft-Windows-Kernel-PnP',
            'description': 'Device USBSTOR\\Disk&Ven_SanDisk&Prod_Cruzer_Blade&Rev_1.00\\4C530001071227117433&0 started.',
            'level': 'Information'
        },
        {
            'event_id': 20001,
            'timestamp': '2024-01-10 09:15:43',
            'source': 'Microsoft-Windows-Kernel-PnP',
            'description': 'Device USBSTOR\\Disk&Ven_Alcor&Prod_Flash_Drive&Rev_1.00\\058F63876583&0 was configured.',
            'level': 'Information'
        },
        {
            'event_id': 20003,
            'timestamp': '2024-01-10 09:15:45',
            'source': 'Microsoft-Windows-Kernel-PnP',
            'description': 'Device USBSTOR\\Disk&Ven_Alcor&Prod_Flash_Drive&Rev_1.00\\058F63876583&0 started.',
            'level': 'Information'
        }
    ]
    
    # Save mock event logs
    with open('mock_event_logs.json', 'w') as f:
        json.dump(events, f, indent=2)
    
    print("Mock event logs created successfully")

if __name__ == "__main__":
    create_mock_event_logs()
