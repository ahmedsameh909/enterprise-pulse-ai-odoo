# EnterprisePulse AI — Odoo 18 Demand Forecasting & Inventory Risk Intelligence

![Odoo Version](https://img.shields.io/badge/Odoo-18.0-purple.svg)
![Python](https://img.shields.io/badge/Python-3.12-blue.svg)
![License](https://img.shields.io/badge/License-LGPL--3-green.svg)
![Status](https://img.shields.io/badge/Status-Graduation_Project-orange.svg)

**EnterprisePulse AI** is an advanced Odoo 18 custom module designed to enhance inventory decision-making and supply chain resilience. By generating synthetic ERP operational data and applying machine learning / deep learning algorithms, the system forecasts inventory demand, identifies stockout risks, and provides actionable insights directly within Odoo.

---

## ✨ Key Features

- 📈 **Demand Forecasting Engine**: Predictive models that forecast future product demand based on historical stock movements and order trends.
- ⚠️ **Inventory Risk & Stockout Analytics**: Real-time evaluation of reorder thresholds and lead times to flag high-risk inventory items before shortages occur.
- ⚡ **Synthetic ERP Data Generator**: Built-in engine for simulating realistic sales, purchase, and stock movement datasets for ML model training and baseline benchmarking.
- 🔌 **Seamless Integration**: Fully embedded into Odoo 18 with custom views, menu items, and secure API integration interfaces.

---

## 🏗️ Module Architecture & Directory Structure

```text
enterprise-pulse-ai-odoo/
├── models/             # Data models, risk scoring, and forecasting logic
├── views/              # Odoo XML views, forms, lists, and dashboards
├── security/           # Access rights (ir.model.access.csv)
├── controllers/        # REST/JSON-RPC API endpoints
├── __init__.py
└── __manifest__.py
