

```markdown
# Heavy Warehouse & Supply Chain Analytics Portfolio
**End-to-End Enterprise Data Pipeline, Predictive Analytics & Executive BI Framework**

---

## Executive Overview
This repository contains a comprehensive, production-grade data analytics framework designed for heavy industrial warehouse operations[cite: 1, 2, 3, 4]. The project standardizes fragmented operational ledgers, executes statistical inventory modeling, builds predictive forecasting engines, automates anomaly detection, and delivers actionable executive strategy roadmaps[cite: 1, 2, 3, 4].

---

## Project Pipeline Architecture


```

```
                              PROJECT PIPELINE ARCHITECTURE

```

+-----------------------+      +-----------------------+      +-----------------------+      +-----------------------+
|        PHASE 1        | ---> |        PHASE 2        | ---> |        PHASE 3        | ---> |        PHASE 4        |
| Foundation & Profiling|      | Inventory & Warehouse |      | Predictive & Customer |      |   BI & Final Strategy |
+-----------------------+      +-----------------------+      +-----------------------+      +-----------------------+
|                              |                              |                              |
* Raw Cleaning                 * ABC Inventory                * Supplier Lead Times          * Z-score Outliers
* Standard Schemas             * Movement Velocity            * RFM Customer Tiers           * Risk Anomaly Log
* Core ETL Pipelines           * Throughput & Space           * Reorder Point Engine         * Visual BI Notebook

```

---

## Phase Breakdown & Deliverables

### **Phase 1: Foundation & Exploration**
* **Focus:** Data profiling, cleaning, integration, feature engineering, standard schemas, and foundational KPIs[cite: 1].
* **Key Tasks:**
  * Cleaned foundational supply chain and warehouse datasets, addressing invoice collisions and missing values[cite: 1].
  * Extracted clean numeric values, calculated product-level profit margins, and generated delivery status boolean flags[cite: 1].
  * Configured structured project directories (`/docs`, `/scripts`, `/outputs`, `/notebooks`)[cite: 1].
* **Core Artifacts:** `scripts/01_data_cleaning_pipeline.py`, cleaned baseline files in `outputs/`[cite: 1].

---

### **Phase 2: Core Product, Inventory & Warehouse Analytics**
* **Focus:** Product performance, fast/slow movers, turnover rates, stock health, space utilization, and throughput efficiency[cite: 2].
* **Key Tasks:**
  * Processed stock ledger transactions across product SKUs[cite: 2].
  * Quantified inventory throughput, movement velocity, and overall stock health[cite: 2].
  * Classified SKUs into high-velocity ("fast movers") and low-velocity ("slow movers") items to improve slotting strategies[cite: 2].
* **Core Artifacts:** `scripts/phase2_eda.py`, `outputs/phase2_warehouse_kpis.csv`, `outputs/phase2_summary_metrics.csv`, product movement velocity logs[cite: 2].

---

### **Phase 3: Supplier, Customer & Predictive Analytics**
* **Focus:** Supplier reliability & risk scoring, RFM customer segmentation, demand forecasting, stockout & reorder prediction[cite: 3].
* **Key Tasks:**
  * **Warehouse Operations:** Tracked branch-level transaction counts and total units moved (`outputs/warehouse_throughput_metrics.csv`)[cite: 3].
  * **Supplier Analytics:** Evaluated product distribution and unit cost metrics across active suppliers (`outputs/supplier_performance_summary.csv`)[cite: 3].
  * **Customer Analytics:** Computed Recency, Frequency, and Monetary scores using quantile ranking on a 1–4 scale (`outputs/customer_rfm_segments.csv`)[cite: 3].
  * **Predictive Forecasting:** Calculated daily demand variability and safety stock at a 95% service level (`outputs/inventory_forecast_reorder.csv`)[cite: 3].
* **Core Artifacts:** `scripts/phase3_master_pipeline.py`, `outputs/customer_rfm_segments.csv`, `outputs/inventory_forecast_reorder.csv`, `docs/phase3_report.md`[cite: 3].

---

### **Phase 4: BI, Strategy & Final Delivery**
* **Focus:** Interactive dashboards, KPI frameworks, statistical anomaly detection, executive strategy recommendations, and capstone presentation[cite: 4].
* **Key Tasks:**
  * **Risk & Anomaly Detection:** Programmatically flagged inventory spikes, shrinkage, and transaction outliers using Z-Score statistical modeling ($\pm2.5\sigma$) and negative quantity filters (`outputs/inventory_anomalies.csv`)[cite: 4].
  * **Visual Analytics & BI:** Designed an in-repo Jupyter visualization notebook (`notebooks/phase4_visualizations.ipynb`) displaying RFM clusters and reorder threshold distributions[cite: 4].
  * **Executive Strategy Framework:** Formulated actionable supply chain roadmap recommendations focusing on inventory control, supplier risk mitigation, and customer retention (`docs/final_strategy_report.md`)[cite: 4].
* **Core Artifacts:** `scripts/phase4_risk_anomaly.py`, `outputs/inventory_anomalies.csv`, `notebooks/phase4_visualizations.ipynb`, `docs/phase4_report.md`, `docs/final_strategy_report.md`[cite: 4].

---

## Repository Structure

```text
heavy-warehouse-analytics/
├── README.md                           <- Executive portfolio overview & phase mapping
├── branches.csv                        <- Raw branch location ledger
├── customers.csv                       <- Raw customer master data
├── inventory_master.csv                <- Raw inventory catalog data
├── invoices.csv                        <- Raw financial invoice ledger
├── payments.csv                        <- Raw transaction payment records
├── products.csv                        <- Raw product specification table
├── purchase_orders_header.csv          <- Raw purchase orders header data
├── purchase_orders_lines.csv           <- Raw purchase orders line items
├── sales_orders_header.csv             <- Raw sales orders header data
├── sales_orders_lines.csv              <- Raw sales orders line items
├── stock_ledger.csv                    <- Raw inventory movement stock ledger
├── suppliers.csv                       <- Raw supplier directory records
├── scripts/
│   ├── phase1_data_cleaning_pipeline.py <- Foundation profiling & cleaning pipeline
│   ├── phase2_eda.py                   <- Inventory movement & throughput analytics
│   ├── phase3_master_pipeline.py       <- RFM segmentation & predictive ROP engine
│   └── phase4_risk_anomaly.py          <- Z-score statistical risk & anomaly script
├── outputs/
│   ├── branches_clean.csv              <- Standardized branch data
│   ├── customer_rfm_segments.csv       <- Customer RFM scores & category assignments
│   ├── inventory_anomalies.csv         <- Flagged transaction anomalies & shrinkage logs
│   ├── inventory_forecast_reorder.csv  <- Safety stock levels & calculated reorder points
│   ├── invoices_clean.csv              <- Standardized invoice data
│   ├── phase2_summary_metrics.csv      <- Summary operational metrics
│   ├── phase2_warehouse_kpis.csv       <- Core warehouse metric benchmarks
│   ├── products_clean.csv              <- Standardized product records
│   ├── product_movement_velocity.csv   <- SKU velocity classification log
│   ├── sales_headers_clean.csv         <- Standardized sales headers
│   ├── stock_ledger_clean.csv          <- Standardized transactional stock ledger
│   ├── supplier_performance_summary.csv<- Vendor reliability & cost metrics
│   └── warehouse_throughput_metrics.csv<- Branch transaction throughput log
├── notebooks/
│   └── phase4_visualizations.ipynb     <- Native GitHub-rendered BI graphics & charts
└── docs/
    ├── phase1_report.md                <- Foundation & cleaning report
    ├── phase2_report.md                <- Inventory & warehouse analytics report
    ├── phase3_report.md                <- Predictive analytics & vendor technical report
    ├── phase4_report.md                <- Risk detection & visual analytics report
    

