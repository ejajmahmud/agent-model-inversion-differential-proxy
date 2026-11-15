"""Core implementation of differential privacy proxy."""
import random
from typing import List

class DifferentialPrivacyProxy:
    def __init__(self, epsilon: float = 1.0, precision_decimals: int = 2):
        self.epsilon = epsilon
        self.precision = precision_decimals

    def sanitize_probabilities(self, probs: List[float]) -> List[float]:
        # Add bounded Laplace noise
        scale = 1.0 / self.epsilon
        noisy = []
        for p in probs:
            noise = random.uniform(-0.01 * scale, 0.01 * scale)
            noisy.append(max(0.0, p + noise))

        total = sum(noisy) or 1.0
        normalized = [round(v / total, self.precision) for v in noisy]
        return normalized
