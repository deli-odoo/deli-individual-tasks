# DELI - Stansteel & Hotmix: Add total cost to SO line and SO
[Link](https://www.odoo.com/web#id=3364465&menu_id=4720&cids=3&action=4665&active_id=3364436&model=project.task&view_type=form) to task

## Steps to complete the dev
- [X] Create a new database
- [X] Create initial working module with init and manifest files
- [X] Create a model and views folder
- [X] Inherit the sale.order.line model
- [ ] Add 2 new computed fields to sale order line: ext. cost and total cost (unless such a field already exists in source)
- [ ] Create 2 functions with the depends decorator to compute these fields based on information in the SO
- [ ] Inherit the sale.order view 
- [ ] Display the newly created fields correctly in the form with xpath
- [ ] Profit

## Issues/Blocking Points

## Topics I need clarification on
      
## Interns who helped me
- PHSN - 5 - Helped make my xpath more specfic which allowed the fields to be properly displayed

## Interns I helped