SELECT AVG(speed)
FROM PC;

SELECT product.maker, AVG(laptop.screen)
FROM laptop
JOIN product
on product.model = laptop.model
GROUP BY product.maker;

SELECT AVG(speed)
FROM laptop
WHERE price > 1000;

SELECT hd, AVG(price)
FROM pc
GROUP BY hd;

SELECT AVG(price)
FROM pc
GROUP BY price
HAVING speed > 500;

SELECT AVG(price)
FROM pc
JOIN product
ON product.model = pc.model
GROUP BY product.maker
HAVING product.maker = 'A';

SELECT product.maker, (AVG(pc.price) + AVG(laptop.price)) / 2
FROM product
LEFT JOIN pc
ON product.model = pc.model
LEFT JOIN laptop
ON product.model = laptop.model
GROUP BY product.maker
HAVING product.maker = 'B';

SELECT product.maker
FROM product
JOIN pc
ON pc.model = product.model
GROUP BY product.maker
HAVING COUNT(pc.model) >= 3;

SELECT product.maker, pc.price
FROM product
JOIN pc
ON pc.model = product.model
WHERE pc.price = (SELECT MAX(price) FROM pc)
GROUP BY product.maker;

SELECT product.maker, AVG(pc.hd)
FROM pc
LEFT JOIN product
ON product.model = pc.model
LEFT JOIN printer
ON printer.model = product.model
WHERE product.maker IN (SELECT product.maker
FROM printer
JOIN product
ON product.model = printer.model)
GROUP BY product.maker;

SELECT DISTINCT product.maker, AVG(pc.hd)
FROM pc
JOIN product
On product.model = pc.model
WHERE product.maker IN (SELECT product.maker
			FROM printer
			JOIN product
			ON product.model = printer.model)
GROUP BY product.maker;