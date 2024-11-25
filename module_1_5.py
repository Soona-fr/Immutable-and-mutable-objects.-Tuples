#неизменяемые и изменяемые объекты. кортежи

immutable_var = 2005, 1000, 7, 'breath', 555.72
print('immutable_var: ', immutable_var)
#immutable_var[3] = heartbeat #так как в данном случае использоуется кортеж, а не список, невозможно выполнить операцию заменыы элемента, так как кортеж не поддерживает работу с заменой отдельных элементов, это статичный "список"
#print(immutable_var)
#--------------------------------------
mutable_list = ([232, 125.5], 'heartbeat')
print('mutable_list_0: ', mutable_list)
mutable_list[0] [0] = 3
print('mutable_list_1: ', mutable_list)




