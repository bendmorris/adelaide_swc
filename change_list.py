def change_list(a_list, to_change = 'I changed this!'):
    a_list[0] = to_change
 
a = [1,2,3,4]
change_list(a, 'something different')  
print a
