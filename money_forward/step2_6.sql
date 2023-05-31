SELECT id, name, price
FROM items
WHERE category = 0
ORDER BY price, id
LIMIT 20;
