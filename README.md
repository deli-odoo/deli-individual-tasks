# DELI - Kinsman Enterprises : Hiding the cart and prices on website
[Link](https://www.odoo.com/web#id=3364473&menu_id=4720&cids=3&action=4665&active_id=3364436&model=project.task&view_type=form) to task

## Steps to complete the dev
- [X] Create a new database
- [X] Create initial files and folders
- [X] Play around with the ecommerce module to figure out what it does
- [X] Create a checkbox in settings to disable/enable price and cart
    - [X] Inherit res.config.settings and create a bool field 
    - [X] Inherit the view as well and display the book field with a checkbox
    - [ ] Since res.config.model is a transient model, create getter and setter methods to store/read the bool field from ir.config_parameter

## Issues/Blocking Points
- Not an issue but I had to do some research on res.config.settings and how the data is actually stored

## Topics I need clarification on
      
## Interns who helped me

## Interns I helped