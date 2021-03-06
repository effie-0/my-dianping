from django.shortcuts import render, redirect
from django.contrib import auth
from .models import Profile, Review, Business
from .myrequest import accurate
from django.contrib.auth.models import User
import django.contrib.auth.models
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    regions = ['朝阳区', '东城区', '西城区', '海淀区', '丰台区', '石景山区', '大兴区',
               '通州区', '昌平区', '房山区', '顺义区', '怀柔区', '延庆区', '密云区', '全市']
    subregions = {}
    subregions['朝阳区'] = ['建外大街', '大望路', '朝外大街', '朝阳公园/团结湖', '左家庄',
                         '亮马桥/三元桥', '亚运村', '望京', '劲松/潘家园', '安贞', '芍药居',
                         '国贸', '双井', '三里屯', '对外经贸', '酒仙桥', '管庄', '首都机场',
                         '十八里店', '北苑家园', '十里堡', '东坝', '孙河', '马泉营', '定福庄',
                         '四惠', '太阳宫', '青年路', '石佛营', '甜水园', '慈云寺/八里庄', '工人体育场',
                         '百子湾', '传媒大学/二外', '双桥', '北京欢乐谷', '高碑店', '北京东站',
                         '霄云路', '蓝色港湾', '燕莎/农业展览馆', '姚家园', '十里河', '立水桥',
                         '小营', '北沙滩', '大屯', '小庄/红庙', '常营', '798/大山子', '草房',
                         '游娱联盟壹号基地', '全区']

    subregions['东城区'] = ['王府井/东单', '建国门/北京站', '东四', '安定门', '朝阳门', '东直门', '广渠门',
                         '左安门', '沙子口', '前门', '崇文门', '天坛', '地安门', '和平里', '东四十条', '雍和宫/地坛',
                         '南锣鼓巷/鼓楼东大街', '北新桥/簋街', '光明楼/龙潭湖', '沙滩/美术馆灯市口', '全区']

    subregions['西城区'] = ['西单', '复兴门', '阜成门', '西直门/动物园', '新街口', '地安门', '前门', '牛街', '虎坊桥',
                         '菜市口', '广内大街', '广外大街', '宣武门', '右安门', '西四', '月坛', '什刹海', '德外大街',
                         '陶然亭', '南菜园/白纸坊', '全区']

    subregions['海淀区'] = ['中关村', '五道口', '魏公村', '北太平庄', '苏州桥', '北下关', '公主坟/万寿路', '紫竹桥',
                         '航天桥', '上地', '颐和园', '田村', '双榆树', '五棵松', '清河', '远大路', '香山', '大钟寺',
                         '知春路', '西三旗', '四季青', '人民大学', '万柳', '学院桥', '军博', '农业大学西区', '全区']

    subregions['丰台区'] = ['方庄', '六里桥/丽泽桥', '洋桥/木樨园', '宋家庄', '右安门', '北大地', '刘家窑', '青塔',
                         '开阳里', '草桥', '看丹桥', '花乡', '大红门', '公益西桥', '云岗', '卢沟桥', '北京西站/六里桥',
                         '分钟寺/成寿寺', '夏家胡同/纪家庙', '马家堡/角门', '马家堡/角门', '总部基地', '石榴庄',
                         '槐房万达广场', '全区']

    subregions['石景山区'] = ['苹果园', '古城/八角', '鲁谷', '模式口', '全区']

    subregions['大兴区'] = ['亦庄', '旧宫', '黄村', '西红门', '全区']

    subregions['通州区'] = ['宋庄', '西集', '物资学院', '果园', '梨园', '新华大街', '九棵树', '通州北苑', '武夷花园', '马驹桥',
                        '次渠', '全区']

    subregions['昌平区'] = ['回龙观', '天通苑', '昌平镇', '小汤山', '南口镇', '北七家', '沙河', '全区']

    subregions['房山区'] = ['长阳镇', '城关镇', '窦店镇', '阎村镇', '燕山', '河北镇', '十渡镇', '青龙湖镇', '良乡', '全区']

    subregions['顺义区'] = ['后沙峪', '马坡牛栏山', '南彩', '石园', '首都机场', '国展', '顺义', '全区']

    subregions['怀柔区'] = ['商业街', '京北大世界', '斜街', '下园', '东关', '富乐大街', '庙城', '桥梓镇', '雁栖开发区',
                         '渤海镇/慕田峪长城', '全区']

    subregions['延庆区'] = ['八达岭镇', '大榆树镇', '大庄科乡', '井庄镇', '旧县镇', '康庄镇', '刘斌堡乡', '千家店镇', '沈家营镇',
                         '四海镇', '香营乡', '延庆镇', '永宁镇', '张山营镇', '珍珠泉乡', '全区']

    subregions['密云区'] = ['北庄镇', '不老屯镇', '大城子镇', '东邵渠镇', '冯家峪镇', '高岭镇', '古北口镇', '河南寨镇',
                         '巨各庄镇', '经济开发区', '密云镇', '穆家峪镇', '十里堡镇', '石城镇', '太师屯镇', '西田各庄镇',
                         '溪翁庄镇', '新城子镇', '全区']

    subregions['全市'] = []

    dish_styles = ['私房菜', '北京菜', '家常菜', '台湾菜', '鲁菜', '川菜', '俄罗斯菜', '湘菜', '湖北菜', '徽菜', '小龙虾',
                   '江浙菜', '粉面馆', '粤菜', '创意菜', '东北菜', '清真菜', '咖啡厅', '新疆菜', '烧烤', '西北菜', '云南菜',
                   '贵州菜', '素菜', '火锅', '海鲜', '小吃快餐', '日本菜', '韩国料理', '东南亚菜', '西餐', '自助餐', '面包甜点',
                   '全部']


    return render(request, 'index0.html', {'regions':regions, 'subregions':subregions, 'dish_styles':dish_styles})

