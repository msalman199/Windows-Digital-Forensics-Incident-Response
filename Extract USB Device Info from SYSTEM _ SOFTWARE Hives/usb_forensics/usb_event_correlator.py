#!/usr/bin/env python3
import json
import re
from datetime import datetime

class USBEventCorrelator:
    def __init__(self):
        self.correlations = []
    
    def load_usb_data(self, usb_file):
        """Load USB device data from analysis results"""
        try:
            with open(usb_file, 'r') as f:
                return json.load(f)
        except Exception as e:
            print(f"Error loading USB data: {e}")
            return None
    
    def load_event_logs(self, event_file):
        """Load event log data"""
        try:
            with open(event_file, 'r') as f:
                return json.load(f)
        except Exception as e:
            print(f"Error loading event logs: {e}")
            return None
    
    def extract_serial_from_event(self, description):
        """Extract serial number from event description"""
        # Pattern to match serial numbers in event descriptions
        pattern = r'\\([A-F0-9]{16,})&'
        match = re.search(pattern, description)
        return match.group(1) if match else None
    
    def correlate_usb_events(self, usb_data, event_data):
        """Correlate USB registry data with event logs"""
        correlations = []
        
        for device in usb_data['devices']:
            device_correlations = {
                'device_info': device,
                'matching_events': [],
                'correlation_confidence': 0
            }
            
            # Find matching events
            for event in event_data:
                event_serial = self.extract_serial_from_event(event['description'])
                
                if event_serial and event_serial == device['serial_number']:
                    device_correlations['matching_events'].append(event)
                    device_correlations['correlation_confidence'] += 1
                
                # Also check for vendor/product matches in description
                if (device['vendor_name'].lower() in event['description'].lower() or
                    device['vendor_id'] in event['description']):
                    device_correlations['matching_events'].append(event)
                    device_correlations['correlation_confidence'] += 0.5
            
            correlations.append(device_correlations)
        
        return correlations
    
    def generate_correlation_timeline(self, correlations):
        """Generate timeline combining USB and event data"""
        timeline_events = []
        
        for correlation in correlations:
            device = correlation['device_info']
            
            # Add registry event
            timeline_events.append({
                'timestamp': device['last_write_time'],
                'event_type': 'Registry Update',
                'source': 'USB Registry',
                'device': f"{device['vendor_name']} ({device['serial_number']})",
                'details': f"Device key: {device['device_key']}"
            })
            
            # Add correlated events
            for event in correlation['matching_events']:
                timeline_events.append({
                    'timestamp': event['timestamp'],
                    'event_type': 'System Event',
                    'source': event['source'],
                    'device': f"{device['vendor_name']} ({device['serial_number']})",
                    'details': event['description']
                })
        
        # Sort timeline by timestamp
        timeline_events.sort(key=lambda x: x['timestamp'])
        return timeline_events
    
    def display_correlation_results(self, correlations):
        """Display correlation analysis results"""
        print("\n" + "="*70)
        print("USB DEVICE - EVENT LOG CORRELATION ANALYSIS")
        print("="*70)
        
        for i, correlation in enumerate(correlations, 1):
            device = correlation['device_info']
            confidence = correlation['correlation_confidence']
            
            print(f"\nDevice {i}: {device['vendor_name']}")
            print(f"Serial Number: {device['serial_number']}")
            print(f"Correlation Confidence: {confidence}")
            print(f"Matching Events: {len(correlation['matching_events'])}")
            
            if correlation['matching_events']:
                print("Event Details:")
                for event in correlation['matching_events']:
                    print(f"  - {event['timestamp']}: {event['description'][:80]}...")
            else:
                print("  No matching events found")
            
            print("-" * 50)
    
    def export_correlation_report(self, correlations, timeline):
        """Export comprehensive correlation report"""
        report = {
            'analysis_metadata': {
                'timestamp': datetime.now().isoformat(),
                'analysis_type': 'USB-Event Correlation',
                'total_devices_analyzed': len(correlations)
            },
            'device_correlations': correlations,
            'unified_timeline': timeline,
            'summary_statistics': {
                'devices_with_events': sum(1 for c in correlations if c['matching_events']),
                'total_correlated_events': sum(len(c['matching_events']) for c in correlations),
                'average_confidence': sum(c['correlation_confidence'] for c in correlations) / len(correlations) if correlations else 0
            }
        }
        
        with open('usb_event_correlation_report.json', 'w') as f:
            json.dump(report, f, indent=2)
        
        print(f"\nCorrelation report exported to: usb_event_correlation_report.json")
        print(f"Summary Statistics:")
        print(f"  - Devices with matching events: {report['summary_statistics']['devices_with_events']}")
        print(f"  - Total correlated events: {report['summary_statistics']['total_correlated_events']}")
        print(f"  - Average confidence score: {report['summary_statistics']['average_confidence']:.2f}")

if __name__ == "__main__":
    correlator = USBEventCorrelator()
    
    # Load data
    usb_data = correlator.load_usb_data('usb_analysis_results.json')
    event_data = correlator.load_event_logs('mock_event_logs.json')
    
    if usb_data and event_data:
        # Perform correlation
        correlations = correlator.correlate_usb_events(usb_data, event_data)
        timeline = correlator.generate_correlation_timeline(correlations)
        
        # Display and export results
        correlator.display_correlation_results(correlations)
        correlator.export_correlation_report(correlations, timeline)
    else:
        print("Failed to load required data files")
