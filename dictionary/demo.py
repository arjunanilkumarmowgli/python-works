#employee id=100 name vipin department=hr  salary=25000

#create a dictionary product with keys id,title,price,brand


product={"id":100 ,"title":"moblie","price":310000,"brand":"iphone"}
print(product["title"])
print(product["brand"])
product["price"]=4000000#is method is to update
product["use_by_this_date"]="12/3/2025"#is method is add
product["offer"]=5#add method
print(product)
if "offer" in product:
  product["offer"]=10
else:
    product["offer"]=20
print(product)