import psycopg2


connection = psycopg2.connect(
    user='postgres',
    password='admin',
    host='127.0.0.1',
    port='5432',
    database='group1407'
)


select_all_from_addresses = connection.cursor()

select_all_from_addresses.execute("SELECT * FROM addresses")

print(select_all_from_addresses.fetchall())
print(select_all_from_addresses.fetchone())