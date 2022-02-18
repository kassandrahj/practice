# Using the json file found at https://raw.githubusercontent.com/wedeploy-examples/supermarket-web-example/master/products.json
# Write python code that accepts json and processes it into a final csv file that is readable in excel.
import json
import csv
#import pandas as pd
with open('products.json') as Json_File:
    products = json.load(Json_File)
product_content = products['product_details']
product_pocket = open('product_holder.csv', 'w')
pocket_writer = csv.writer(product_pocket)
count = 0
for product in products:
    if count == 0:
 
        header = product.keys()
        pocket_writer.writerow(header)
        count += 1
pocket_writer.writerow(product.values())
 
products.close()
# the_file = pd.read_csv (r'Path where the CSV file is stored\product_holder.csv')
# the_file.to_excel (r'Path to store the Excel file\File name.xlsx', index = None, header=True)

