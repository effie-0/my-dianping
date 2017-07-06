import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "my_dianping.settings")
django.setup()
from dianping.models import Business
from django.core.exceptions import ObjectDoesNotExist

r_file = open('location.txt')
count = 0
for line in r_file:
    list = line.split('\t')
    print(count)
    if len(list) < 5:
        continue

    shop_id = list[2]
    telephone = list[4]

    if len(list[0]) > 0:
        latitude = float(list[0])
    else:
        latitude = -1

    if len(list[1]) > 0:
        longitude = float(list[1])
    else:
        longitude = -1

    # print(shop_id)
    try:
        business = Business.objects.get(shop_id=shop_id)
    except ObjectDoesNotExist:
        continue

    business.latitude = latitude
    business.longitude = longitude
    business.telephone = telephone
    business.save()

    count += 1

r_file.close()
