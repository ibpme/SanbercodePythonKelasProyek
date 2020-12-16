import sqlite3

connection = sqlite3.connect('chinook.db')

find_invoices = '''
SELECT InvoiceDate,Total
FROM invoices 
WHERE InvoiceDate 
BETWEEN '2009-02-01 00:00:00' AND '2009-06-31 00:00:00';
'''


cursor = connection.cursor()
cursor.execute(find_invoices)

invoices = cursor.fetchall()

print(invoices)


connection.commit()


cursor.close()
connection.close()