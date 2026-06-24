#!/usr/bin/env python3
import argparse
import re
import urllib.parse
import xml.etree.ElementTree as ET
from collections import defaultdict
import sys
import base64
import html

def parse_burp_xml(file_path):
    """Parse Burp Suite XML export file with base64 support."""
    requests = []
    
    with open(file_path, 'r', encoding='utf-8', errors='replace') as f:
        content = f.read()
    
    try:
        root = ET.fromstring(content)
        items = root.findall('.//item')
        
        for item in items:
            request_elem = item.find('request')
            url_elem = item.find('url')
            method_elem = item.find('method')
            
            if request_elem is not None and request_elem.text:
                raw = request_elem.text.strip()
                
                # Check if base64 encoded
                is_base64 = request_elem.get('base64', 'false') == 'true'
                
                if is_base64:
                    try:
                        raw = base64.b64decode(raw).decode('utf-8', errors='replace')
                    except Exception as e:
                        print(f"[!] Base64 decode error: {e}")
                        continue
                else:
                    # Might be HTML escaped
                    if '&lt;' in raw or '&gt;' in raw:
                        raw = html.unescape(raw)
                
                url = url_elem.text.strip() if url_elem is not None and url_elem.text else 'N/A'
                method = method_elem.text.strip() if method_elem is not None and method_elem.text else ''
                
                requests.append({
                    'raw': raw,
                    'url': url,
                    'method': method
                })
    
    except ET.ParseError as e:
        print(f"[!] XML parse error: {e}")
        sys.exit(1)
    
    return requests

def parse_raw_http(raw_text):
    """Parse raw HTTP request to extract method, path, host, headers, and body."""
    result = {
        'method': '',
        'path': '',
        'host': '',
        'full_url': '',
        'headers': {},
        'body': ''
    }
    
    # Normalize line endings
    raw_text = raw_text.replace('\r\n', '\n')
    
    # Find where headers end and body begins
    # Body starts after the first empty line
    body_start = raw_text.find('\n\n')
    if body_start == -1:
        body_start = raw_text.find('\r\n\r\n')
    
    if body_start != -1:
        header_section = raw_text[:body_start]
        result['body'] = raw_text[body_start:].strip('\n').strip()
    else:
        header_section = raw_text
    
    lines = header_section.split('\n')
    
    # Parse request line
    if lines:
        request_line = lines[0].strip()
        match = re.match(r'(GET|POST|PUT|DELETE|PATCH|HEAD|OPTIONS)\s+(\S+)\s+HTTP/', request_line, re.IGNORECASE)
        if match:
            result['method'] = match.group(1).upper()
            result['path'] = match.group(2)
    
    # Parse headers
    for line in lines[1:]:
        line = line.strip()
        if ':' in line:
            key, value = line.split(':', 1)
            result['headers'][key.strip().lower()] = value.strip()
            if key.strip().lower() == 'host':
                result['host'] = value.strip()
    
    # Construct full URL
    if result['host'] and result['path']:
        if result['path'].startswith('http'):
            result['full_url'] = result['path']
        else:
            result['full_url'] = f"https://{result['host']}{result['path']}"
    
    return result

def extract_post_params(body):
    """Extract parameters from POST body - supports url-encoded form data."""
    params = []
    
    if not body or not body.strip():
        return params
    
    body = body.strip()
    
    # URL-encoded form data (most common)
    if '&' in body and '=' in body:
        try:
            pairs = body.split('&')
            for pair in pairs:
                if '=' in pair:
                    key, value = pair.split('=', 1)
                    # URL decode both key and value
                    key = urllib.parse.unquote_plus(key)
                    value = urllib.parse.unquote_plus(value)
                    params.append({
                        'name': key,
                        'value': value,
                        'type': 'form'
                    })
                else:
                    key = urllib.parse.unquote_plus(pair.strip())
                    if key:
                        params.append({
                            'name': key,
                            'value': '',
                            'type': 'form'
                        })
        except Exception:
            pass
    
    # JSON
    if not params and (body.startswith('{') or body.startswith('[')):
        try:
            import json
            data = json.loads(body)
            
            def extract_json(obj, prefix=''):
                if isinstance(obj, dict):
                    for k, v in obj.items():
                        full_key = f"{prefix}.{k}" if prefix else k
                        if isinstance(v, (dict, list)):
                            extract_json(v, full_key)
                        else:
                            params.append({
                                'name': full_key,
                                'value': str(v) if v is not None else 'null',
                                'type': 'json'
                            })
                elif isinstance(obj, list):
                    for i, item in enumerate(obj):
                        full_key = f"{prefix}[{i}]"
                        if isinstance(item, (dict, list)):
                            extract_json(item, full_key)
                        else:
                            params.append({
                                'name': full_key,
                                'value': str(item) if item is not None else 'null',
                                'type': 'json'
                            })
            
            extract_json(data)
        except json.JSONDecodeError:
            pass
    
    return params

