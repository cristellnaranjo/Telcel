from itertools import product
from django.shortcuts import render, redirect, HttpResponse
from django.http import HttpResponse, response
from django.http import JsonResponse


# import requests
import xmlrpc.client
import base64
import sys
import json 
import os
import pandas as pd
import csv


 
from .connectionOdoo import * 
 
from dotenv import load_dotenv
load_dotenv()

def viewproducts(request):
    odoo = connectionOdoo()
    products =  odoo.models.execute_kw(
    odoo.db
    ,odoo.uid,
    odoo.password,
    'product.template','search_read',
    [
        [
            [ "company_id" ,"=", 4]
        ]
    ],
    {'fields': []}
) 
 
    data = {
        "products":products
    }
    
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
 
    data = {
        "products":products
    }
    return render(request ,"get.html", data)

def createProduct(request):

    return render(request, 'add.html')

def create(request):
    datos = request.POST
    odoo = connectionOdoo()
    odoo.models.execute_kw(odoo.db, odoo.uid, odoo.password, 'product.template', 'create', [
        {
            'name': datos['name'],
            'description': datos['description'],
            'barcode': datos['barcode'],
            'description_picking':datos['description_picking'],
            'default_code': datos['default_code'],
            'list_price': datos['list_price'],
            'company_id': 4
        }
    ])
    return redirect('/products')

def login(request):

    return render(request, 'login.html')

 
def deleteProduct(request, id):
    odoo = connectionOdoo()
    products =  odoo.models.execute_kw(
    odoo.db
    ,odoo.uid,
    odoo.password, 'product.template', 'unlink', [[id]])
    return redirect("/products")
    return HttpResponse("deleted")
 
def update(request,id):
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
 
    data = {
        "products":products
    }
    return render(request, 'update.html', data)
def updateProduct(request, id):
    datos = request.POST
    odoo = connectionOdoo()
    odoo.models.execute_kw(odoo.db, odoo.uid, odoo.password, 'product.template', 'write', [[id], 
        {
            'name': datos['name'],
            'description': datos['description'],
            'description_purchase': datos['description_purchase'],
            'description_sale': datos['description_sale'],
            'type':datos['type'],
            'barcode': datos['barcode'],
            # 'categ_id': datos['categ_id'],
            'volume': datos['volume'],
            'weight': datos['weight'],
            'description_picking':datos['imagen'],
            'default_code': datos['default_code'],
            'list_price': datos['list_price']
        }
    ])
    return redirect('/get/' + str(id))
    
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