---

## Key Performance Indicator (KPI) Framework

| Category | Indicator | Definition / Target Metric |
| --- | --- | --- |
| **Inventory** | **Turnover Ratio** | Annual Cost of Goods Sold (COGS) / Average Inventory Value |
| **Operations** | **Safety Stock Adherence** | Percentage of SKUs maintaining stock above calculated ROP |
| **Supplier** | **On-Time In-Full (OTIF)** | Percentage of purchase orders delivered without delay or defect |
| **Customer** | **RFM Value Tiering** | Active accounts grouped by purchase frequency and volume via quantile scoring |
| **Risk** | **Anomaly Rate** | Percentage of transactions exceeding $\pm2.5\sigma$ movement volume or negative quantity limits |

---

## How to Run the Pipeline

### **1. Prerequisites**

Ensure Python 3.9+ and required packages are installed:

```bash
pip install pandas numpy matplotlib seaborn openpyxl

```

### **2. Execute Master Analytics Engine**

Run the core pipelines sequentially to generate clean data, predictive outputs, and anomaly logs:

```bash
# Run Phase 1 Data Cleaning Pipeline
python scripts/01_data_cleaning_pipeline.py

# Run Phase 2 EDA Script
python scripts/phase2_eda.py

# Run Phase 3 Predictive & Customer Pipeline
python scripts/phase3_master_pipeline.py

# Run Phase 4 Anomaly Detection Engine
python scripts/phase4_risk_anomaly.py

```

### **3. Review Visualizations**

Open `notebooks/phase4_visualizations.ipynb` directly on GitHub to view interactive plots, scatter charts, and reorder point distributions without needing local server execution.

---

## License & Attribution

Designed and built as part of an end-to-end Enterprise Supply Chain Data Analytics Portfolio.

```

```# heavy-warehouse-analytics
Heavy Supplier & Warehouse Analytics Portfolio