def format_output(organized_params):
    """Format the extracted parameters nicely."""
    lines = []
    lines.append("=" * 80)
    lines.append("BURP SUITE POST PARAMETER EXTRACTOR")
    lines.append("=" * 80)
    
    total_params = 0
    
    for url, params in organized_params.items():
        lines.append(f"\n{'─' * 80}")
        lines.append(f"URL: {url}")
        lines.append(f"Parameters: {len(params)}")
        lines.append(f"{'─' * 80}")
        
        params.sort(key=lambda x: x['name'])
        
        lines.append(f"{'Parameter Name':<40} {'Value':<40}")
        lines.append(f"{'─' * 39} {'─' * 39}")
        
        for p in params:
            val = p['value'][:80] + '...' if len(p['value']) > 80 else p['value']
            lines.append(f"{p['name']:<40} {val:<40}")
            total_params += 1
    
    lines.append(f"\n{'=' * 80}")
    lines.append(f"SUMMARY: {len(organized_params)} URLs with POST parameters, {total_params} total parameters")
    lines.append(f"{'=' * 80}")
    
    return '\n'.join(lines)

def main():
    parser = argparse.ArgumentParser(description='Extract POST parameters from Burp Suite XML exports')
    parser.add_argument('-f', '--file', required=True, help='Burp Suite XML export file')
    parser.add_argument('-o', '--output', help='Output file (prints to stdout if not specified)')
    parser.add_argument('--csv', help='Export to CSV file')
    parser.add_argument('--debug', '-d', action='store_true', help='Show debug output')
    
    args = parser.parse_args()
    
    print(f"[*] Reading Burp XML: {args.file}")
    requests = parse_burp_xml(args.file)
    print(f"[*] Found {len(requests)} request(s)")
    
    if not requests:
        print("[!] No requests found!")
        sys.exit(1)
    
    organized = defaultdict(list)
    
    for i, req in enumerate(requests):
        method = req['method']
        if args.debug:
            print(f"\n[DEBUG] Request #{i+1}: method={method}, url={req['url'][:80]}...")
        
        if method != 'POST':
            if args.debug:
                print(f"[DEBUG] Skipping non-POST request")
            continue
        
        parsed = parse_raw_http(req['raw'])
        
        if args.debug:
            print(f"[DEBUG] Parsed method: {parsed['method']}")
            print(f"[DEBUG] Body ({len(parsed['body'])} chars): {parsed['body']}")
        
        params = extract_post_params(parsed['body'])
        
        if args.debug:
            print(f"[DEBUG] Extracted {len(params)} parameter(s)")
            for p in params:
                print(f"         {p['name']} = {p['value']}")
        
        url = parsed['full_url'] or req['url']
        
        for p in params:
            organized[url].append(p)
    
    if not organized:
        print("\n[!] No POST parameters found!")
        print("[!] Possible reasons:")
        print("  1. The XML contains only GET requests")
        print("  2. POST body is empty")
        print("  3. The body format is not supported")
        print("\n[*] Try running with --debug flag to see raw request contents")
        sys.exit(1)
    
    output = format_output(organized)
    
    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(output)
        print(f"\n[+] Output saved to: {args.output}")
    else:
        print(output)
    
    if args.csv:
        import csv
        with open(args.csv, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['URL', 'Parameter Name', 'Parameter Value'])
            for url, params in organized.items():
                for p in params:
                    writer.writerow([url, p['name'], p['value']])
        print(f"[+] CSV saved to: {args.csv}")

if __name__ == '__main__':
    main()
