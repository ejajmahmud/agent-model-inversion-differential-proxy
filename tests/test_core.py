"""Automated test suite for Differential Privacy Proxy."""
import unittest
from agent_model_inversion_differential_proxy.core import DifferentialPrivacyProxy

class TestDifferentialPrivacyProxy(unittest.TestCase):
    def test_sanitization_bounds(self):
        proxy = DifferentialPrivacyProxy(epsilon=1.0, precision_decimals=2)
        sanitized = proxy.sanitize_probabilities([0.9, 0.1])
        self.assertEqual(len(sanitized), 2)
        self.assertTrue(all(p >= 0.0 for p in sanitized))
