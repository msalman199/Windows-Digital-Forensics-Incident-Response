#!/usr/bin/env python3
import re
import json
from datetime import datetime

class USBDeviceParser:
    def __init__(self):
        self.usb_devices = []
        self.vendor_codes = {
            '0781': 'SanDisk',
            '058F': 'Alcor Micro',
            '090C': 'Silicon Motion',
            '0951': 'Kingston Technology',
            '1058': 'Western Digital'
        }
    
    def parse_usb_registry_data(self, data_file):
        """Parse USB device information from registry data"""
        try:
            with open(data_file, 'r') as f:
                content = f.read()
            
            # Extract USB device information using regex
            vid_pattern = r'VID: ([A-F0-9]{4})'
            pid_pattern = r'PID: ([A-F0-9]{4})'
            serial_pattern = r'Serial: ([A-F0-9]+)'
            time_pattern = r'Last Write: ([\d\-\s:]+)'
            
            vids = re.findall(vid_pattern, content)
            pids = re.findall(pid_pattern, content)
            serials = re.findall(serial_pattern, content)
            times = re.findall(time_pattern, content)
            
            # Combine extracted data
            for i in range(len(vids)):
                device = {
                    'vendor_id': vids[i],
                    'product_id': pids[i],
                    'serial_number': serials[i],
                    'last_write_time': times[i],
                    'vendor_name': self.vendor_codes.get(vids[i], 'Unknown'),
                    'device_key': f"VID_{vids[i]}&PID_{pids[i]}"
                }
                self.usb_devices.append(device)
            
            return True
        except Exception as e:
            print(f"Error parsing registry data: {e}")
            return False
    
    def generate_timeline(self):
        """Generate timeline of USB device connections"""
        timeline = []
        for device in self.usb_devices:
            timeline.append({
                'timestamp': device['last_write_time'],
                'event': 'USB Device Registry Update',
                'device': f"{device['vendor_name']} ({device['device_key']})",
                'serial': device['serial_number']
            })
        
        # Sort by timestamp
        timeline.sort(key=lambda x: x['timestamp'])
        return timeline
    
    def export_results(self, output_file):
        """Export parsed results to JSON"""
        results = {
            'total_devices': len(self.usb_devices),
            'devices': self.usb_devices,
            'timeline': self.generate_timeline(),
            'analysis_timestamp': datetime.now().isoformat()
        }
        
        with open(output_file, 'w') as f:
            json.dump(results, f, indent=2)
        
        print(f"Results exported to {output_file}")
    
    def display_summary(self):
        """Display summary of found USB devices"""
        print("\n" + "="*50)
        print("USB DEVICE FORENSIC ANALYSIS SUMMARY")
        print("="*50)
        print(f"Total USB Devices Found: {len(self.usb_devices)}")
        print("-"*50)
        
        for i, device in enumerate(self.usb_devices, 1):
            print(f"Device {i}:")
            print(f"  Vendor: {device['vendor_name']} ({device['vendor_id']})")
            print(f"  Product ID: {device['product_id']}")
            print(f"  Serial Number: {device['serial_number']}")
            print(f"  Last Registry Update: {device['last_write_time']}")
            print(f"  Device Key: {device['device_key']}")
            print("-"*30)

if __name__ == "__main__":
    parser = USBDeviceParser()
    
    # Parse the mock registry data
    if parser.parse_usb_registry_data('mock_system_usb.txt'):
        parser.display_summary()
        parser.export_results('usb_analysis_results.json')
    else:
        print("Failed to parse registry data")
