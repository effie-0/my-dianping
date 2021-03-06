from django.shortcuts import render, get_object_or_404
from .models import Business, Review, Profile
from django.contrib.auth.decorators import login_required
from .forms import ReviewForm
from django.contrib import messages
from gensim import corpora, models, similarities
import jieba

def search(request):
    request_type = request.POST.get("search_method")
    content = request.POST.get("request_content")
    if request.method == 'POST':
        if request_type == '1':
            business_list = Business.objects.filter(name__contains = content).order_by('-avg_rating')
        elif request_type == '2':
            business_list = Business.objects.filter(popular_dishes__contains = content).order_by('-avg_rating')
        else:
            business_list = Business.objects.filter(address__contains = content).order_by('-avg_rating')

    return render(request, 'display.html', {'businesses':business_list, })



def review_search(request):
    dictionary = corpora.Dictionary.load('review.dictionary')
    #corpus = corpora.MmCorpus('review.mm')
    lsi = models.LsiModel.load('review.lsi')
    print(lsi.num_topics)
    index = similarities.Similarity.load('review.index')

    query_txt = request.POST.get('review')
    query_string = ",".join(jieba.cut_for_search(query_txt))
    query_words = query_string.split(",")
    print(query_words)
    query = dictionary.doc2bow(query_words)
    print(query)
    query_lsi = lsi[query]
    print(query_lsi)

    sims = index[query_lsi]
    result_list = sorted(enumerate(sims), key=lambda item: -item[1])
    result_list = result_list[0:20]
    print(result_list)
    review_list = []
    for result in result_list:
        try:
            result_review = Review.objects.get(file_num=int(result[0]))
        except:
            continue

        review_list.append(result_review)

    return render(request, 'display_review.html', {'reviews':review_list, })

def review_search_key_word(request):
    content = request.POST.get('keyword')
    review_list = Review.objects.filter(content__contains = content)

    return render(request, 'display_review.html', {'reviews':review_list, })

def search_region(shop_list, region, dish_style):
    dic = { '朝阳区':['建外大街', '大望路', '朝外大街', '朝阳公园/团结湖', '左家庄',
                         '亮马桥/三元桥', '亚运村', '望京', '劲松/潘家园', '安贞', '芍药居',
                         '国贸', '双井', '三里屯', '对外经贸', '酒仙桥', '管庄', '首都机场',
                         '十八里店', '北苑家园', '十里堡', '东坝', '孙河', '马泉营', '定福庄',
                         '四惠', '太阳宫', '青年路', '石佛营', '甜水园', '慈云寺','八里庄', '工人体育场',
                         '百子湾', '传媒大学','二外', '双桥', '北京欢乐谷', '高碑店', '北京东站',
                         '霄云路', '蓝色港湾', '燕莎','农业展览馆', '姚家园', '十里河', '立水桥',
                         '小营', '北沙滩', '大屯', '小庄/红庙', '常营', '798/大山子', '草房',
                         '游娱联盟壹号基地'], 
            '东城区':['王府井/东单', '建国门/北京站', '东四', '安定门', '朝阳门', '东直门', '广渠门',
                         '左安门', '沙子口', '前门', '崇文门', '天坛', '地安门', '和平里', '东四十条', '雍和宫/地坛',
                         '南锣鼓巷/鼓楼东大街', '北新桥/簋街', '光明楼/龙潭湖', '沙滩/美术馆灯市口'], 
            '西城区':['西单', '复兴门', '阜成门', '西直门/动物园', '新街口', '地安门', '前门', '牛街', '虎坊桥',
                         '菜市口', '广内大街', '广外大街', '宣武门', '右安门', '西四', '月坛', '什刹海', '德外大街',
                         '陶然亭', '南菜园','白纸坊'],
            '海淀区':['中关村', '五道口', '魏公村', '北太平庄', '苏州桥', '北下关', '公主坟/万寿路', '紫竹桥',
                         '航天桥', '上地', '颐和园', '田村', '双榆树', '五棵松', '清河', '远大路', '香山', '大钟寺',
                         '知春路', '西三旗', '四季青', '人民大学', '万柳', '学院桥', '军博', '农业大学西区'], 
            '丰台区':['方庄', '六里桥/丽泽桥', '洋桥/木樨园', '宋家庄', '右安门', '北大地', '刘家窑', '青塔',
                         '开阳里', '草桥', '看丹桥', '花乡', '大红门', '公益西桥', '云岗', '卢沟桥', '北京西站/六里桥',
                         '分钟寺','成寿寺', '夏家胡同/纪家庙', '马家堡','角门', '马家堡','角门', '总部基地', '石榴庄',
                         '槐房万达广场'], 
            '石景山区':['苹果园', '古城','八角', '鲁谷', '模式口'],
            '大兴区':['亦庄', '旧宫', '黄村', '西红门'],
            '通州区':['宋庄', '西集', '物资学院', '果园', '梨园', '新华大街', '九棵树', '通州北苑', '武夷花园', '马驹桥',
                        '次渠'], 
            '昌平区':['回龙观', '天通苑', '昌平镇', '小汤山', '南口镇', '北七家', '沙河'], 
            '房山区':['长阳镇', '城关镇', '窦店镇', '阎村镇', '燕山', '河北镇', '十渡镇', '青龙湖镇', '良乡'], 
            '顺义区':['后沙峪', '马坡牛栏山', '南彩', '石园', '首都机场', '国展', '顺义'], 
            '怀柔区':['商业街', '京北大世界', '斜街', '下园', '东关', '富乐大街', '庙城', '桥梓镇', '雁栖开发区',
                         '渤海镇/慕田峪长城'], 
            '延庆区':['八达岭镇', '大榆树镇', '大庄科乡', '井庄镇', '旧县镇', '康庄镇', '刘斌堡乡', '千家店镇', '沈家营镇',
                         '四海镇', '香营乡', '延庆镇', '永宁镇', '张山营镇', '珍珠泉乡'], 
            '密云区':['北庄镇', '不老屯镇', '大城子镇', '东邵渠镇', '冯家峪镇', '高岭镇', '古北口镇', '河南寨镇',
                         '巨各庄镇', '经济开发区', '密云镇', '穆家峪镇', '十里堡镇', '石城镇', '太师屯镇', '西田各庄镇',
                         '溪翁庄镇', '新城子镇']
        }
    enum_list = dic[region]
    #result = Business.objects.none()
    result = []
    for subregion in enum_list:
        temp_list = Business.objects.filter(region__contains = subregion).order_by('-avg_rating')
        if dish_style != '全部':
            temp_list = temp_list.filter(category__contains = dish_style).order_by('-avg_rating')
        for b in temp_list:
            result.append(b)

    return result


