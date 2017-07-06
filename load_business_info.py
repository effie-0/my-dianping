import os,django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "my_dianping.settings")
django.setup()

from dianping.models import Business
r_file = open('business_info.txt')
count = 0
for line in r_file:
	list = line.split('\t')
	print(count)
	if len(list) < 13:
		continue

	name = list[0]
	photo_url = list[1]
	shop_id = list[2][6:]
	recommend_text = list[12]

	if len(list[4]) > 0:
		if list[4][-2] == 'r':
			star = 0
		else:
			star = int(list[4][-2:])/10.0

	else:
		star = -1

	if len(list[5]) > 0:
		avg_price = int(list[5][1:])
	else:
		avg_price = -1

	category = list[6]
	region = list[7]
	address = list[8]

	if len(list[9]) > 0:
		product_grade = float(list[9])
	else:
		product_grade = -1

	if len(list[10]) > 0:
		decoration_grade = float(list[10])
	else:
		decoration_grade = -1

	if len(list[11]) > 0:
		service_grade = float(list[11])
	else:
		service_grade = -1

	sale_text = list[3]
	avg_rating = (product_grade + decoration_grade + service_grade)/ 3.0

	
	#print(shop_id)
	Business.objects.create(name = name, address = address, region = region, category = category, avg_rating = avg_rating,
							product_grade = product_grade, decoration_grade = decoration_grade, service_grade = service_grade,
							avg_price = avg_price, review_count = 0, sale_text = sale_text, recommend_text = recommend_text,
							photo_url = photo_url, star = star, shop_id = shop_id)

	count += 1

r_file.close()
