# DELI - Kinsman Enterprises : Hiding the cart and prices on website
[Link](https://www.odoo.com/web#id=3364473&menu_id=4720&cids=3&action=4665&active_id=3364436&model=project.task&view_type=form) to task

## Steps to complete the dev
- [X] Create a new database
- [X] Create initial files and folders
- [X] Play around with the ecommerce module to figure out what it does
- [X] Create a checkbox in settings to disable/enable price and cart
    - [X] Inherit res.config.settings and create a bool field 
    - [X] Inherit the view as well and display the book field with a checkbox
    - [X] Since res.config.model is a transient model, create getter and setter methods to store/read the bool field from ir.config_parameter
- [X] Inherit the view containing the cart button (edit: instead of inheriting a view, inherit the template)
- [ ] Inherit the template containing the price
- [ ] Inherit the template containing the quantity selector
- [X] Enable/disable templates based on the bool field with t-if and t-call (I actually implemented this without qweb but instead set the active tags of the templates)

## Issues/Blocking Points
- Not an issue but I had to do some research on res.config.settings and how the data is actually stored
- Issues with inheriting templates and general qweb quesitons
- Steps I was not able to get to:
    - Inheriting the templates for price and quantity selector and enabling/disabling it

## Topics I need clarification on
      
## Interns who helped me
- vajg - 2 - helped find which template to inherit from

## Interns I helped