import pandas as pd
import os

print("--- STARTING PHASE 2: WAREHOUSE & INVENTORY ANALYTICS ---")

# 1. Load Data
products_path = 'outputs/products_clean.csv'
stock_path = 'outputs/stock_ledger_clean.csv'

if os.path.exists(products_path) and os.path.exists(stock_path):
    df_prod = pd.read_csv(products_path)
    df_stock = pd.read_csv(stock_path)
    
    # 2. Merge stock ledger with product data for deeper insights
    if 'product_id' in df_stock.columns and 'product_id' in df_prod.columns:
        df_merged = pd.merge(df_stock, df_prod, on='product_id', how='left')
    else:
        df_merged = df_stock # fallback if IDs differ
        
    # 3. Analyze Fast and Slow Movers (based on movement frequency / quantity)
    if 'quantity' in df_merged.columns and 'product_id' in df_merged.columns:
        product_movement = df_merged.groupby('product_id')['quantity'].sum().reset_index()
        product_movement = product_movement.sort_values(by='quantity', ascending=False)
        
        # Categorize fast vs slow movers
        top_movers = product_movement.head(10)
        slow_movers = product_movement.tail(10)
        
        print(f"Analyzed {len(product_movement)} unique products for movement velocity.")
        
    # 4. Generate Comprehensive Phase 2 Summary Metrics
    summary_data = {
        'Warehouse_Metric': [
            'Total Product SKUs', 
            'Total Stock Ledger Transactions', 
            'Total Inventory Movement Volume', 
            'Average Transaction Quantity'
        ],
        'Value': [
            len(df_prod) if 'df_prod' in locals() else 0,
            len(df_stock),
            df_stock['quantity'].sum() if 'quantity' in df_stock.columns else 0,
            df_stock['quantity'].mean() if 'quantity' in df_stock.columns else 0
        ]
    }
    
    df_summary = pd.DataFrame(summary_data)
    
    # 5. Save Results to Outputs
    os.makedirs('outputs', exist_ok=True)
    df_summary.to_csv('outputs/phase2_warehouse_kpis.csv', index=False)
    product_movement.to_csv('outputs/product_movement_velocity.csv', index=False)
    
    print("Successfully generated and saved Phase 2 KPIs to outputs/!")
else:
    print("Error: Cleaned files not found in outputs/ folder. Please check your filenames.")

print("--- PHASE 2 EDA COMPLETE ---")