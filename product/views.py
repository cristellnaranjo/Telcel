from email import message
from itertools import product
from django.shortcuts import render, redirect, HttpResponse
from django.http import HttpResponse, response
from django.http import JsonResponse
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required


# import requests
import xmlrpc.client
import base64
import sys
import json 
import os
from numpy import true_divide
import pandas as pd
import csv


 
from .connectionOdoo import * 
 
from dotenv import load_dotenv
load_dotenv()

@login_required
def viewproducts(request):
    odoo = connectionOdoo()
    try:
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
        return JsonResponse({"message": "Ok"})
    except:
        return JsonResponse({"message":"Error"})

    
@login_required
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

@login_required
def createProduct(request):

    return render(request, 'add.html')

@login_required
def create(request):
    datos = request.POST
    try:
        odoo = connectionOdoo()
        odoo.models.execute_kw(odoo.db, odoo.uid, odoo.password, 'product.template', 'create', [
            {
                'name': datos['name'],
                'description': datos['description'],
                'barcode': datos['barcode'],
                'default_code': datos['default_code'],
                'list_price': float(datos['list_price'])*1.16,
                'company_id': datos['companyId']
            }
        ])
        return JsonResponse({"message": "Se agrego"})
    except:
        return JsonResponse({"message": "Error"})

        return redirect('/products')

@login_required
def deleteProduct(request, id):
    try:
        odoo = connectionOdoo()
        products =  odoo.models.execute_kw(
        odoo.db
        ,odoo.uid,
        odoo.password, 'product.template', 'unlink', [[id]])
        return JsonResponse({"message":"Borrado", "ID":id})
        return redirect("/products")
    except:
        return JsonResponse({"message":"Error", "ID":id})
 
@login_required
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
    try:
        odoo = connectionOdoo()
        odoo.models.execute_kw(odoo.db, odoo.uid, odoo.password, 'product.template', 'write', [[id], 
            {
                'name': datos['name'],
                'description': datos['description'],
                'barcode': datos['barcode'],
                'default_code': datos['default_code'],
                'list_price': float(datos['list_price'])*1.16,
                'company_id': datos['companyId']
            }
        ])
        return JsonResponse({"message":"Ok"})
    except Exception as e:
        return JsonResponse({"message":e})
def createCsvProducts(name, description, description_purchase, description_sale, type, barcode, defaultCode, categ_id, listPrice, volume, weight, companyId, sale_ok, purchase_ok, active, imagen):
    self = connectionOdoo()
    try:
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
        return True
    except:
        return False
    
@login_required
def AddProductsCSV(request):

    try:
        odoo = connectionOdoo()
        csv_file = request.FILES["fileContent"]
        df = pd.read_csv(csv_file, sep=',', delimiter=None, header="infer", names=None, index_col=False)
    except:
        return JsonResponse({"message":"Error 1"})
    try:
        cont = 0
        for i in range(len(df.to_numpy())):
            resp = createCsvProducts(df.to_numpy()[i][0], df.to_numpy()[i][1], df.to_numpy()[i][2], df.to_numpy()[i][3], df.to_numpy()[i][4], df.to_numpy()[i][5], df.to_numpy()[i][6], df.to_numpy()[i][7], df.to_numpy()[i][8], df.to_numpy()[i][9], df.to_numpy()[i][10], df.to_numpy()[i][11], df.to_numpy()[i][12], df.to_numpy()[i][13], df.to_numpy()[i][14], df.to_numpy()[i][15])
            if resp:
                cont = cont + 1
    except:
        return JsonResponse({"message":"Error 2"})
        
    if cont == len(df.to_numpy()):
        return JsonResponse({"message": "Se agregaron todos los archivos"})
    else: 
        if cont == 0:
            return JsonResponse({"message": "No se agrego ningun archivo"})
        else:
            return JsonResponse({"message": str("Se agregaron " + cont + " archivos")})


def logoutview(request):
    logout(request)
    return redirect('/login')
def redirec(request):
    return redirect('/login')
