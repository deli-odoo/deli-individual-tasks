# DELI - Stansteel & Hotmix: Add total cost to SO line and SO
[Link](https://www.odoo.com/web#id=3364465&menu_id=4720&cids=3&action=4665&active_id=3364436&model=project.task&view_type=form) to task

## Steps to complete the dev
- [X] Create a new database
- [X] Create initial working module with init and manifest files
- [X] Create a model and views folder
- [X] Inherit the sale.order.line model
- [X] Add 2 new computed fields to sale order line: ext. cost and total cost (unless such a field already exists in source)
- [X] Create 2 functions with the depends decorator to compute these fields based on information in the SO
- [X] Inherit the sale.order view 
- [X] Display the newly created fields correctly in the form with xpath
- [ ] Profit?
- STEPS THAT I MISSED IN THE DESIGN BUT IMPLEMENTED:
- [X] Ext. cost goes in sale.order.line but total cost should have gone in sale.order (also inherit sale.order)
- [X] Minor detail: display cost with ext. cost to make debugging easier

## Issues/Blocking Points
- I had an issue with properly displaying the cost on the order line tree view. It turns out my xpath was not specific enough and it was finding the wrong field.
- Using sale.order view to display fields in sale.order.line

## Topics I need clarification on
- Defining cost/ext. cost in sale.order.line but displaying it using an inherited sale.order view NOT sale.order.line view was confusing. I figured out how it worked after trial and error and I think the behavior is like so because sale.order is related to sale.order.line in a one2many relationship but I will need more clarification on this. (Adam helped me with this and I understand it now)
      
## Interns who helped me
- PHSN - 5 - Helped make my xpath more specfic which allowed the fields to be properly displayed

## Interns I helped
