# DELI - Matrix Systems : Sequential Number for Barcode
[Link](https://www.odoo.com/web#id=3364442&menu_id=4720&cids=3&action=4665&active_id=3364436&model=project.task&view_type=form) to task

## Steps to complete the dev
- [X] Create a new database
- [X] Create initial files and folders
- [X] Inherit product.template and create 2 fields, barcode and product_group
- [X] Create a new model product_group
    - [X] Add security rights
    - [X] Create a field product_group of type int
- [X] In product template, make its product_group field a many2one relation with the model product_group
- [X] Make a compute method for barcode depending on product_template.product_group
- [X] Inherit the product template view and display product group and barcode

## Issues/Blocking Points
- I was unable to create error handling for the product group

## Topics I need clarification on
- I would like to practice more with relational fields to really get a feel for them
- Error handling
      
## Interns who helped me

## Interns I helped