#DAY-9
travel_log=[
{
 'country':'france',
 'cities':['paris','lille'],
  'visits':10
},

{
 'country':'germany',
 'cities':['berlin','dijion'],
 'visits':12
},
]

def add_new_country(country,city,visit):
    new_dict={}
    new_dict['country']=country
    new_dict['cities']=city
    new_dict['visits']=visit
    travel_log.append(new_dict)
    print(travel_log)
    
add_new_country(country="russia",city=['moscow','saint'],visit=12)
