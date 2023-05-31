SELECT category, COUNT(*) as item_count
FROM items
GROUP BY category;
