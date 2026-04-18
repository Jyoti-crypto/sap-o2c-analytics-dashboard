"""
SAP Order-to-Cash (O2C) Analytics Dashboard
Capstone Project | Jyoti Kumari | Roll No: 2305297 | CSE
Windows Compatible Version - Uses relative paths
"""

import os
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import warnings
warnings.filterwarnings('ignore')

# ── Setup folders using relative paths ─────────────────
BASE   = os.path.dirname(os.path.abspath(__file__))
DATA   = os.path.join(BASE, 'data')
CHARTS = os.path.join(BASE, 'charts')

os.makedirs(DATA,   exist_ok=True)
os.makedirs(CHARTS, exist_ok=True)

# ══════════════════════════════════════════════════════
# STEP 1 — GENERATE DATA
# ══════════════════════════════════════════════════════
import random
from datetime import datetime, timedelta

random.seed(42)
np.random.seed(42)

customers = {
    'C001': 'Tata Steel Ltd',      'C002': 'Infosys Technologies',
    'C003': 'Reliance Industries', 'C004': 'Wipro Limited',
    'C005': 'HDFC Bank',           'C006': 'Mahindra & Mahindra',
    'C007': 'Larsen & Toubro',     'C008': 'Bajaj Auto',
    'C009': 'HCL Technologies',    'C010': 'ITC Limited'
}
products = {
    'P001': ('Enterprise License',   45000),
    'P002': ('Data Analytics Suite', 32000),
    'P003': ('SAP S/4HANA Module',   78000),
    'P004': ('Cloud Storage (TB)',    1200),
    'P005': ('SAP Training Pack',    15000),
    'P006': ('BI Dashboard Tool',    28000),
    'P007': ('ERP Integration Kit',  55000),
    'P008': ('HR Module Add-on',     22000),
}
regions  = ['North', 'South', 'East', 'West']
statuses = ['Completed', 'Completed', 'Completed', 'Pending', 'In Progress']

orders = []
start  = datetime(2024, 1, 1)
for i in range(200):
    order_date          = start + timedelta(days=random.randint(0, 364))
    cust_id             = random.choice(list(customers.keys()))
    prod_id             = random.choice(list(products.keys()))
    prod_name, base_price = products[prod_id]
    qty                 = random.randint(1, 20)
    discount            = round(random.uniform(0, 0.25), 2)
    unit_price          = base_price * (1 - discount)
    total               = round(qty * unit_price, 2)
    delivery            = order_date + timedelta(days=random.randint(3, 30))
    orders.append({
        'Order_ID':      f'SO-{2024000 + i}',
        'Order_Date':    order_date.strftime('%Y-%m-%d'),
        'Customer_ID':   cust_id,
        'Customer_Name': customers[cust_id],
        'Product_ID':    prod_id,
        'Product_Name':  prod_name,
        'Quantity':      qty,
        'Unit_Price':    round(unit_price, 2),
        'Discount_Pct':  round(discount * 100, 1),
        'Total_Amount':  total,
        'Region':        random.choice(regions),
        'Status':        random.choice(statuses),
        'Delivery_Date': delivery.strftime('%Y-%m-%d'),
        'Month':         order_date.strftime('%B'),
        'Quarter':       f"Q{(order_date.month - 1) // 3 + 1}",
    })

df = pd.DataFrame(orders)
df.to_csv(os.path.join(DATA, 'sap_sales_orders.csv'), index=False)

inventory = []
for pid, (pname, price) in products.items():
    stock   = random.randint(50, 500)
    reorder = random.randint(20, 80)
    inventory.append({
        'Product_ID': pid, 'Product_Name': pname,
        'Unit_Price': price, 'Stock_Available': stock,
        'Reorder_Level': reorder,
        'Stock_Status': 'Low' if stock < reorder * 1.5 else 'OK'
    })
pd.DataFrame(inventory).to_csv(os.path.join(DATA, 'sap_inventory.csv'), index=False)
print("✅ Data generated successfully")

