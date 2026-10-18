import pandas as pd
import numpy as np
import os

print("==================================================")
print("--- RUNNING PHASE 4: RISK & ANOMALY DETECTION ---")
print("==================================================")

stock_path = 'outputs/stock_ledger_clean.csv'

if os.path.exists(stock_path):
    df_stock = pd.read_csv(stock_path)
    
    # 1. Detect Inventory Movement Anomalies (Catalogue G)
    # Using Z-score method on quantities to find unusual spikes or negative adjustments (shrinkage)
    mean_qty = df_stock['quantity'].mean()
    std_qty = df_stock['quantity'].std()
    
    if std_qty > 0:
        df_stock['z_score'] = (df_stock['quantity'] - mean_qty) / std_qty
    else:
        df_stock['z_score'] = 0
        
    # Flag transactions where absolute Z-score > 2.5 (outliers) or quantity < 0 (potential shrinkage/returns)
    anomalies = df_stock[(df_stock['z_score'].abs() > 2.5) | (df_stock['quantity'] < 0)].copy()
    
    # 2. Save Anomaly Log
    os.makedirs('outputs', exist_ok=True)
    anomalies.to_csv('outputs/inventory_anomalies.csv', index=False)
    
    print(f"Anomaly Detection Complete! Flagged {len(anomalies)} anomalous transactions.")
    print("Saved to outputs/inventory_anomalies.csv")
    print("==================================================")
else:
    print("Error: stock_ledger_clean.csv not found in outputs/ folder.")