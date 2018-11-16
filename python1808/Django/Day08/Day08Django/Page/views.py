from django.core.paginator import Paginator
from django.shortcuts import render
from .models import *
from random import *
# Create your views here.


def index(request,num):
    users = User.objects.all()
    p = Paginator(users,15)
#     names = '''李宇春 张靓颖 周笔畅 何洁 刘亦菲 张含韵 陈好 尚雯婕
# 汤唯 张筱雨 韩雪 孙菲菲 张嘉倪 霍思燕 陈紫函 朱雅琼
# 江一燕 厉娜 许飞 胡灵 郝菲尔 刘力扬 reborn 章子怡
# 谭维维 魏佳庆 张亚飞 李旭丹 孙艺心 巩贺 艾梦萌 闰妮
# 王蓉 汤加丽 汤芳 牛萌萌 范冰冰 赵薇 周迅 金莎
# 纪敏佳 黄雅莉 叶一茜 马苏 阿桑 董卿 金铭 徐行
# 姚笛 朱妍 夏颖 陈西贝 冯家妹 高娅媛 林爽 郑靖文
# 陶虹 徐静蕾 黄奕 董洁 巩俐 高圆圆 于娜 孟广美
# Gameapple 美女奉奉 小龙女彤彤 张子萱 果子 丁贝莉 吸血芭比 公交MM
# 香香 段思思 二月丫头 刘羽琦 dodolook 拉拉公主 沈丽君 周璟馨
# 丁叮 谢雅雯 陈嘉琪 宋琳 郭慧敏 卢洁云 佘曼妮 黄景
# 马艳丽 蒋雯丽 宁静 许晴 张静初 瞿颖 张延 孙俪
# 闵春晓 蔡飞雨 邓莎 白冰 程媛媛 吴婷 殷叶子 朱伟珊
# 孙菂 赵梦恬 龚洁 许晚秋 杨舒婷 乔维怡 王海珍 易慧
# 谢雨欣 陈娟红 舒畅 李小璐 曹颖 李冰冰 王艳 沈星
# 阿朵 周洁 杨林 李霞 陈自瑶 李小冉 李湘 金巧巧
# 蒋勤勤 梅婷 刘涛 秦海璐 安又琪 杨钰莹 马伊俐 陈红
# 鲍蕾 牛莉 胡可 杨幂 龚蓓苾 田震 杨童舒 吕燕
# 王姬 苗圃 李欣汝 王小丫 秦岚 徐帆 刘蓓 彭心怡
# 邓婕 眉佳 李媛媛 刘晓庆 杨若兮 黄圣依 林熙 薛佳凝
# 斯琴格日乐 宋祖英 郝蕾 乐珈彤 冯婧 宋丹丹 盖丽丽 田海蓉
# 杨澜 沈冰 王宇婕 王希维 姜培琳 何晴 焦媛 白灵
# 胡静 陈冲 刘怡君 韦唯 龚雪 周彦宏 刘丹 傅艺伟
# 谢东娜 朱媛媛 黑鸭子 周璇 吕丽萍 杨欣 陈小艺 伍宇娟
# 苏瑾 李玲玉 张凯丽 潘虹 沈丹萍 岳红 赵静怡 宋晓英'''
#     names = names.replace('\n',' ').split(' ')
#
#     print(names)
#     for name in names:
#         age = randint(20,60)
#         obj = User.objects.create(name=name,age=age)
    page = p.page(num)
    data = {
        "page":page,
        "page_range":p.page_range,
    }


    return render(request,'Page/index.html',data)