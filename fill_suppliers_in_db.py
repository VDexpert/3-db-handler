import json
import psycopg2

with psycopg2.connect(host='localhost', database='northwind', user='postgres', password='postgres') as conn:
    cur = conn.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS suppliers (supplier_id serial PRIMARY KEY, company_name varchar NOT NULL, 
    phone varchar NOT NULL, fax varchar, country varchar NOT NULL, region varchar, postcode varchar NOT NULL, 
    city varchar NOT NULL, address varchar NOT NULL, homepage varchar);
    
    ALTER TABLE products ADD COLUMN supplier_id smallint NOT NULL DEFAULT 1""")

    with open('suppliers.json', 'r', encoding='utf-8') as f:
        json_suppliers = json.load(f)
        supplier_id = 0

        for supplier in json_suppliers:
            supplier_id += 1
            fax = supplier['fax']
            homepage = supplier['homepage']
            address_split = supplier["address"].split(';')

            if not supplier['fax']:
                fax = 'null'

            if not supplier['homepage']:
                homepage = 'null'

            cur.execute("""INSERT INTO suppliers VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
                        (supplier_id, supplier["company_name"], supplier["phone"], fax, address_split[0],
                         address_split[1], address_split[2], address_split[3], address_split[4], homepage))

            for product in supplier['products']:
                product = product.replace("'", '"')
                cur.execute(f"""UPDATE products SET supplier_id = {supplier_id} WHERE product_name = '{product}'""")


        cur.execute("""ALTER TABLE products ADD CONSTRAINT fk_products_supplier_id 
        FOREIGN KEY (supplier_id) REFERENCES suppliers(supplier_id)""")

    cur.close()

print('successful completion of the table')