# ══════════════════════════════════════════════════════
# STEP 2 — KPI SUMMARY
# ══════════════════════════════════════════════════════
total_revenue   = df['Total_Amount'].sum()
total_orders    = len(df)
avg_order_value = df['Total_Amount'].mean()
completion_rate = (df['Status'] == 'Completed').mean() * 100
top_customer    = df.groupby('Customer_Name')['Total_Amount'].sum().idxmax()

print("=" * 55)
print("  SAP O2C ANALYTICS - KEY METRICS")
print("=" * 55)
print(f"  Total Revenue    : Rs {total_revenue:>15,.0f}")
print(f"  Total Orders     : {total_orders:>18}")
print(f"  Avg Order Value  : Rs {avg_order_value:>15,.0f}")
print(f"  Completion Rate  : {completion_rate:>17.1f}%")
print(f"  Top Customer     : {top_customer}")
print("=" * 55)

# ── Colours ────────────────────────────────────────────
SAP_BLUE  = '#003366'
SAP_TEAL  = '#007DB8'
SAP_GOLD  = '#F0AB00'
SAP_GREEN = '#2D8653'
SAP_RED   = '#D32F2F'
PALETTE   = [SAP_BLUE, SAP_TEAL, SAP_GOLD, SAP_GREEN, SAP_RED,
             '#6A0DAD', '#FF6600', '#00897B']

plt.rcParams.update({
    'font.family':      'DejaVu Sans',
    'axes.spines.top':  False,
    'axes.spines.right':False,
    'figure.dpi':       150,
})

# ══════════════════════════════════════════════════════
# CHART 1 — Monthly Revenue
# ══════════════════════════════════════════════════════
month_order = ['January','February','March','April','May','June',
               'July','August','September','October','November','December']
monthly = df.groupby('Month')['Total_Amount'].sum().reindex(month_order).dropna()

fig, ax = plt.subplots(figsize=(12, 5))
bars = ax.bar(range(len(monthly)), monthly.values, color=SAP_TEAL, alpha=0.85, width=0.6, zorder=3)
ax.plot(range(len(monthly)), monthly.values, color=SAP_GOLD, marker='o', linewidth=2.5, markersize=7, zorder=4)
for bar, val in zip(bars, monthly.values):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 80000,
            f'Rs{val/1e6:.1f}M', ha='center', va='bottom', fontsize=8, color=SAP_BLUE, fontweight='bold')
ax.set_title('Monthly Revenue Trend - FY 2024', fontsize=14, fontweight='bold', color=SAP_BLUE)
ax.set_xlabel('Month'); ax.set_ylabel('Revenue (Rs)')
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'Rs{x/1e6:.1f}M'))
ax.set_xticks(range(len(monthly)))
ax.set_xticklabels([m[:3] for m in monthly.index], fontsize=10)
ax.grid(axis='y', linestyle='--', alpha=0.4)
plt.tight_layout()
plt.savefig(os.path.join(CHARTS, 'chart1_monthly_revenue.png'), bbox_inches='tight')
plt.close()
print("✅ Chart 1 saved")

# ══════════════════════════════════════════════════════
# CHART 2 — Top 5 Customers
# ══════════════════════════════════════════════════════
top_customers = df.groupby('Customer_Name')['Total_Amount'].sum().nlargest(5).sort_values()
fig, ax = plt.subplots(figsize=(10, 5))
bars = ax.barh(top_customers.index, top_customers.values, color=PALETTE[:5], height=0.55, zorder=3)
for bar, val in zip(bars, top_customers.values):
    ax.text(val + 50000, bar.get_y() + bar.get_height()/2,
            f'Rs{val/1e6:.2f}M', va='center', fontsize=9, fontweight='bold', color=SAP_BLUE)
ax.set_title('Top 5 Customers by Total Revenue', fontsize=14, fontweight='bold', color=SAP_BLUE)
ax.set_xlabel('Total Revenue (Rs)')
ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'Rs{x/1e6:.1f}M'))
ax.grid(axis='x', linestyle='--', alpha=0.4)
plt.tight_layout()
plt.savefig(os.path.join(CHARTS, 'chart2_top_customers.png'), bbox_inches='tight')
plt.close()
print("✅ Chart 2 saved")

