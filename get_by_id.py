import psycopg2

def get_product_by_id(config, id):
    result_json = []
    conn = psycopg2.connect(host=config[0], database=config[1], user=config[2], password=config[3])
    cur = conn.cursor()
    cur.execute(f"""SELECT product_id, product_name, category_name, unit_price 
    FROM products JOIN categories USING (category_id) WHERE product_id={id}""")
    header = [i[0] for i in cur.description]
    orig_data = cur.fetchall()

    for values in orig_data:
        result_json.append(dict(zip(header, values)))

    cur.close()
    conn.close()

    return result_json


def get_category_by_id(config, id):
    result_json = []
    conn = psycopg2.connect(host=config[0], database=config[1], user=config[2], password=config[3])
    cur = conn.cursor()
    cur.execute(f"""SELECT DISTINCT category_id, category_name, description 
    FROM categories JOIN products USING (category_id) WHERE category_id={id}""")
    header = [i[0] for i in cur.description]
    orig_data = cur.fetchall()

    for values in orig_data:
        result_json.append(dict(zip(header, values)))

    cur.execute(f"""SELECT product_name FROM products JOIN categories USING (category_id) WHERE category_id={id}""")
    values_products = cur.fetchall()
    products = []

    for value in values_products:
        products.append(*value)

    result_json[0]["products_names"] = products

    cur.close()
    conn.close()

    return result_json

if __name__ == "__main__":
    config = ['localhost', 'northwind', 'postgres', 'postgres']

    print(get_product_by_id(config, 4))
    print(get_category_by_id(config, 8))