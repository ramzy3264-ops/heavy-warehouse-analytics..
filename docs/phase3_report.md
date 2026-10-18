# Phase 3: Supplier, Customer & Predictive Analytics

## 1. Executive Summary
Phase 3 transitions the project from descriptive inventory analysis into predictive modeling, operational risk assessment, and behavioral customer segmentation. By consolidating execution into a single automated master pipeline (`phase3_master_pipeline.py`), this phase successfully generates supplier performance metrics, RFM customer scores, and predictive reorder thresholds.

## 2. Core Modules & Outputs

| Analytical Domain | Target Task / Catalogue | Output File / Script | Key Insight / Methodology |
| :--- | :--- | :--- | :--- |
| **Warehouse Operations** | Throughput & Space Utilization (Cat. C) | `outputs/warehouse_throughput_metrics.csv` | Tracks branch-level transaction counts and total units moved. |
| **Supplier Analytics** | Supplier Contribution & Performance (Cat. D) | `outputs/supplier_performance_summary.csv` | Evaluates product distribution and unit cost metrics across active suppliers. |
| **Customer Analytics** | RFM Segmentation & Behavior (Cat. E) | `outputs/customer_rfm_segments.csv` | Computes Recency, Frequency, and Monetary scores using quantile ranking (1–4 scale). |
| **Predictive Forecasting** | Reorder Point & Safety Stock (Cat. F) | `outputs/inventory_forecast_reorder.csv` | Calculates daily demand variability and safety stock (95% service level) to mitigate stockouts. |

## 3. Automation & Execution
* **Master Script**: Fully executed via `scripts/phase3_master_pipeline.py`.
* **Data Integrity**: Automatically handles missing columns with intelligent fallbacks and simulated proxies for customer and supplier dimensions where applicable.

## 4. Next Steps
* Transition outputs and findings into **Phase 4: BI Dashboards, Anomaly Detection & Strategic Recommendations**.