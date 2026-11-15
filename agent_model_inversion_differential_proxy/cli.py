"""CLI for Differential Privacy Proxy."""
import argparse
from .core import DifferentialPrivacyProxy

def main():
    parser = argparse.ArgumentParser(description="Differential Privacy Proxy CLI")
    parser.add_argument("--demo", action="store_true", help="Demonstrate probability sanitization")
    args = parser.parse_args()

    proxy = DifferentialPrivacyProxy(epsilon=1.0, precision_decimals=2)
    raw = [0.8523419, 0.1245591, 0.0230990]

    sanitized = proxy.sanitize_probabilities(raw)
    print(f"Raw probabilities: {raw}")
    print(f"Sanitized differential output: {sanitized}")

if __name__ == "__main__":
    main()
