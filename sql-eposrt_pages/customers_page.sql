--- Посчитать количество заказчиков
SELECT COUNT(*) FROM customers;

--- Выбрать все уникальные сочетания городов и стран, в которых "зарегестрированы" заказчики
SELECT DISTINCT city, country FROM customers ;

--- Найти заказчиков и обслуживающих их заказы сотрудников, таких, что и заказчики и сотрудники
--- из города London, а доставка идёт компанией Speedy Express. Вывести компанию заказчика и ФИО сотрудника.
SELECT customers.company_name AS customer,  CONCAT(first_name, ' ', last_name) AS full_name_employee FROM orders
JOIN employees USING (employee_id) JOIN customers USING (customer_id) JOIN shippers ON (ship_via = shipper_id)
WHERE customers.city = 'London' AND employees.city = 'London' AND shippers.company_name = 'Speedy Express';

--- Найти заказчиков, не сделавших ни одного заказа. Вывести имя заказчика.
SELECT customers.company_name FROM customers
EXCEPT
SELECT customers.company_name FROM orders
JOIN customers USING(customer_id);
