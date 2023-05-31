SELECT prefecture
FROM shops
GROUP BY prefecture
HAVING COUNT(DISTINCT id) >= 5;
