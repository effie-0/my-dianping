r_file = open('popular_dishes.txt','r')
w_file = open('recommend_dish.txt','w')

line_count = 0
shop_id = ''
dish_list = []

for line in r_file:
	dish,id = line.split('\t')
	dish = dish[1:]
	length = len(id)
	id = id[0:length - 1]

	if len(dish) < 1:
		print('skip')
		continue
		
	if dish[0] == '(':
		continue
	if line_count == 0:
		shop_id = id
		dish_list.append(dish)
	else:
		if shop_id == id:
			dish_list.append(dish)
		else:
			string = shop_id + '\t' + ','.join(dish_list)
			#w_file.seek(0,2)
			w_file.write(string)
			shop_id = id
			dish_list = []
			dish_list.append(dish)
			w_file.write('\n')
	line_count += 1
	print(line_count)