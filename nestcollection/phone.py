products=[
    {"id":1,"title":"s23ultra","brand":"samsung","price":78000},
    {"id":2,"title":"a17","brand":"samsung","price":18000},
    {"id":3,"title":"m50","brand":"samsung","price":16000},
    {"id":4,"title":"pocom3","brand":"poco","price":15000},
    {"id":7,"title":"vivov50","brand":"vivo","price":25000},
    {"id":5,"title":"oppof19pro","brand":"oppo","price":27000},
    {"id":6,"title":"iphone16pro","brand":"apple","price":150000},
    {"id":9,"title":"iphone16plus","brand":"apple","price":150000},
    {"id":8,"title":"nokia105","brand":"nokia","price":900}

]

# total number of mobiles
# print(len(products))

# print mobile titles
titles=[t.get("title") for t in products]
# print(titles)

# print samsung mobiles
titles1=[t.get("title") for t in products if t.get("brand")=="samsung"] #returns a list of all phones with "brand"=="samsung"
print(len(titles1))

# print(titles1)

#most expensive
most_exp=(max(products,key=lambda d:d.get("price"))) #get most expensive mobile dictionary
max_cost=most_exp.get("price")                       #get the "price"  value of the most expensive mobile
all_exp_mobs=[m.get("title") for m in products if m.get("price")==max_cost]  #get all mobile phones with the highest price value
print(all_exp_mobs) 

# print(min(products,key=lambda d:d.get("price")))

all_brand_names=[p.get("brand")for p in products]
count_of_brands={c:all_brand_names.count(c) for c in all_brand_names}
print(count_of_brands)