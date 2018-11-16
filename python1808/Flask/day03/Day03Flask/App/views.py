from random import *

from flask import Blueprint, render_template, request
from .models import *

blue = Blueprint('blue',__name__)
def init_blue(app):
    app.register_blueprint(blue)


@blue.route('/')
def init_page():
    return render_template('book_index.html')

@blue.route('/addauthor/')
def add_author():
    author_list = ['陈青云', '曹文轩', '陈继明', '陈启文', '陈染', '陈世旭', '陈晓明', '池莉', '迟子建', '陈建功', '陈瑞统', '陈与义', '程乃珊', '晁错', '曹靖华', '陈阵', '陈师道',
     '陈衍', '查沧珊', '陈映真', '程小青', '从维熙', '陈敬容', '常新港', '崔皓景', '陈益', '陈桂棣', '陈村', '橙未央', '蔡秋桐', '陈亮', '陈端生', '蔡骏', '沧月',
     '蔡芹芹', '陈枰', '曹雪芹', '陈应松', '陈福民']

    for author_name in author_list:
        author = Author()
        author.name = author_name
        author.age = randint(15,70)
        author.sex = choice([0,1])
        author.email = 'www.baidu.com'
        db.session.add(author)

        db.session.commit()

    return '创建作者成功'


@blue.route('/addbooks/')
def add_books():

    books_list = ['自读课本', '中国少年报', '小学生必读文库', '（史记·汉书）故事选编', '儿童文学', '少年文艺', '叶圣陶作品选', '莎士比亚戏剧故事选', '科学小博士文库', '红岩', '冰心作品选', '珍爱生命远离毒品', '小学生自然观察日记', '上下五千年', '闪闪的红星', '十万个斗智故事', '绿野仙踪', '神秘岛', '昆虫记', '杨红樱校园小说', '格列佛游记', '世界著名发明家的故事', '荷马史诗故事', '金银岛', '千家诗', '百家姓', '寄小读者', '假如只有三天光明', '哈克贝星·费思历险记']
    for book_name in books_list:
        book = Book()
        book.title = book_name
        book.date = str(randint(1990,2018))+'-'+str(randint(1,12))+'-'+str(randint(1,12))
        book.author = randint(1,39)
        db.session.add(book)
        db.session.commit()
    return '添加书籍成功'


@blue.route('/addpublisher/')
def add_publisher():

    publisher_list = ['巴蜀书社', '白山出版社', '百花文艺出版社', '百花洲文艺出版社', '北方妇女儿童出版社', '北方文艺出版社', '北京北影录音录像公司', '北京伯通电子出版社', '北京财经电子音像出版社', '北京出版社', '北京大学出版社', '北京大学医学出版社', '北京大学音像出版社', '北京电视艺术中心出版社', '北京电子音像出版社', '北京电子音像出版中心', '北京东方影音公司']
    for publisher_name in publisher_list:
        publisher = Publisher()
        publisher.name = publisher_name
        publisher.address = '北京'
        publisher.city = '北京'
        publisher.province = '北京'
        publisher.country = '中国'
        publisher.website = 'http:www.baidu.com'
        db.session.add(publisher)
        db.session.commit()
    return '添加出版社成功'



@blue.route('/bkaddpub/')
def book_add_publisher():
    for i in range(1,29):
        book = Book.query.get(i)
        for j in range(randint(1,5)):
            publisher = Publisher.query.get(randint(1,17))
            book.publishers.append(publisher)
            db.session.commit()
    return '添加关系成功'


# 书籍列表
@blue.route('/booklist/')
def book_list():
    page = int(request.args.get('page'))
    page_num = 5
    book_list = Book.query.offset((page-1)*page_num).limit(page_num)
    return render_template('book_list.html',book_list=book_list)

# 书籍详情
@blue.route('/bookdetail/<int:id>/')
def book_detail(id):
    book = Book.query.get(id)
    author_id = book.author
    author = Author.query.get(author_id)
    print(book.publishers)
    publishers = book.publishers
    return render_template('book_detail.html',book=book,author = author,publishers = publishers,length=len(publishers))

@blue.route(('/authordetail/<int:id>/'))
def author_detail(id):
    author = Author.query.get(id)

    return render_template('author_detail.html',author=author)


@blue.route(('/publisherdetail/<int:id>/'))
def publisher_detail(id):
    publisher = Publisher.query.get(id)

    return render_template('publisher_detail.html', publisher=publisher)