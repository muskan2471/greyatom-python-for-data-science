# --------------
class_1=['Geoffrey Hinton','Andrew Ng','Sebastian Raschka','Yoshua Bengio']
class_2=['Hilary Mason','Carla Gentry','Corinna Cortes']
new_class=class_1+class_2
print(new_class)
new_class.append('Peter Warden')
print(new_class)
new_class.remove('Carla Gentry')
print(new_class)

courses={'Math':65,'English':70,'History':80,'French':70,'Science':60}
total=0
for each in courses.keys():
    total=total+courses.get(each)
print(total)
percentage=(total/500)*100
print(percentage)

mathematics={'Geoffrey Hinton':78,
'Andrew Ng':95,
'Sebastian Raschka':65,
'Yoshua Benjio':50,
'Hilary Mason':70,
'Corinna Cortes':66,
'Peter Warden':75}
topper  =max(mathematics,key=mathematics.get)
print(topper)

nameLs=topper.split(" ")
first_name=nameLs[0]
last_name=nameLs[1]
full_name =last_name+" "+first_name
certificate_name=full_name.upper()
print(certificate_name)





