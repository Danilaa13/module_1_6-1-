my_dict = {'Dima': 2001, 'Egor': 1999, 'Dasha': 2002}
print(my_dict)
print(my_dict['Dima'])
print(my_dict.get('Masha'))
my_dict.update({'Denis': 1998, 'Sasha': 1999})
a = my_dict.pop('Egor')
print(a)
print(my_dict)

my_set = {1,2,5,'Denis','Denis',1,4,5,3,2,'Denis',(1,2,3),True}
print(my_set)
my_set.add(8)
my_set.add('Masha')
my_set.discard(5)
print(my_set)