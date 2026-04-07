#On the following code we will see how we can be able to modify sets

set_countries = {"Col", "Arg", "Bra"}

#with the method 'len' we can know the size 
size = len(set_countries)
print("The size is the: ", size)

#If we want to know if there are any element inside the set we could use the next command
print('Col' in set_countries)
print('Pe' in set_countries)

#Now if we want to add an element we can use the following syntasis

set_countries.add("Pe")
print(set_countries)
print('Pe' in set_countries)

#And if we want to add more than one element we can use the sentence "Update" and "{}"
set_countries.update({"Ven", "Par", "Cu"})
print(set_countries)

#And to remove we could use the following syntasis
set_countries.remove('Ven')
print(set_countries)

#And at the end if we don't want to have any elemet present,
#we could use "discard" and if the element that we indicate 
#in discard doesn't exist nothing will happend

set_countries.discard('Pe')
set_countries.discard("USA")