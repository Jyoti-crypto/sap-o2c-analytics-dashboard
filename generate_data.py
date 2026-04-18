import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

random.seed(42)
np.random.seed(42)

# ─── Sales Orders ──────────────────────────────────────────────
customers = {
    'C001': 'Tata Steel Ltd',      'C002': 'Infosys Technologies',
    'C003': 'Reliance Industries', 'C004': 'Wipro Limited',
    'C005': 'HDFC Bank',           'C006': 'Mahindra & Mahindra',
    'C007': 'Larsen & Toubro',     'C008': 'Bajaj Auto',
    'C009': 'HCL Technologies',    'C010': 'ITC Limited'
}
products = {
    'P001': ('Enterprise License', 45000), 'P002': ('Data Analytics Suite', 32000),
    'P003': ('SAP S/4HANA Module',  78000), 'P004': ('Cloud Storage (TB)',   1200),
    'P005': ('SAP Training Pack',   15000), 'P006': ('BI Dashboard Tool',    28000),
    'P007': ('ERP Integration Kit', 55000), 'P008': ('HR Module Add-on',     22000),
}
regions   = ['North', 'South', 'East', 'West']
statuses  = ['Completed', 'Completed', 'Completed', 'Pending', 'In Progress']

orders = []
start = datetime(2024, 1, 1)
for i in range(200):
    order_date = start + timedelta(days=random.randint(0, 364))
    cust_id    = random.choice(list(customers.keys()))
    prod_id    = random.choice(list(products.keys()))
    prod_name, base_price = products[prod_id]
    qty        = random.randint(1, 20)
    discount   = round(random.uniform(0, 0.25), 2)
    unit_price = base_price * (1 - discount)
    total      = round(qty * unit_price, 2)
    status     = random.choice(statuses)
    region     = random.choice(regions)
    delivery   = order_date + timedelta(days=random.randint(3, 30))
    orders.append({
        'Order_ID':       f'SO-{2024000 + i}',
        'Order_Date':     order_date.strftime('%Y-%m-%d'),
        'Customer_ID':    cust_id,
        'Customer_Name':  customers[cust_id],
        'Product_ID':     prod_id,
        'Product_Name':   prod_name,
        'Quantity':       qty,
        'Unit_Price':     round(unit_price, 2),
        'Discount_Pct':   round(discount * 100, 1),
        'Total_Amount':   total,
        'Region':         region,
        'Status':         status,
        'Delivery_Date':  delivery.strftime('%Y-%m-%d'),
        'Month':          order_date.strftime('%B'),
        'Quarter':        f"Q{(order_date.month - 1) // 3 + 1}",
    })

df_orders = pd.DataFrame(orders)
df_orders.to_csv('/home/claude/sap_project/data/sap_sales_orders.csv', index=False)

# ─── Inventory ──────────────────────────────────────────────────
inventory = []
for pid, (pname, price) in products.items():
    stock = random.randint(50, 500)
    reorder = random.randint(20, 80)
    inventory.append({
        'Product_ID': pid, 'Product_Name': pname,
        'Unit_Price': price, 'Stock_Available': stock,
        'Reorder_Level': reorder, 'Stock_Status': 'Low' if stock < reorder * 1.5 else 'OK'
    })
pd.DataFrame(inventory).to_csv('/home/claude/sap_project/data/sap_inventory.csv', index=False)

print("✅ Data generated successfully")
print(f"   Sales Orders : {len(df_orders)} rows")
print(f"   Inventory    : {len(inventory)} rows")
print(df_orders.head(3).to_string())
