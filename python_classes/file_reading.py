# Using the json file found at https://raw.githubusercontent.com/wedeploy-examples/supermarket-web-example/master/products.json
# Write python code that accepts json and processes it into a final csv file that is readable in excel.
import json
import csv
import pandas as pd
import openpyxl
with open('products.json') as Json_File:
    products = json.load(Json_File)
product_pocket = open('product_holder.csv', 'w')
pocket_writer = csv.writer(product_pocket)
count = 0
for product in products:
    if count == 0:
 
        header = product.keys()
        pocket_writer.writerow(header)
        count += 1
    pocket_writer.writerow(product.values())
product_pocket.close()
the_file = pd.read_csv('./product_holder.csv')
the_file.to_excel('new_file.xlsx', index = None, header=True)

