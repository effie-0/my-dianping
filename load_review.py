import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "my_dianping.settings")
django.setup()
from dianping.models import Review, Business
from django.utils import timezone

r_file = open('review.txt','r')
count = 0
for line in r_file:
	list = line.split('\t')
	if len(list) < 16 :
		continue

	print(count)
	count += 1

	shop_id_here = list[15]
	shop_list = Business.objects.filter(shop_id = shop_id_here)
	if len(shop_list) < 1:
		continue
		
	business = shop_list[0]
	author = list[1]

	#if len(list[12]) > 0:
	#	month, date = list[12].split('-')
	#	created_at = datetime.date(2017, int(month), int(date))
	#else:
	#	created_at = timezone.now

	content = list[14]
	if len(list[14]) > 50:
		excerpt = list[14]
	else:
		excerpt = list[14][0:47] + '...'

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