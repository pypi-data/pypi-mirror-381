import re
import pandas as pd
import numpy as np

class APResourceMonitor:
    def __init__(self, content):
        self.content = content
        self.resource_patterns = {
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
            'network_utilization': r'Network\s*[Uu]tilization\s*[:=]\s*(\d+(?:\.\d+)?)%?'
        }
        self.system_patterns = {
            'system_load': r'load\s*averages?\s*[:=]\s*(\d+\.\d+)',
            'cpu_cores': r'CPU\s*cores?\s*[:=]\s*(\d+)',
            'total_ram': r'Total\s*RAM\s*[:=]\s*(\d+)\s*MB',
            'available_ram': r'Available\s*RAM\s*[:=]\s*(\d+)\s*MB',
            'flash_usage': r'Flash\s*[Uu]sage\s*[:=]\s*(\d+(?:\.\d+)?)%?',
            'buffer_usage': r'Buffer\s*[Uu]sage\s*[:=]\s*(\d+(?:\.\d+)?)%?'
        }
        self.error_patterns = {
            'errors': r'error',
            'warnings': r'warning',
            'failures': r'fail',
            'timeouts': r'timeout',
            'drops': r'drop'
        }
        self.resource_data = self._extract_patterns(self.resource_patterns)
        self.system_data = self._extract_patterns(self.system_patterns)
        self.error_counts = self._extract_error_counts()
        self.process_df = self._extract_process_info()
        self.interface_df = self._extract_interface_stats()
        self.resource_stats = self._calc_resource_stats()
        self.health_scores = self._calc_health_scores()
        self.overall_health, self.health_status = self._calc_overall_health()

    def _extract_patterns(self, patterns):
        data = {}
        for key, pattern in patterns.items():
            matches = re.findall(pattern, self.content, re.IGNORECASE)
            if matches:
                try:
                    data[key] = [float(x) for x in matches]
                except ValueError:
                    data[key] = matches
        return data

    def _extract_error_counts(self):
        counts = {}
        for key, pattern in self.error_patterns.items():
            matches = re.findall(pattern, self.content, re.IGNORECASE)
            counts[key] = len(matches)
        return counts

    def _extract_process_info(self):
        process_info = re.findall(
            r'PID\s*:\s*(\d+).*?CPU\s*:\s*(\d+(?:\.\d+)?)%.*?MEM\s*:\s*(\d+(?:\.\d+)?)%',
            self.content, re.IGNORECASE | re.DOTALL
        )
        if process_info:
            df = pd.DataFrame(process_info, columns=['PID', 'CPU_Percent', 'Memory_Percent'])
            return df.astype(float)
        return None

    def _extract_interface_stats(self):
        interface_stats = re.findall(
            r'Interface\s+(\w+).*?RX\s*:\s*(\d+).*?TX\s*:\s*(\d+)',
            self.content, re.IGNORECASE | re.DOTALL
        )
        if interface_stats:
            df = pd.DataFrame(interface_stats, columns=['Interface', 'RX_Bytes', 'TX_Bytes'])
            df['RX_Bytes'] = df['RX_Bytes'].astype(int)
            df['TX_Bytes'] = df['TX_Bytes'].astype(int)
            return df
        return None

    def _calc_resource_stats(self):
        stats = {}
        for key, values in self.resource_data.items():
            if values and isinstance(values[0], (int, float)):
                stats[key] = {
                    'count': len(values),
                    'min': min(values),
                    'max': max(values),
                    'avg': np.mean(values),
                    'std': np.std(values) if len(values) > 1 else 0
                }
        return stats

    def _calc_health_scores(self):
        error_values = list(self.error_counts.values())
        cpu_health = 100 - self.resource_stats.get('cpu_usage', {}).get('avg', 0) if 'cpu_usage' in self.resource_stats else 50
        memory_health = 100 - self.resource_stats.get('memory_usage', {}).get('avg', 0) if 'memory_usage' in self.resource_stats else 50
        load_health = max(0, 100 - (self.resource_stats.get('load_average', {}).get('avg', 0) * 20)) if 'load_average' in self.resource_stats else 50
        error_health = max(0, 100 - (sum(error_values) / 10)) if sum(error_values) > 0 else 100
        return {
            'cpu': cpu_health, 'memory': memory_health, 'load': load_health, 'error': error_health
        }

    def _calc_overall_health(self):
        h = self.health_scores
        health_values = [h['cpu'], h['memory'], h['load'], h['error']]
        overall_health = np.mean(health_values)
        if overall_health >= 80:
            health_status = "Excellent"
        elif overall_health >= 60:
            health_status = "Good"
        elif overall_health >= 40:
            health_status = "Fair"
        else:
            health_status = "Poor"
        return overall_health, health_status

    def print_report(self):
        print("="*80)
        print("AP RESOURCE MONITORING DETAILED REPORT")
        print("="*80)

        stats = self.resource_stats
        print(f"🖥️  SYSTEM PERFORMANCE METRICS:")
        if 'cpu_usage' in stats:
            cpu_avg = stats['cpu_usage']['avg']
            cpu_status = "Normal" if cpu_avg < 70 else "High" if cpu_avg < 90 else "Critical"
            print(f"• CPU Usage: {cpu_avg:.1f}% average ({cpu_status})")
        else:
            print("• CPU Usage: Data not available")

        if 'memory_usage' in stats:
            mem_avg = stats['memory_usage']['avg']
            mem_status = "Normal" if mem_avg < 80 else "High" if mem_avg < 95 else "Critical"
            print(f"• Memory Usage: {mem_avg:.1f}% average ({mem_status})")
        else:
            print("• Memory Usage: Data not available")

        if 'load_average' in stats:
            load_avg = stats['load_average']['avg']
            load_status = "Normal" if load_avg < 2 else "Moderate" if load_avg < 4 else "High"
            print(f"• System Load: {load_avg:.2f} average ({load_status})")

        print(f"📊 RESOURCE AVAILABILITY:")
        total_resources = len(self.resource_data)
        available_resources = sum(1 for v in self.resource_data.values() if v)
        print(f"• Resource metrics available: {available_resources}/{total_resources}")
        print(f"• Monitoring coverage: {(available_resources/max(1,total_resources))*100:.1f}%")

        print(f"⚠️  SYSTEM EVENTS ANALYSIS:")
        error_counts = self.error_counts
        error_values = list(error_counts.values())
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
        if self.interface_df is not None:
            print(f"• Network interfaces monitored: {len(self.interface_df)}")
            total_rx = self.interface_df['RX_Bytes'].sum()
            total_tx = self.interface_df['TX_Bytes'].sum()
            print(f"• Total RX traffic: {total_rx:,} bytes")
            print(f"• Total TX traffic: {total_tx:,} bytes")
            print(f"• Traffic ratio (RX/TX): {total_rx/max(1,total_tx):.2f}")

        print(f"📈 HEALTH ASSESSMENT:")
        print(f"• Overall system health: {self.overall_health:.1f}/100 ({self.health_status})")
        h = self.health_scores
        print(f"• CPU health score: {h['cpu']:.0f}/100")
        print(f"• Memory health score: {h['memory']:.0f}/100")
        print(f"• Load health score: {h['load']:.0f}/100")
        print(f"• Error health score: {h['error']:.0f}/100")

        print(f"🎯 RECOMMENDATIONS:")
        if h['cpu'] < 70:
            print("• Monitor CPU usage - consider load balancing")
        if h['memory'] < 70:
            print("• Check memory usage - possible memory leak")
        if h['load'] < 50:
            print("• High system load detected - investigate processes")
        if h['error'] < 60:
            print("• High error rate - review system logs and configuration")
        if sum(error_values) > 1000:
            print("• Excessive system events - implement log rotation")

        print("="*80)
        print("AP RESOURCE MONITORING ANALYSIS COMPLETE")
        print("="*80)

    def print_tables(self):
        # Resource Statistics Table
        if self.resource_stats:
            resource_table = []
            for key, stats in self.resource_stats.items():
                resource_table.append({
                    'Resource': key.replace('_', ' ').title(),
                    'Samples': stats['count'],
                    'Minimum': f"{stats['min']:.2f}",
                    'Maximum': f"{stats['max']:.2f}",
                    'Average': f"{stats['avg']:.2f}",
                    'Std Dev': f"{stats['std']:.2f}",
                    'Status': 'Normal' if stats['avg'] < 70 else 'High' if stats['avg'] < 90 else 'Critical'
                })
            resource_monitoring_df = pd.DataFrame(resource_table)
            print("Resource Monitoring Statistics:")
            print(resource_monitoring_df.to_string(index=False))

        # System Events Table
        events_table = []
        for event_type, count in self.error_counts.items():
            severity = 'High' if count > 200 else 'Medium' if count > 50 else 'Low'
            events_table.append({
                'Event Type': event_type.title(),
                'Count': count,
                'Percentage': f"{(count/max(1,sum(self.error_counts.values())))*100:.1f}%",
                'Severity': severity
            })

        events_df = pd.DataFrame(events_table)
        print("\nSystem Events Analysis:")
        print(events_df.to_string(index=False))

        # Interface Statistics Table
        if self.interface_df is not None:
            print("\nInterface Statistics:")
            interface_summary = self.interface_df.copy()
            interface_summary['RX_MB'] = interface_summary['RX_Bytes'] / (1024*1024)
            interface_summary['TX_MB'] = interface_summary['TX_Bytes'] / (1024*1024)
            interface_summary['Total_MB'] = interface_summary['RX_MB'] + interface_summary['TX_MB']
            print(interface_summary.to_string(index=False))

        # Health Scores Table
        h = self.health_scores
        health_table = pd.DataFrame({
            'Component': ['CPU', 'Memory', 'System Load', 'Error Rate'],
            'Health Score': [h['cpu'], h['memory'], h['load'], h['error']],
            'Status': [
                'Good' if h['cpu'] >= 70 else 'Fair' if h['cpu'] >= 40 else 'Poor',
                'Good' if h['memory'] >= 70 else 'Fair' if h['memory'] >= 40 else 'Poor',
                'Good' if h['load'] >= 70 else 'Fair' if h['load'] >= 40 else 'Poor',
                'Good' if h['error'] >= 70 else 'Fair' if h['error'] >= 40 else 'Poor'
            ]
        })
        print("\nSystem Health Assessment:")
        print(health_table.to_string(index=False))
