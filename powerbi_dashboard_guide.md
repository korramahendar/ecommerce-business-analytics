# Power BI Dashboard Guide

## Import
1. Open Power BI Desktop.
2. Get Data → Text/CSV.
3. Select `data/ecommerce_sales.csv`.
4. Load the table.

## Measures (DAX)

Total Sales = SUM(ecommerce_sales[Sales])

Total Profit = SUM(ecommerce_sales[Profit])

Total Orders = DISTINCTCOUNT(ecommerce_sales[Order_ID])

Units Sold = SUM(ecommerce_sales[Quantity])

Average Order Value = DIVIDE([Total Sales], [Total Orders])

Profit Margin = DIVIDE([Total Profit], [Total Sales])

## Visuals

### Overview
- KPI cards: Total Sales, Total Profit, Total Orders, Units Sold, Profit Margin
- Line chart: Order_Date vs Total Sales
- Column chart: Category vs Total Sales
- Bar chart: Region vs Total Sales
- Table: Product, Sales, Profit

### Business Insights
Use slicers for:
- Region
- Category
- Payment Method
- Order Date

## Portfolio tip
After building the dashboard, export 2–3 screenshots and add them to the GitHub README.
