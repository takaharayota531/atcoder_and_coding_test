import sys
import json
import urllib.request


args=sys.argv
recipe_id=int(args[1])
# url = "https://static.cookpad.com/hr/screen/recipe_ingredients.json"
url=args[2]

with urllib.request.urlopen(url) as response:
    data = json.loads(response.read().decode())

data=data['data']


ingredient_dict={}
for i in range(len(data)):
  if data[i]['id']==recipe_id and data[i]['type']=='recipe':
    target=data[i]
  if  data[i]['type']=='ingredient':
    ingredient_dict[data[i]['id']]=data[i]['price']

target_ingredients = target['ingredients']

ans = 0
for ingredent in target_ingredients:
    ingredent_id = ingredent['ingredient_id']
    quantity = ingredent['quantity']
    ans += ingredient_dict[ingredent_id] * quantity

print(ans)