-- Practical 7
-- Shrey Viradiya
-- 18BCE259

-- This Code is executed on https://livesql.oracle.com

-- Display the description and total quantity sold
-- for each product.

select description,nvl(sum(qtyordered), 0)"TOTAL_QTY" 
from product left outer join sales_order_details 
on product.productno=sales_order_details.productno 
group by description;

-- Calculate the average quantity sold for each 
-- client that has a maximum order value of 15000.00

select clientno,nvl(avg(qtyordered),0)"AVERAGE" 
from sales_order left outer join sales_order_details 
on sales_order.orderno=sales_order_details.orderno 
group by clientno having nvl(sum(qtyordered*productrate),0)<15000;

-- Find out the total of all the billed orders for the month of May.

select extract(month from orderdate)"MONTH", nvl(sum(qtyordered), 0)"MAY_ORDER" 
from sales_order left outer join sales_order_details
on (sales_order.orderno=sales_order_details.orderno)
where sales_order.billyn='N'  and extract(month from orderdate)=5
group by extract(month from orderdate);

-- Find the products and their quantities for the orders placed by ‘Ivan Bayross’ and ‘Mamta Shah’.

select name,description,qtyordered 
from client,product,sales_order,sales_order_details 
where name in('Ivan Bayross','Mamta Shah') 
and client.clientno = sales_order.clientno 
and sales_order.orderno = sales_order_details.orderno 
and sales_order_details.productno = product.productno;

-- List the products and orders from customers who have ordered less than 5 units of ‘1.44 Floppies’.

select description, orderno
from product left outer join sales_order_details 
on (product.productno=sales_order_details.productno)
where description like '1.44%' and qtyordered < 5;