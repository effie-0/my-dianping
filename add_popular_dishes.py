from dianping.models import Business

r_file = open('recommend_dishes.txt','r')
for line in r_file:
	id, string = line.split('\t')
	shop_list = Business.objects.filter(shop_id = id)
	for shop in shop_list:
		shop.popular_dishes = string