# ══════════════════════════════════════════════════════
# CHART 3 — Order Status Pie
# ══════════════════════════════════════════════════════
status_counts = df['Status'].value_counts()
fig, ax = plt.subplots(figsize=(7, 6))
ax.pie(status_counts.values, labels=status_counts.index,
       autopct='%1.1f%%', colors=[SAP_GREEN, SAP_GOLD, SAP_TEAL],
       explode=[0.03]*len(status_counts), startangle=140,
       textprops={'fontsize': 11},
       wedgeprops={'edgecolor': 'white', 'linewidth': 2})
ax.set_title('Order Status Distribution', fontsize=14, fontweight='bold', color=SAP_BLUE)
plt.tight_layout()
plt.savefig(os.path.join(CHARTS, 'chart3_order_status.png'), bbox_inches='tight')
plt.close()
print("✅ Chart 3 saved")

# ══════════════════════════════════════════════════════
# CHART 4 — Regional Revenue
# ══════════════════════════════════════════════════════
regional = df.groupby('Region')['Total_Amount'].sum().sort_values(ascending=False)
fig, ax = plt.subplots(figsize=(8, 5))
bars = ax.bar(regional.index, regional.values,
              color=[SAP_BLUE, SAP_TEAL, SAP_GOLD, SAP_GREEN], width=0.5, zorder=3)
for bar, val in zip(bars, regional.values):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 100000,
            f'Rs{val/1e6:.2f}M', ha='center', fontsize=10, fontweight='bold', color=SAP_BLUE)
ax.set_title('Revenue by Region', fontsize=14, fontweight='bold', color=SAP_BLUE)
ax.set_xlabel('Region'); ax.set_ylabel('Revenue (Rs)')
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'Rs{x/1e6:.1f}M'))
ax.grid(axis='y', linestyle='--', alpha=0.4)
plt.tight_layout()
plt.savefig(os.path.join(CHARTS, 'chart4_regional_revenue.png'), bbox_inches='tight')
plt.close()
print("✅ Chart 4 saved")

# ══════════════════════════════════════════════════════
# CHART 5 — Product Revenue
# ══════════════════════════════════════════════════════
prod_rev = df.groupby('Product_Name')['Total_Amount'].sum().sort_values()
fig, ax = plt.subplots(figsize=(11, 5))
colors_p = plt.cm.Blues(np.linspace(0.4, 0.9, len(prod_rev)))
bars = ax.barh(prod_rev.index, prod_rev.values, color=colors_p, height=0.6, zorder=3)
for bar, val in zip(bars, prod_rev.values):
    ax.text(val + 50000, bar.get_y() + bar.get_height()/2,
            f'Rs{val/1e6:.2f}M', va='center', fontsize=9, fontweight='bold', color=SAP_BLUE)
ax.set_title('Revenue by Product', fontsize=14, fontweight='bold', color=SAP_BLUE)
ax.set_xlabel('Total Revenue (Rs)')
ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'Rs{x/1e6:.1f}M'))
ax.grid(axis='x', linestyle='--', alpha=0.4)
plt.tight_layout()
plt.savefig(os.path.join(CHARTS, 'chart5_product_revenue.png'), bbox_inches='tight')
plt.close()
print("✅ Chart 5 saved")

# ══════════════════════════════════════════════════════
# CHART 6 — Quarterly Performance
# ══════════════════════════════════════════════════════
quarterly = df.groupby('Quarter').agg(
    Revenue=('Total_Amount','sum'), Orders=('Order_ID','count')).reset_index()
fig, ax1 = plt.subplots(figsize=(8, 5))
ax2 = ax1.twinx()
bars = ax1.bar(quarterly['Quarter'], quarterly['Revenue'],
               color=SAP_TEAL, alpha=0.75, width=0.4, zorder=3, label='Revenue')
