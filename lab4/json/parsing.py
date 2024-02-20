import json

with open('sample_data.json', 'r') as file:
    data = json.load(file)

print('Interface Status')
print('================================================='
      '===========================')
print('DN                                             '
      'Description      Speed  MTU ')
print('------------------------------------------ '
      '------------------- ------- ----')
for item in data['imdata']:
    if item['l1PhysIf']['attributes']['dn'][-3] == '/':
        print(f"{item['l1PhysIf']['attributes']['dn']}                     "
              f" {item['l1PhysIf']['attributes']['speed']}"
              f" {item['l1PhysIf']['attributes']['mtu']}")
    else:
        print(f"{item['l1PhysIf']['attributes']['dn']}                    "
              f" {item['l1PhysIf']['attributes']['speed']}"
              f" {item['l1PhysIf']['attributes']['mtu']}")