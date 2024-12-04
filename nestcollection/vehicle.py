cars=[
    {"id":1,"name":"fronx","price":1200000,"brand":"nexa",
     "colors":["red","blue","white"],
     "transmissions":["manuel","amt","cvt"]},
    {"id":2,"name":"baleno","price":1100000,"brand":"nexa",
     "colors":["grey","blue","white"],
     "transmissions":["manuel","amt","cvt"]},
    {"id":3,"name":"3xo","price":900000,"brand":"mahindra","colors":["red","white","black"],"transmissions":["amt","cvt"]},
    {"id":4,"name":"punch","price":700000,"brand":"tata","colors":["red","blue","white","green"],"transmissions":["manuel","cvt"]},
    {"id":5,"name":"nexon","price":1400000,"brand":"tata","colors":["red","white"],"transmissions":["manuel","amt","cvt"]},
    {"id":6,"name":"kiger","price":1000000,"brand":"renault","colors":["blue","white"],"transmissions":["manuel","cvt","dct"]},
    {"id":7,"name":"taigun","price":2300000,"brand":"volkswagon","colors":["red","blue","white"],"transmissions":["manuel","cvt","torque"]},
]
#printnumber of cars

print(f"total vehicle=>{len(cars)}")

#print available baleno

baleno_colors=[c.get("colors") for c in  cars if c.get("name")=="baleno"]
print(baleno_colors[0])

#print all brands

all_brands=[c.get("brand") for c in cars]
print(set(all_brands))
        
#print car name available in amt transmission 
amt_cars=[c.get("name") for c in cars if "amt" in c.get ("transmissions")]
print(amt_cars)


#cars avilable in blue color

blue_colors_cars=[ ]

#costly car

costly_cars=max(cars,key=lambda d:d.get("price"))
print(costly_cars.get("name"))

#low_cost car

low_cost=min(cars,key=lambda d:d.get("price"))

print(low_cost.get("name"))

#sort cars
sorted_car=sorted(cars,key=lambda d:d.get("price"),reverse=True)
sorted_car_name={c.get("name"):[c.get("brand"),c.get("price")] for c in sorted_car}
print(sorted_car_name)