#!/usr/bin/env python3
import json
import hashlib
from datetime import datetime

class USBMetadataExtractor:
    def __init__(self):
        self.metadata = {}
    
    def extract_device_signatures(self, results_file):
        """Extract unique device signatures for identification"""
        try:
            with open(results_file, 'r') as f:
                data = json.load(f)
            
            signatures = []
            for device in data['devices']:
                # Create unique device signature
                signature_string = f"{device['vendor_id']}{device['product_id']}{device['serial_number']}"
                signature_hash = hashlib.md5(signature_string.encode()).hexdigest()
                
                signatures.append({
                    'device_signature': signature_hash,
                    'vendor_id': device['vendor_id'],
                    'product_id': device['product_id'],
                    'serial_number': device['serial_number'],
                    'vendor_name': device['vendor_name']
                })
            
            return signatures
        except Exception as e:
            print(f"Error extracting signatures: {e}")
            return []
    
    def analyze_connection_patterns(self, results_file):
        """Analyze USB connection patterns"""
        try:
            with open(results_file, 'r') as f:
                data = json.load(f)
            
            patterns = {
                'unique_vendors': set(),
                'connection_frequency': {},
                'time_analysis': []
            }
            
            for device in data['devices']:
                patterns['unique_vendors'].add(device['vendor_name'])
                
                # Count connections per vendor
                vendor = device['vendor_name']
                patterns['connection_frequency'][vendor] = patterns['connection_frequency'].get(vendor, 0) + 1
                
                # Time analysis
                patterns['time_analysis'].append({
                    'device': device['device_key'],
                    'timestamp': device['last_write_time']
                })
            
            patterns['unique_vendors'] = list(patterns['unique_vendors'])
            return patterns
        except Exception as e:
            print(f"Error analyzing patterns: {e}")
            return {}
    
    def generate_forensic_report(self, results_file):
        """Generate comprehensive forensic report"""
        signatures = self.extract_device_signatures(results_file)
        patterns = self.analyze_connection_patterns(results_file)
        
        report = {
            'report_metadata': {
                'generated_at': datetime.now().isoformat(),
                'analysis_type': 'USB Device Registry Forensics',
                'tool_version': '1.0'
            },
            'device_signatures': signatures,
            'connection_patterns': patterns,
            'forensic_indicators': {
                'total_unique_devices': len(signatures),
                'vendor_diversity': len(patterns.get('unique_vendors', [])),
                'potential_data_exfiltration_risk': 'Medium' if len(signatures) > 2 else 'Low'
            }
        }
        
        # Save report
        with open('usb_forensic_report.json', 'w') as f:
            json.dump(report, f, indent=2)
        
        print("\n" + "="*60)
        print("COMPREHENSIVE USB FORENSIC REPORT")
        print("="*60)
        print(f"Analysis Date: {report['report_metadata']['generated_at']}")
        print(f"Total Unique Devices: {report['forensic_indicators']['total_unique_devices']}")
        print(f"Vendor Diversity: {report['forensic_indicators']['vendor_diversity']}")
        print(f"Risk Assessment: {report['forensic_indicators']['potential_data_exfiltration_risk']}")
        print("-"*60)
        
        print("\nDevice Signatures:")
        for sig in signatures:
            print(f"  {sig['vendor_name']}: {sig['device_signature'][:16]}...")
        
        print("\nVendor Connection Frequency:")
        for vendor, count in patterns.get('connection_frequency', {}).items():
            print(f"  {vendor}: {count} device(s)")
        
        print("\nForensic report saved to: usb_forensic_report.json")

if __name__ == "__main__":
    extractor = USBMetadataExtractor()
    extractor.generate_forensic_report('usb_analysis_results.json')
