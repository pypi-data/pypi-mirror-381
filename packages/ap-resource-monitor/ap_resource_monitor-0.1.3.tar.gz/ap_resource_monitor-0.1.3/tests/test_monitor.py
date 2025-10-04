import unittest
from ap_resource_monitor.monitor import APResourceMonitor

class TestAPResourceMonitor(unittest.TestCase):
    def test_basic_extraction(self):
        content = (
            "CPU Usage: 45% Memory Usage: 67% Load Average: 1.5 \"
            "Interface eth0 RX: 123456 TX: 654321\n"
            "error warning fail timeout drop"
        )
        monitor = APResourceMonitor(content)
        self.assertIn("cpu_usage", monitor.resource_data)
        self.assertIn("memory_usage", monitor.resource_data)
        self.assertEqual(monitor.error_counts["errors"], 1)
        self.assertEqual(monitor.error_counts["warnings"], 1)
        self.assertEqual(monitor.error_counts["failures"], 1)
        self.assertEqual(monitor.error_counts["timeouts"], 1)
        self.assertEqual(monitor.error_counts["drops"], 1)

if __name__ == "__main__":
    unittest.main()