ax2.plot(quarterly['Quarter'], quarterly['Orders'],
         color=SAP_GOLD, marker='D', linewidth=2.5, markersize=9, zorder=4, label='Orders')
for bar, val in zip(bars, quarterly['Revenue']):
    ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 100000,
             f'Rs{val/1e6:.1f}M', ha='center', fontsize=9, fontweight='bold', color=SAP_BLUE)
ax1.set_title('Quarterly Revenue vs Order Volume', fontsize=14, fontweight='bold', color=SAP_BLUE)
ax1.set_xlabel('Quarter')
ax1.set_ylabel('Revenue (Rs)', color=SAP_TEAL)
ax2.set_ylabel('Number of Orders', color=SAP_GOLD)
ax1.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'Rs{x/1e6:.1f}M'))
ax1.grid(axis='y', linestyle='--', alpha=0.3)
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper left', fontsize=10)
plt.tight_layout()
plt.savefig(os.path.join(CHARTS, 'chart6_quarterly.png'), bbox_inches='tight')
plt.close()
print("✅ Chart 6 saved")

# ══════════════════════════════════════════════════════
# DASHBOARD — Combined Overview
# ══════════════════════════════════════════════════════
from PIL import Image as PILImage

fig = plt.figure(figsize=(16, 10))
fig.patch.set_facecolor('#F5F7FA')

ax_h = fig.add_axes([0, 0.92, 1, 0.08])
ax_h.set_facecolor(SAP_BLUE)
ax_h.text(0.5, 0.55, 'SAP Order-to-Cash (O2C) Analytics Dashboard',
          ha='center', va='center', fontsize=18, fontweight='bold', color='white',
          transform=ax_h.transAxes)
ax_h.text(0.5, 0.15, 'Capstone Project | Jyoti Kumari | Roll No: 2305297 | CSE | FY 2024',
          ha='center', va='center', fontsize=10, color='#AACDE8', transform=ax_h.transAxes)
ax_h.axis('off')

kpis = [
    (f'Rs{total_revenue/1e6:.1f}M', 'Total Revenue',    SAP_BLUE),
    (f'{total_orders}',             'Total Orders',      SAP_TEAL),
    (f'Rs{avg_order_value/1e3:.0f}K','Avg Order Value', SAP_GREEN),
    (f'{completion_rate:.0f}%',     'Completion Rate',   SAP_GOLD),
]
for i, (val, label, color) in enumerate(kpis):
    ax_k = fig.add_axes([0.02 + i * 0.245, 0.76, 0.22, 0.14])
    ax_k.set_facecolor(color)
    ax_k.text(0.5, 0.6, val,   ha='center', va='center', fontsize=22,
              fontweight='bold', color='white', transform=ax_k.transAxes)
    ax_k.text(0.5, 0.2, label, ha='center', va='center', fontsize=10,
              color='white', alpha=0.9, transform=ax_k.transAxes)
    ax_k.axis('off')

positions   = [[0.01,0.39,0.48,0.35],[0.51,0.39,0.48,0.35],
               [0.01,0.01,0.31,0.35],[0.34,0.01,0.31,0.35],[0.67,0.01,0.31,0.35]]
chart_files = [
    os.path.join(CHARTS, 'chart1_monthly_revenue.png'),
    os.path.join(CHARTS, 'chart6_quarterly.png'),
    os.path.join(CHARTS, 'chart3_order_status.png'),
    os.path.join(CHARTS, 'chart4_regional_revenue.png'),
    os.path.join(CHARTS, 'chart2_top_customers.png'),
]
for pos, cfile in zip(positions, chart_files):
    ax = fig.add_axes(pos)
    ax.imshow(np.array(PILImage.open(cfile)))
    ax.axis('off')

plt.savefig(os.path.join(CHARTS, 'dashboard_overview.png'),
            bbox_inches='tight', dpi=150, facecolor='#F5F7FA')
plt.close()
print("✅ Dashboard saved")
print("\n🎉 All done! Check the 'charts' folder for your outputs.")
