import re
import pandas as pd
import numpy as np

def generate_ap_health_report(log_file_path, print_report=True):
    """
    Generate a health report from an AP (Access Point) log file.

    Args:
        log_file_path (str): Path to the log file.
        print_report (bool): Whether to print the report (default: True).

    Returns:
        dict: Dictionary containing parsed statistics and DataFrames.
    """
    with open(log_file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    resource_patterns = {
        'cpu_usage': r'CPU\s*[Uu]sage\s*[:=]\s*(\d+(?:\.\d+)?)%?',
        'memory_usage': r'Memory\s*[Uu]sage\s*[:=]\s*(\d+(?:\.\d+)?)%?',
        'memory_total': r'Total\s*Memory\s*[:=]\s*(\d+)',
        'memory_free': r'Free\s*Memory\s*[:=]\s*(\d+)',
        'memory_used': r'Used\s*Memory\s*[:=]\s*(\d+)',
        'uptime': r'Uptime\s*[:=]\s*(\d+)',
        'temperature': r'Temperature\s*[:=]\s*(\d+(?:\.\d+)?)',
        'load_average': r'Load\s*Average\s*[:=]\s*(\d+(?:\.\d+)?)',
        'processes': r'Processes\s*[:=]\s*(\d+)',
        'threads': r'Threads\s*[:=]\s*(\d+)',
        'disk_usage': r'Disk\s*[Uu]sage\s*[:=]\s*(\d+(?:\.\d+)?)%?',
        'network_utilization': r'Network\s*[Uu]tilization\s*[:=]\s*(\d+(?:\.\d+)?)%?
    }

    resource_data = {}
    for key, pattern in resource_patterns.items():
        matches = re.findall(pattern, content, re.IGNORECASE)
        if matches:
            try:
                resource_data[key] = [float(x) for x in matches]
            except ValueError:
                resource_data[key] = matches

    error_patterns = {
        'errors': r'error',
        'warnings': r'warning',
        'failures': r'fail',
        'timeouts': r'timeout',
        'drops': r'drop'
    }

    error_counts = {k: len(re.findall(p, content, re.IGNORECASE)) for k, p in error_patterns.items()}

    # Resource statistics
    resource_stats = {}
    for key, values in resource_data.items():
        if values and isinstance(values[0], (int, float)):
            resource_stats[key] = {
                'count': len(values),
                'min': min(values),
                'max': max(values),
                'avg': np.mean(values),
                'std': np.std(values) if len(values) > 1 else 0
            }

    # Health scores
    error_values = list(error_counts.values())
    cpu_health = 100 - resource_stats.get('cpu_usage', {}).get('avg', 0) if 'cpu_usage' in resource_stats else 50
    memory_health = 100 - resource_stats.get('memory_usage', {}).get('avg', 0) if 'memory_usage' in resource_stats else 50
    load_health = max(0, 100 - (resource_stats.get('load_average', {}).get('avg', 0) * 20)) if 'load_average' in resource_stats else 50
    error_health = max(0, 100 - (sum(error_values) / 10)) if sum(error_values) > 0 else 100

    health_values = [cpu_health, memory_health, load_health, error_health]
    overall_health = np.mean(health_values)
    if overall_health >= 80:
        health_status = "Excellent"
    elif overall_health >= 60:
        health_status = "Good"
    elif overall_health >= 40:
        health_status = "Fair"
    else:
        health_status = "Poor"

    # Process info
    process_info = re.findall(
        r'PID\s*:\s*(\d+).*?CPU\s*:\s*(\d+(?:\.\d+)?)%.*?MEM\s*:\s*(\d+(?:\.\d+)?)%',
        content, re.IGNORECASE | re.DOTALL
    )
    process_df = pd.DataFrame(process_info, columns=['PID', 'CPU_Percent', 'Memory_Percent']).astype(float) if process_info else None

    # Interface info
    interface_stats = re.findall(
        r'Interface\s+(\w+).*?RX\s*:\s*(\d+).*?TX\s*:\s*(\d+)',
        content, re.IGNORECASE | re.DOTALL
    )
    interface_df = pd.DataFrame(interface_stats, columns=['Interface', 'RX_Bytes', 'TX_Bytes']) if interface_stats else None
    if interface_df is not None:
        interface_df['RX_Bytes'] = interface_df['RX_Bytes'].astype(int)
        interface_df['TX_Bytes'] = interface_df['TX_Bytes'].astype(int)

    # Compose return value
    results = {
        "resource_stats": resource_stats,
        "error_counts": error_counts,
        "cpu_health": cpu_health,
        "memory_health": memory_health,
        "load_health": load_health,
        "error_health": error_health,
        "overall_health": overall_health,
        "health_status": health_status,
        "process_df": process_df,
        "interface_df": interface_df
    }

    # Optionally print report
    if print_report:
        print("="*80)
        print("AP RESOURCE MONITORING DETAILED REPORT")
        print("="*80)
        print("🖥️  SYSTEM PERFORMANCE METRICS:")
        if 'cpu_usage' in resource_stats:
            cpu_avg = resource_stats['cpu_usage']['avg']
            cpu_status = "Normal" if cpu_avg < 70 else "High" if cpu_avg < 90 else "Critical"
            print(f"• CPU Usage: {cpu_avg:.1f}% average ({cpu_status})")
        else:
            print("• CPU Usage: Data not available")
        if 'memory_usage' in resource_stats:
            mem_avg = resource_stats['memory_usage']['avg']
            mem_status = "Normal" if mem_avg < 80 else "High" if mem_avg < 95 else "Critical"
            print(f"• Memory Usage: {mem_avg:.1f}% average ({mem_status})")
        else:
            print("• Memory Usage: Data not available")
        if 'load_average' in resource_stats:
            load_avg = resource_stats['load_average']['avg']
            load_status = "Normal" if load_avg < 2 else "Moderate" if load_avg < 4 else "High"
            print(f"• System Load: {load_avg:.2f} average ({load_status})")
        print(f"📊 RESOURCE AVAILABILITY:")
        total_resources = len(resource_data)
        available_resources = sum(1 for v in resource_data.values() if v)
        print(f"• Resource metrics available: {available_resources}/{total_resources}")
        print(f"• Monitoring coverage: {(available_resources/max(1,total_resources))*100:.1f}%")
        print(f"⚠️  SYSTEM EVENTS ANALYSIS:")
        total_events = sum(error_values)
        print(f"• Total system events: {total_events:,}")
        print(f"• Error rate: {error_counts['errors']:,} errors")
        print(f"• Warning rate: {error_counts['warnings']:,} warnings")
        print(f"• Failure rate: {error_counts['failures']:,} failures")
        print(f"• Timeout events: {error_counts['timeouts']:,}")
        print(f"• Drop events: {error_counts['drops']:,}")
        if total_events > 0:
            error_ratio = error_counts['errors'] / total_events
            if error_ratio > 0.5:
                severity = "High"
            elif error_ratio > 0.2:
                severity = "Moderate"
            else:
                severity = "Low"
            print(f"• Event severity level: {severity}")
        print(f"🔧 INTERFACE MONITORING:")
        if interface_df is not None:
            print(f"• Network interfaces monitored: {len(interface_df)}")
            total_rx = interface_df['RX_Bytes'].sum()
            total_tx = interface_df['TX_Bytes'].sum()
            print(f"• Total RX traffic: {total_rx:,} bytes")
            print(f"• Total TX traffic: {total_tx:,} bytes")
            print(f"• Traffic ratio (RX/TX): {total_rx/max(1,total_tx):.2f}")
        print(f"📈 HEALTH ASSESSMENT:")
        print(f"• Overall system health: {overall_health:.1f}/100 ({health_status})")
        print(f"• CPU health score: {cpu_health:.0f}/100")
        print(f"• Memory health score: {memory_health:.0f}/100")
        print(f"• Load health score: {load_health:.0f}/100")
        print(f"• Error health score: {error_health:.0f}/100")
        print(f"🎯 RECOMMENDATIONS:")
        if cpu_health < 70:
            print("• Monitor CPU usage - consider load balancing")
        if memory_health < 70:
            print("• Check memory usage - possible memory leak")
        if load_health < 50:
            print("• High system load detected - investigate processes")
        if error_health < 60:
            print("• High error rate - review system logs and configuration")
        if total_events > 1000:
            print("• Excessive system events - implement log rotation")
        print("="*80)
        print("AP RESOURCE MONITORING ANALYSIS COMPLETE")
        print("="*80)

    return results
