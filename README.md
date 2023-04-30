# Peak Design Exam
Build a backend server that enables users to create a store and manage products
in the store. The API should allow users to create products associated with a specific store,
update the product’s inventory, and retrieve product information.

# Testing Tool
 - Postman

## Setup
1. Create virtual environment
 - `python -m venv {venv_name}`
    - make sure python and pip is installed

2. Install Dependencies
 - `pip install django`
 - `pip install djangorestframework`
 
3. Run server
 - `python manage.py runserver`


## Routes
1. Create Store:
  - [Post] `http://127.0.0.1:3000/app/store/`
  - Request Parameters: `name` `url`
  
2. Create Product:
  - [Post] `http://127.0.0.1:3000/app/products/`
  - Request Parameters: `store_id`, `name`, `sku`, `inventory_quantity`, `inventory_updated_time`
  
3. Get All Products related to Store
  - [Get] `http://127.0.0.1:3000/app/products/`
  - Request Parameters: `store_id`

4. Get Specific Product in Store
  - [Get] `http://127.0.0.1:3000/app/products/{int:product_id}/`
  - Request Parameters = `store_id`
  
5. Update Product
  - [Put]  `http://127.0.0.1:3000/app/products/{int:product_id}/inventory/`
  - Request Parameters = `store_id`, `inventory_quantity`

  
