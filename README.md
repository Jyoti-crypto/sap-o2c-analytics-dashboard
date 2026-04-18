# SAP Order-to-Cash (O2C) Analytics Dashboard
### Capstone Project | Jyoti Kumari | Roll No: 2305297 | CSE

---

## 📌 Project Overview
This project simulates and analyses an SAP Order-to-Cash (O2C) business cycle using Python.
It generates realistic SAP-style transactional data and builds a complete analytics dashboard
with KPI metrics, revenue trends, customer analysis, and regional performance charts.

---

## 🗂️ Project Structure
```
sap_project/
│
├── data/
│   ├── generate_data.py          # Generates SAP-style sales & inventory CSV
│   ├── sap_sales_orders.csv      # 200 simulated O2C sales orders
│   └── sap_inventory.csv         # Product inventory data
│
├── charts/
│   ├── chart1_monthly_revenue.png
│   ├── chart2_top_customers.png
│   ├── chart3_order_status.png
│   ├── chart4_regional_revenue.png
│   ├── chart5_product_revenue.png
│   ├── chart6_quarterly.png
│   └── dashboard_overview.png    ← Main dashboard screenshot
│
├── analytics_dashboard.py        # Main analysis + chart generation script
├── generate_pdf.py               # PDF documentation generator
├── Project_Documentation.pdf     # Final project report (submit this)
└── README.md                     # This file
```

---

## 🚀 How to Run

### 1. Install Dependencies
```bash
pip install pandas matplotlib seaborn reportlab pillow numpy
```

### 2. Generate Data
```bash
python data/generate_data.py
```

### 3. Run Analytics Dashboard
```bash
python analytics_dashboard.py
```

### 4. Generate PDF Documentation
```bash
python generate_pdf.py
```

---

## 📊 Key Features
- Simulates 200 SAP O2C sales orders with customers, products, regions, discounts
- 6 analytical charts: Monthly Revenue, Quarterly Performance, Top Customers,
  Regional Revenue, Product Breakdown, Order Status
- Combined KPI dashboard showing Total Revenue, Order Count, Avg Order Value, Completion Rate
- Professional PDF report (4–5 pages, A4, Arial font, page numbers)

---

## 🔧 Tech Stack
| Tool | Purpose |
|------|---------|
| Python 3.x | Core programming language |
| Pandas | Data manipulation and aggregation |
| Matplotlib | Chart and dashboard generation |
| Seaborn | Enhanced visualisation styling |
| NumPy | Numerical data generation |
| ReportLab | PDF documentation creation |

---

## 📈 Business Insights Uncovered
- Total FY 2024 Revenue: ₹70.5 Million
- 200 Sales Orders processed across 10 customers
- Average Order Value: ₹352,643
- Order Completion Rate: 62.5%
- Top Customer: ITC Limited
- Best Performing Product: SAP S/4HANA Module

---

**Student:** Jyoti Kumari | **Roll No:** 2305297 | **Branch:** CSE  
**Program:** SAP — Data Analytics & Engineering | **Institution:** KIIT
