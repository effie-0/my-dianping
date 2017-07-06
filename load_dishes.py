import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "my_dianping.settings")
django.setup()
from dianping.models import Business
from django.core.exceptions import ObjectDoesNotExist

r_file = open('recommend_dish.txt')
count = 0
for line in r_file:
    shop_id, dishes = line.split('\t')
    print(count)

    try:
        business = Business.objects.get(shop_id=shop_id)
    except ObjectDoesNotExist:
        print('drop out!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
        continue

    business.popular_dishes = dishes
    business.save()

    count += 1

r_file.close()
