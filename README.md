# tZERO Practice: Tokenized Asset Ledger API

A high-performance, API-first backend service built to simulate the lifecycle of digital assets, focusing on secure settlement and immutable transaction logging.

## 🚀 Overview
This project demonstrates the core engineering principles required for regulated digital asset infrastructure. It provides a RESTful interface for token issuance and peer-to-peer asset settlement.

### Key Fintech Features
* **Atomic Settlement:** Logic ensuring balances are updated simultaneously to prevent double-spending.
* **Immutable Ledger:** Every trade is hashed using SHA-256 to create a "tamper-evident" audit trail, mimicking blockchain architecture.
* **API-First Design:** Built with FastAPI to provide automatic OpenAPI/Swagger documentation for institutional integrations.

## 🛠 Tech Stack
* **Language:** Python 3.10
* **Framework:** FastAPI (RESTful API)
* **Containerization:** Docker (Standardized deployment)
* **AI-Assisted Dev:** Developed using GitHub Copilot for unit testing and boilerplate optimization.

## 📦 Getting Started

### Using Docker (Preferred)
To run the containerized service:
```bash
docker build -t tzero-ledger .
docker run -p 8000:8000 tzero-ledger