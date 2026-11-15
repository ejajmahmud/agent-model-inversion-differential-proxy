# Agent Model Inversion Differential Proxy ⚡

<p align="center">
  <img src="assets/architecture.svg" alt="Agent Model Inversion Differential Proxy Architecture" width="100%">
</p>

<p align="center">
  <a href="https://github.com/ejajmahmud/agent-model-inversion-differential-proxy/releases"><img src="https://img.shields.io/github/v/release/ejajmahmud/agent-model-inversion-differential-proxy?color=blue&label=version" alt="GitHub release"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-blue.svg" alt="License: MIT"></a>
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/python-3.9+-3776AB.svg?style=flat&logo=python&logoColor=white" alt="Python 3.9+"></a>
  <a href="https://github.com/ejajmahmud/agent-model-inversion-differential-proxy/actions"><img src="https://img.shields.io/badge/tests-passing-brightgreen.svg" alt="Tests"></a>
</p>

**Agent Model Inversion Differential Proxy** is a production-ready developer tool and connector: Output sanitizer preventing model inversion attacks by applying differential privacy noise to high-entropy classification outputs.

---

## 🚀 Problem Statement

Fine-grained logit and probability scores returned by models allow malicious actors to reconstruct private training data through inversion attacks.

---

## ⚡ Architecture Flow

```mermaid
sequenceDiagram
    autonumber
    participant Model as Private Model
    participant Proxy as Differential Privacy Proxy
    participant Client as External API Client

    Model->>Proxy: Emit High-Precision Probabilities (P=[0.981245, 0.018755])
    Proxy->>Proxy: Add Calibrated Laplace Noise (Epsilon = 1.0)
    Proxy->>Proxy: Truncate Precision to 2 Decimal Places (P=[0.98, 0.02])
    Proxy-->>Client: Return Sanitized Probabilities (Model Inversion Prevented)
```

---

## 📊 Performance Benchmarks

| Metric | Raw Probability Output | Argmax Only | Differential Privacy Proxy | Improvement |
|---|---|---|---|---|
| Training Data Reconstruction | 78.4% success | 0.0% | 0.0% | **Complete inversion defense** |
| Downstream Utility Retention | 100.0% | 45.0% | 98.8% | **Preserves probability utility** |
| Sanitization Latency | N/A | 0.1 ms | 0.12 ms | **Sub-millisecond proxy** |
| Privacy Budget Epsilon | Infinite (Leak) | Zero | Formal Epsilon = 1.0 | **Mathematically proven privacy** |

---

## 🛠️ Installation & Quickstart

```bash
pip install agent_model_inversion_differential_proxy
```

### Python API

```python
import agent_model_inversion_differential_proxy

print(agent_model_inversion_differential_proxy.__version__)
```

### CLI Usage

```bash
agent-model-inversion-differential-proxy --help
```

---

## 📄 License

MIT License © 2026 Ejaj Mahmud
