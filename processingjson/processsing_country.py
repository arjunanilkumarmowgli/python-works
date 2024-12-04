from json import load

f=open("C:\\pythonworks\\dataset\\countiresdetails.json",encoding="utf-8")

data=load(f)

# print number of countries

# print(len(data))

# print all country names

all_country_name=[country.get("name")for country in data]

# print(all_country_name)

# print all regions

all_regions=[country.get("region")for country in data ]

#print(set(all_regions))
region_count={region:all_regions.count(region) for region in all_regions}
#print(region_count)
#printing maximum region count
max_region_count=max(region_count,key=lambda k:region_count.get(k))
# print(max_region_count,region_count.get(max_region_count))

#capital of india   
country_capital=[country.get("capital") for country in data if country.get("name")=="India"]  
# print(country_capital)       


# country with most number of boader

country_borders={country.get("name"):len(country.get("borders",[]))for country in data}

# print(country_borders)

# max borders

max_border_country=max(data,key=lambda country:len(country.get("borders",[]))).get("name")
# print(max_border_country)

# most populate country

most_populated_country=max(data,key=lambda country:country.get("population",0)).get("name")
# print(most_populated_country)
aplfa_three_codes=[country.get("borders") for country in data if country.get("name")=="Afghanistan"][0]

for code in aplfa_three_codes:

    for country in data:

        if country.get("alpha3Code")==code:

            print(country.get("name"))








