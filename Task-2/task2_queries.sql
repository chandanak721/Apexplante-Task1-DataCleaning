-- Business Questions
SELECT Category, SUM(Sales) FROM sales GROUP BY Category;
SELECT Month, SUM(Sales) FROM sales GROUP BY Month;
SELECT Region, SUM(Profit) FROM sales GROUP BY Region;