def login(request):
    return render(request, 'login.html')

def authenticate(request):
    username = request.POST.get('username')
    password = request.POST.get('password')

    user = auth.authenticate(request, username=username, password=password)

    if not user:
        if len(django.contrib.auth.models.User.objects.filter(username=username)) == 0:
            messages.info(request, '用户{}未注册'.format(username))
        else:
            messages.info(request, '密码错误')
        return redirect('login')

    auth.login(request, user)
    return redirect('index')

def signup(request):
    return render(request, 'signup.html')

def signup_submit(request):
    username = request.POST.get('username')
    telephone = request.POST.get('telephone')
    password = request.POST.get('password')
    if len(django.contrib.auth.models.User.objects.filter(username=username)) != 0:
        messages.info(request, '用户{}已注册'.format(username))
    if len(Profile.objects.filter(telephone = telephone)) != 0:
        messages.info(request, '手机号{}已注册'.format(telephone))

    try:
        print("trying")
        user = django.contrib.auth.models.User.objects.create_user(username = username, password = password)
        Profile.objects.get(user = user).telephone = telephone
        print("what's wrong?")
        return redirect('login')
    except:
        print("except orzzz")
        return redirect('signup')


@login_required
def logout(request):
    auth.logout(request)
    return redirect('login')

@login_required
def home(request):
    reviews = Review.objects.filter(user = request.user)
    profile = Profile.objects.get(user = request.user)
    telephone = profile.telephone
    businesses = profile.starred_list.all()
    return render(request, 'home.html', {'reviews': reviews, 'user': request.user, 'tel': telephone,
                                         'businesses': businesses })

@login_required
def delete(request, review_id):
    Review.objects.get(id = review_id).delete()
    return home(request)

@login_required
def change(request, user_id):
    user = User.objects.get(id = user_id)
    tel = Profile.objects.get(user = user).telephone
    return render(request, 'changeinfo.html', {'user': user, 'tel': tel})

@login_required
def changesubmit(request):
    user_id = request.POST.get('userid')
    user = User.objects.get(id = user_id)
    profile = Profile.objects.get(user = user)
    username = request.POST.get('username')
    telephone = request.POST.get('telephone')
    if username != user.username:
        if len(django.contrib.auth.models.User.objects.filter(username=username)) != 0:
            messages.info(request, '用户{}已注册'.format(username))
        else:
            user.username = username
            user.save()

    if telephone != profile.telephone:
        if len(Profile.objects.filter(telephone=telephone)) != 0:
            messages.info(request, '手机号{}已注册'.format(telephone))
        else:
            profile.telephone = telephone
            profile.save()

    return home(request)

@login_required
def changestar(request, shop_id):
    profile = Profile.objects.get(user = request.user)
    business = Business.objects.get(shop_id = shop_id)

    try:
        profile.starred_list.get(shop_id = shop_id)
        profile.starred_list.remove(business)
    except:
        profile.starred_list.add(business)

    return accurate(request, shop_id)
