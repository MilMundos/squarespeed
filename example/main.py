import csv

ls = 'lightspeed-inventory-export.csv'
ss = 'squarespace-inventory-export.csv'

ls_set = set()
ss_set = set()

with open(ls) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        ls_set.add(row['UPC'] + row['Custom SKU'])

with open(ss) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        ss_set.add(row['SKU'])

result = ls_set - ss_set

header = ["System ID","UPC","EAN","Custom SKU","Manufact. SKU","Item","Qty.","Price","Tax","Brand","Publish to eCom","Season","Department","MSRP","Tax Class","Default Cost","Vendor","Category","Subcategory 1","Subcategory 2","Subcategory 3","Subcategory 4","Subcategory 5","Subcategory 6","Subcategory 7","Subcategory 8","Subcategory 9"]

with open('missing-lightspeed-items.csv', 'a') as output:
    output.write(','.join(header) + "\n")
    with open (ls) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            element = row['UPC'] + row['Custom SKU']
            if element in result:
                fields = []
                for item in header:
                    fields.append(row[item])
                output.write(','.join(fields) + "\n")
