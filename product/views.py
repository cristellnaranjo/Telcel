from itertools import product
from django.shortcuts import render
from django.http import HttpResponse, response
# import requests
import xmlrpc.client
import json
import base64
import sys
import json 
import os
import pandas as pd
import csv


 
from .connectionOdoo import * 
 
from dotenv import load_dotenv
load_dotenv()
# from dotenv import load_dotenv
 
# Create your views here.
def viewproducts(request):
    #return HttpResponse(socket.gethostbyname(socket.gethostname()))
    
    odoo = connectionOdoo()
    products =  odoo.models.execute_kw(
    odoo.db
    ,odoo.uid,
    odoo.password,
    'product.template','search_read',
    [
        [
            [ "company_id" ,"=", 4]
            # [ "id" ,"=", 2]
        ]
    ],
    {'fields': []}
)
 
    data = {
        "products":products
    }
    
        
    # return HttpResponse(products)
    return render(request ,"flights.html",data)
 
def viewproduct(request, id):
    odoo = connectionOdoo()
    products =  odoo.models.execute_kw(
    odoo.db
    ,odoo.uid,
    odoo.password,
    'product.template','search_read',
    [
        [
            [ "id" ,"=", id]
        ]
    ],
    {'fields': []}
)
 
    data = products
    
        
    # return HttpResponse(data['products'])
    return render(request ,"get.html", data)

def createProduct(request):
    url = os.getenv("URL_ODOO")
    db =  os.getenv("DB_ODOO")
    password =  os.getenv("PASSWORD_ODOO")
 
    models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
    common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
    output = common.version()
    uid = common.authenticate(db, os.getenv("USERNAME_ODOO"), password, output)
 
    id = models.execute_kw(db, uid, password, 'product.template', 'create', [{
    'name': "Producto DJANGO companyID",
    'default_code':"test_default_code_DJANGO",
    'list_price':"100",
    "company_id":1
    }])
    return HttpResponse(id)
 
def deleteProduct(request, id):
    url = os.getenv("URL_ODOO")
    db =  os.getenv("DB_ODOO")
    password =  os.getenv("PASSWORD_ODOO")
    models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
    common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
    output =  common.version()
    uid = common.authenticate(db, os.getenv("USERNAME_ODOO"), password, output)
    models.execute_kw(db, uid, password, 'product.template', 'unlink', [[id]])
    return HttpResponse("deleted")
 
def updateProduct(request):
    odoo = connectionOdoo()
    odoo.models.execute_kw(odoo.db, odoo.uid, odoo.password, 'product.template', 'write', [[43], {
    'name': "Newer partner",
    "price":"4567"
        }])
    return HttpResponse("updated")
    
def createCsvProducts(name, description, description_purchase, description_sale, type, barcode, defaultCode, categ_id, listPrice, volume, weight, companyId, sale_ok, purchase_ok, active, imagen):
    self = connectionOdoo()
    id = self.models.execute_kw(self.db, self.uid, self.password, 'product.template', 'create',
                                [
                                    {
                                        'name': name,
                                        'description': description,
                                        'description_purchase': description_purchase,
                                        'description_sale': description_sale,
                                        'type':type,
                                        'barcode': barcode,
                                        'categ_id': categ_id,
                                        'volume': volume,
                                        'weight': weight,
                                        'sale_ok':sale_ok,
                                        'purchase_ok':purchase_ok,
                                        'active': active,
                                        'description_picking':imagen,
                                        'default_code': defaultCode,
                                        'list_price': listPrice,
                                        'company_id': companyId
                                    }
                                ])
    

def AddProductsCSV(request):
    csv_file = os.path.join(os.path.dirname(__file__), 'productos.csv')
    df = pd.read_csv(csv_file)

    print(df.to_numpy()[0])
    for i in range(len(df.to_numpy())):
        createCsvProducts(df.to_numpy()[i][0], df.to_numpy()[i][1], df.to_numpy()[i][2], df.to_numpy()[i][3], df.to_numpy()[i][4], df.to_numpy()[i][5], df.to_numpy()[i][6], df.to_numpy()[i][7], df.to_numpy()[i][8], df.to_numpy()[i][9], df.to_numpy()[i][10], df.to_numpy()[i][11], df.to_numpy()[i][12], df.to_numpy()[i][13], df.to_numpy()[i][14], df.to_numpy()[i][15])
    return HttpResponse("CVS agregado")

    return HttpResponse("No hay archivo")


# check if the deleted record is still in the database
    # models.execute_kw(db, uid, password,
    #     'res.partner', 'search', [[['id', '=', id]]])
   