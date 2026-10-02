import pandas as pd
import numpy as np
import os

os.makedirs('outputs', exist_ok=True)

print("--- STEP 1: LOADING CSV DATA ---")
branches = pd.read_csv('branches.csv')
customers = pd.read_csv('customers.csv')
products = pd.read_csv('products.csv')
invoices = pd.read_csv('invoices.csv')
payments = pd.read_csv('payments.csv')
purchase_headers = pd.read_csv('purchase_orders_header.csv')
purchase_lines = pd.read_csv('purchase_orders_lines.csv')
sales_headers = pd.read_csv('sales_orders_header.csv')
sales_lines = pd.read_csv('sales_orders_lines.csv')
stock_ledger = pd.read_csv('stock_ledger.csv')
inventory_master = pd.read_csv('inventory_master.csv')
suppliers = pd.read_csv('suppliers.csv')

print("--- STEP 2: CLEANING MASTER DATA ---")
if 'warehouse_capacity' in branches.columns:
    branches['warehouse_capacity_num'] = branches['warehouse_capacity'].astype(str).str.extract(r'(\d+)')[0].astype(float)

if 'unit_cost' in products.columns and 'unit_price' in products.columns:
    products['computed_margin'] = (products['unit_price'] - products['unit_cost']) / products['unit_price']

print("--- STEP 3: RESOLVING DATA TRAPS ---")
sales_headers['is_delivered'] = sales_headers['order_status'].str.lower() == 'delivered'
invoices_clean = invoices.drop_duplicates(subset=['so_id']).copy()
payments['payment_row_id'] = range(len(payments))

if 'running_balance' in stock_ledger.columns:
    stock_ledger = stock_ledger.sort_values(by=['product_id', 'branch_id', 'movement_date'])
    stock_ledger['derived_signed_qty'] = stock_ledger.groupby(['product_id', 'branch_id'])['running_balance'].diff().fillna(0)

# Save cleaned files as CSVs in outputs folder
branches.to_csv('outputs/branches_clean.csv', index=False)
products.to_csv('outputs/products_clean.csv', index=False)
sales_headers.to_csv('outputs/sales_headers_clean.csv', index=False)
invoices_clean.to_csv('outputs/invoices_clean.csv', index=False)
stock_ledger.to_csv('outputs/stock_ledger_clean.csv', index=False)

print("--- PHASE 1 PIPELINE COMPLETED SUCCESSFULLY ---")