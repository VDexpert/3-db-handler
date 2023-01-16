--- Выбрать записи работников (включить колонки имени, фамилии, телефона, региона) в которых регион неизвестен
SELECT first_name, last_name, home_phone, city, country
FROM employees WHERE region IS NULL

--- Выбрать такие страны в которых "зарегистированы" одновременно заказчики и поставщики,
--- но при этом в них не "зарегистрированы" работники
--- 1 вариант:
SELECT DISTINCT country FROM customers
JOIN suppliers USING (country)
EXCEPT
SELECT DISTINCT country FROM employees;
--- 2 вариант:
SELECT DISTINCT c.country FROM customers AS c
WHERE EXISTS (SELECT 1 FROM suppliers AS s WHERE c.country=s.country)
EXCEPT
SELECT DISTINCT country FROM employees