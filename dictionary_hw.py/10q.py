product={"diarymilk":100,
"munch":50,
"chocobar":25,
"snikers":40
}
over={items:price*0.9 for items,price in product.items()}
print("MRP=",product)
print("oƯer price=",over)