def multi_search(request):
    dish_style = request.POST.get("dish_style")
    region = request.POST.get("region")
    subregion = request.POST.get("subregion")
    shop_list = Business.objects.all()

    if dish_style == None:
        dish_style = '全部'
    if region == None:
        region = '全市'
    if subregion == None:
        subregion = '全区'

    if dish_style != '全部':
        shop_list = shop_list.filter(category__contains = dish_style).order_by('-avg_rating')
    if region != '全市':
        if subregion != '全区':
            shop_list = shop_list.filter(region__contains = subregion).order_by('-avg_rating')
        else:
            shop_list = search_region(shop_list, region, dish_style)

    return render(request, 'display.html', {'businesses':shop_list})

def accurate(request, id):
    my_id = str(id)
    business = None
    try:
        business = Business.objects.get(shop_id = my_id)
    except:
        messages.info(request, "店铺未找到")
    reviews = Review.objects.filter(business__shop_id = my_id).order_by('-created_at')
    print(len(reviews))
    starred = 0

    if request.user.is_authenticated():
        profile = Profile.objects.get(user = request.user)
        try:
            profile.starred_list.get(shop_id = my_id)
            starred = 1
        except:
            starred = 0

    return render(request, 'show.html',{'business': business, 'reviews' : reviews, 'starred': starred})

def business_review(my_business):
    reviews = Review.objects.filter(business = my_business)
    return reviews

def recommend(request):
    dish_style = request.POST.get('mydish')
    region = request.POST.get('myregion')
    shop_list = Business.objects.all()

    if dish_style != None:
        shop_list = shop_list.filter(category__contains = dish_style).order_by('-avg_rating')
    if region != None:
        shop_list = shop_list.filter(region__contains = region).order_by('-avg_rating')

    return render(request, 'display.html', {'businesses':shop_list})

def region_search(request, region):
    shop_list = Business.objects.filter(region__contains = region).order_by('-avg_rating')
    return render(request, 'display.html', {'businesses':shop_list})

def dish_search(request, dish):
    shop_list = Business.objects.filter(category__contains = dish).order_by('-avg_rating')
    return render(request, 'display.html', {'businesses':shop_list})

@login_required
def create(request, myshop_id):
    params = request.POST if request.method == 'POST' else None

    form = ReviewForm(params)
    if form.is_valid():
        review = form.save(commit = False)
        review.user = request.user
        review.author = request.user.username
        business = Business.objects.get(shop_id = myshop_id)
        review.business = business
        if len(review.content) >= 50:
            review.excerpt = review.content[:50]
        else:
            review.excerpt = review.content

        if review.grade < 0 or review.grade > 5:
            messages.info(request, '请输入0到5之间的分数')
        elif review.price < 0:
            messages.info(request, '请输入大于等于0的价格')
        else:
            review.save()
            messages.info(request, '评论《{}》创建成功'.format(review.excerpt))

        form = ReviewForm()

    return render(request, 'comment.html', {'form':form, 'shop_id':myshop_id})
