{'name': "Enterprise Pulse",
 'author': "Eng Ahmed Sameh, Eng Karim Shawky",
 'category': "",
 'version': "18.0.0.1.0",
 'depends': [
     'base', 'hr', 'contacts', 'account', 'stock','purchase', 'sale_management'
 ],
 'data': [
    'security/ir.model.access.csv',
    'views/res_company_view.xml',
    'views/res_partner_view.xml',
    'views/stock_location.xml',
    'views/stock_warehouse.xml',
    'views/product_category.xml',
    'views/product_template.xml',
    'views/sale_order.xml',
 ],
 'assets' : {
 }
 ,
 'license': 'LGPL-3',
 'application': True,
 }
