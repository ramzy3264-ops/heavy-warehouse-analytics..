# Week 1 Sprint Report: Phase 1 (Foundation & Exploration)
**Project:** Heavy Supplier & Warehouse Analytics  
**Sprint Focus:** Repository Architecture, Data Ingestion, Cleaning Pipeline, and Initial Feature Engineering  

---

## 1. Executive Summary
During Week 1, the core data foundation and repository structure for the Heavy Supplier & Warehouse Analytics project were successfully established. Working within an agile sprint framework, the primary objectives were setting up the environment, resolving raw data format and pathing traps, and building an automated Python data cleaning pipeline to process 12 foundational supply chain and warehouse datasets.

---

## 2. Repository & Environment Architecture
* **Directory Structure Setup:** Configured structured project directories to maintain clean separation of concerns:
  * `/docs` — Documentation, sprint reports, and field references.
  * `/scripts` — Core Python automation and data transformation scripts.
  * `/outputs` — Cleaned and processed dataset artifacts.
  * `/notebooks` — Exploratory data analysis scratchpads.
* **Environment Configuration:** Installed and verified essential Python analytical libraries (`pandas`, `numpy`, and `openpyxl`).
* **Dataset Ingestion:** Integrated 12 core operational files (`branches`, `customers`, `inventory_master`, `invoices`, `payments`, `products`, `purchase_orders_header`, `purchase_orders_lines`, `sales_orders_header`, `sales_orders_lines`, `stock_ledger`, and `suppliers`).

---

## 3. Data Cleaning & Pipeline Implementation (`01_data_cleaning_pipeline.py`)
Successfully built and executed an automated data cleaning pipeline to tackle key operational data traps:
* **Invoice Collision Resolution:** Addressed duplicate invoice entries by filtering unique sales order IDs (`so_id`) to maintain financial integrity.
* **Missing Value Imputation:** Handled missing data points and gaps in running balance calculations using safe imputation (`.fillna(0)`).
* **Feature Engineering & Transformation:**
  * Extracted clean numeric values from unstructured text strings (e.g., warehouse capacity metrics).
  * Calculated product-level profit margins using the formula: $\frac{\text{Unit Price} - \text{Unit Cost}}{\text{Unit Price}}$.
  * Generated delivery status boolean flags (`is_delivered`) from raw order status strings.

---

## 4. Key Performance Indicators (KPIs) Established
* **Product Profit Margin:** Tracking margin health across product lines.
* **Order Fulfillment Status:** Monitoring delivered versus incomplete sales orders.
* **Warehouse Capacity Metric:** Normalizing storage sizing for upcoming utilization analysis.

---

## 5. Next Steps (Week 2 - Phase 2 Preview)
* Transitioning from Phase 1 (Data Foundation) to **Phase 2 (Core Product, Inventory & Warehouse Analytics)**.
* Focus areas: Fast/slow-moving product identification, inventory turnover ratios, stock health assessment, and ABC / Pareto product classification.