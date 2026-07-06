#!/usr/bin/env python3
import json
from datetime import datetime

def generate_final_forensic_summary():
    """Generate comprehensive final forensic summary"""
    
    try:
        # Load all analysis results
        with open('usb_analysis_results.json', 'r') as f:
            usb_data = json.load(f)
        
        with open('usb_forensic_report.json', 'r') as f:
            forensic_data = json.load(f)
        
        with open('usb_event_correlation_report.json', 'r') as f:
            correlation_data = json.load(f)
        
        # Generate final summary
        final_report = {
            'investigation_summary': {
                'case_id': f"USB_FORENSICS_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
                'investigation_date': datetime.now().isoformat(),
                'analyst': 'Forensic Lab Student',
                'evidence_sources': ['SYSTEM Registry Hive', 'SOFTWARE Registry Hive', 'Windows Event Logs']
            },
            'key_findings': {
                'total_usb_devices': len(usb_data['devices']),
                'unique_vendors': len(forensic_data['connection_patterns']['unique_vendors']),
                'devices_with_event_correlation': correlation_data['summary_statistics']['devices_with_events'],
                'risk_assessment': forensic_data['forensic_indicators']['potential_data_exfiltration_risk']
            },
            'device_inventory': usb_data['devices'],
            'timeline_analysis': correlation_data['unified_timeline'],
            'recommendations': [
                'Monitor USB device usage policies',
                'Implement device whitelisting if high-risk devices detected',
                'Regular audit of USB device connections',
                'Consider DLP solutions for sensitive environments'
            ]
        }
        
        # Save final report
        with open('FINAL_USB_FORENSIC_INVESTIGATION.json', 'w') as f:
            json.dump(final_report, f, indent=2)
        
        # Display executive summary
        print("\n" + "="*80)
        print("FINAL USB DEVICE FORENSIC INVESTIGATION SUMMARY")
        print("="*80)
        print(f"Case ID: {final_report['investigation_summary']['case_id']}")
        print(f"Investigation Date: {final_report['investigation_summary']['investigation_date']}")
        print(f"Evidence Sources: {', '.join(final_report['investigation_summary']['evidence_sources'])}")
        print("\nKEY FINDINGS:")
        print(f"  • Total USB Devices Identified: {final_report['key_findings']['total_usb_devices']}")
        print(f"  • Unique Vendors: {final_report['key_findings']['unique_vendors']}")
        print(f"  • Devices with Event Correlation: {final_report['key_findings']['devices_with_event_correlation']}")
        print(f"  • Risk Assessment: {final_report['key_findings']['risk_assessment']}")
        
        print("\nDEVICE INVENTORY:")
        for i, device in enumerate(final_report['device_inventory'], 1):
            print(f"  {i}. {device['vendor_name']} - Serial: {device['serial_number']}")
        
        print("\nRECOMMENDATIONS:")
        for i, rec in enumerate(final_report['recommendations'], 1):
            print(f"  {i}. {rec}")
        
        print(f"\nFinal investigation report saved to: FINAL_USB_FORENSIC_INVESTIGATION.json")
        print("="*80)
        
    except Exception as e:
        print(f"Error generating final report: {e}")

if __name__ == "__main__":
    generate_final_forensic_summary()
