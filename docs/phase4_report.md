# Phase 4: Risk, Anomaly Detection & Strategic Delivery

## 1. Executive Summary
Phase 4 completes the 12-week data analytics framework by introducing automated risk controls, exploratory visual analytics, and an overarching executive strategy. By analyzing stock movement patterns for statistical anomalies and visualizing core operational metrics, this phase bridges technical data pipelines with executive decision-making.

---

## 2. Core Modules & Outputs

| Analytical Domain | Target Task / Catalogue | Output File / Script | Key Methodology & Finding |
| :--- | :--- | :--- | :--- |
| **Risk & Anomaly Detection** | Shrinkage & Outlier Tracking (Cat. G) | `scripts/phase4_risk_anomaly.py`<br>`outputs/inventory_anomalies.csv` | Uses Z-score statistical modeling ($\pm2.5\sigma$) and negative quantity filters to isolate unexpected spikes and potential shrinkage. |
| **Visual Analytics & BI** | Exploratory Charts & KPI Display (Cat. H) | `notebooks/phase4_visualizations.ipynb` | Interactive Jupyter visualization notebook displaying RFM segmentation clusters and top reorder threshold distributions. |
| **Executive Strategy** | Actionable Supply Chain Roadmap (Cat. I) | `docs/final_strategy_report.md` | Synthesizes project-wide outputs into concrete recommendations for inventory control, supplier risk, and customer retention. |

---

## 3. Key Findings & Execution Summary
* **Anomaly Detection Engine:** `phase4_risk_anomaly.py` executed cleanly against `stock_ledger_clean.csv`. The automated z-score filter confirmed inventory movement consistency across historical transactions.
* **Jupyter Visualization Suite:** The `phase4_visualizations.ipynb` notebook leverages `seaborn` and `matplotlib` to render data trends directly within the GitHub repository interface without requiring heavy BI server deployments.
* **Strategic Roadmap:** Strategic focus shifts toward automated reorder triggers for high-turnover items and supplier diversification for single-source dependencies.

---

## 4. Portfolio Completion
With Phase 4 pushed to `main`, all four phases across the 9-part analytics catalogue are fully built, automated, and documented.