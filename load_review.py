import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'my_dianping.settings'
import django
django.setup()
from dianping.models import Review, Business
from django.core.exceptions import ObjectDoesNotExist

r_file = open('review.txt','r')
count = 0
for line in r_file:
	list = line.split('\t')

	if len(list) < 16 :
		continue

	shop_id_here = list[15][:-1]
	try:
		business = Business.objects.get(shop_id = shop_id_here)
	except ObjectDoesNotExist:
		print('drop out!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
		print(shop_id_here.isdigit())
		print(list[15])
		continue

	print(count)
	count += 1

	author = list[1]

	content = list[14][1:]

	if len(content) < 50:
		excerpt = content
	else:
		excerpt = content[0:47] + '...'
	print(excerpt)
	#excerpt = ''

	if len(list[6]) > 0:
		grade = int(list[6][-2:])/10.0
	else:
		grade = -1
	if len(list[7]) > 0:
		avg_price = int(list[7][5:])
	else:
		avg_price = -1
	photo_url = list[9]
	if len(list[3]) > 0:
		author_id = list[3][8:]
	else:
		author_id = ''
	if len(list[13]) > 0:
		review_id = list[13][4:]
	else:
		review_id = ''
	
	Review.objects.create(business = business, author = author, author_id = author_id, price = avg_price, excerpt = excerpt, content = content,
						  grade = grade, review_id = review_id, photo_url = photo_url)
	
r_file.close()