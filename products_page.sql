--- Найти активные (см. поле discontinued) продукты из категории Beverages и Seafood,
--- которых в продаже менее 20 единиц. Вывести наименование продуктов, кол-во единиц
--- в продаже, имя контакта поставщика и его телефонный номер.
SELECT product_name, units_in_stock, company_name AS supplier_name, phone AS supplier_phone
FROM products JOIN categories USING (category_id) JOIN suppliers USING (supplier_id)
WHERE units_in_stock >= 20 AND category_name IN ('Beverages', 'Seafood');