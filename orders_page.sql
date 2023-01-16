--- Выбрать все заказы, отсортировать по required_date (по убыванию) и отсортировать по дате отгрузке (по возрастанию)
--- две сортировки сразу:
SELECT * FROM orders ORDER BY required_date DESC, shipped_date;
--- сортировка по требуемой дате (по убыванию)
SELECT * FROM orders ORDER BY required_date DESC;
--- сортировка по дате отгрузки (по возрастанию)
SELECT * FROM orders ORDER BY shipped_date;

--- Найти среднее значение дней, уходящих на доставку с даты формирования заказа в USA
SELECT AVG(shipped_date - order_date) AS average_period_shipping
FROM orders WHERE ship_country = 'USA';

--- Найти сумму, на которую имеется товаров (количество * цену) причём таких, которые не сняты с продажи
SELECT SUM(unit_price * units_in_stock) AS sum_of_products
FROM products WHERE discontinued = 0;