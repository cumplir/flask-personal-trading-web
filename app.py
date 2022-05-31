from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
from user import User
from product import Product
import os
# 웹 서버 생성
APP = Flask(__name__)

product_images = ['kitchen', 'vegetables', 'books', 'watch', 'pig']

# 템플릿을 렌더할 때 공통적으로 거치는 인터페이스 
template = {
    'user': None,                   # 현재 로그인된 유저
    'user_list': User.user_list,    # 가입된 전체 유저 리스트
    'product_list': [],             # 페이지네이션 번호를 통해 물품을 보여줄 리스트(10개 제한)
    'current_page': 0,              # 페이지네이션 번호
    'user_id_list': {},
    'all_Products': Product.product_list, # 등록된 전체 물품 리스트
    'selected_follower':None
}

#초기화 -> 매번 회원가입하기 매우 귀찮기 때문에 미리 초기화 해두기!
User.add_user('nojy99', '1234')
User.add_user('junsu', '1111')
User.add_user('leejunsoo','1111');

Product.add_product('아이폰12pro','2년 정도 지났지만 여전히 쓸만한 최신 핸드폰', 300000,  '핸드폰', 'junsu', 0,"smartphone.png")
Product.add_product('Mouse','old mouse, and expensive', 20000, '마우스', 'nojy99', 0,"Mouse.png")
Product.add_product('Math book','5학년때 썼던 교과서', 15000, '교양책', 'junsu', 1,"MathBook.png")
Product.add_product('자아와 명상 book','000교수님 자아아 명상 교재', 6000, '교양책', 'leejunsoo', 2,"Meditation.png")
Product.add_product('오마이걸 음원','리얼러브 앨범', 30000, '최신', 'nojy99', 3,"OhmygirlAlbum.png")
Product.add_product('컴퓨터 구조 족보','2009년부터 21년까지의 족보모음집', 40000, '전공책', 'leejunsoo', 2,"CompuScience.png")
Product.add_product('디지털 신호 처리 솔루션','퀴즈 및 과제 솔루션', 28000, '전공책', 'junsu', 4,"Digital.png")
Product.add_product('스타벅스 아메리카노 기프티콘', '2023년 6월까지 쓸 수 있는 아이스 아메리카노 기프티콘', 4500, '기프티콘', 'junsu', 0,"Starbugs.png")
Product.add_product('베스킨라빈스 파인트 기프티콘', '8200->7000에 팝니다', 7000, '기프티콘', 'junsu', 3,"Bera31.png")
Product.add_product('GallexyS21+','미개봉상품', 200000, '핸드폰', 'nojy99', 0,"GallexyS21.png")
Product.add_product('나이키 에어맥스','사이즈가 안맞아서 팝니다.', 180000, '신발', 'nojy99', 0,"NikeShoes.png")
Product.add_product('스타벅스 기프티콘 팝니다','5000->4500에 팝니다', 4500, '기프티콘', 'junsu', 0,"Starbugs.png")


#메인화면
@APP.route("/")
def index():
    return render_template('home.html', template=template)

#로그인
@APP.route("/login", methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        name = request.form['ID']
        password = request.form['PW']
        template['user'] = User.login(name, password)
        template['user_id_list']=User.user_ID_list
        if template['user'] is None:
            #로그인 실패
            print('login is fail')
            return render_template('login.html', template=template)
        else:
            #로그인 성공
            print('logged')
            return redirect('/')
    #로그인 폼
    return render_template('login.html', template=template)

#회원가입
@APP.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == 'POST':
        name = request.form['ID']
        password = request.form['PW']

        if User.add_user(name, password) == False:
            #회원가입 실패
            print('sign up failed!')
            return redirect('')
        else:
            #회원가입 성공
            print(User.user_list)
            return render_template('home.html', template=template)
    else:
        #회원가입 폼
        return render_template('register.html', template=template)
    
#물품 업로드
@APP.route("/product-form", methods=["GET", "POST"])
def Upload():
    if request.method == 'POST':
        name=request.form['name']
        keword=request.form['keyword']
        Price=request.form['price']
        file=request.files['image']
        filename = secure_filename(file.filename)
        os.makedirs("./static/images", exist_ok=True)
        file.save(os.path.join("./static/images/", filename))
        Desc=request.form['desc']
    else:
        return redirect('/')
    id = Product.add_product(name, Desc, Price, keword, template['user'].name, template['user'].id, filename)
    template['all_Products']=Product.product_list
    return render_template('mypage.html', template=template)

#로그아웃
@APP.route('/logout')
def logout():
    User.logout()
    template['user'] = None
    return redirect('/')
    
#물품 조회
@APP.route('/product')
def product():
    start, end = template['current_page']*10, template['current_page']*10+10
    template['product_list'] = Product.product_list[start:end]
    return render_template('product.html', template=template)

@APP.route('/search')
def Search():
    keyword = request.args.get('keyword')
    template['product_list']=[]
    for i in template['all_Products']:
        if i.keyword==keyword:
            template['product_list'].append(i)
    return render_template('product.html', template=template)

@APP.route('/GotoFollower')
def GotoFollower():
    ID=request.args.get('ID')
    for user in User.user_list:
        if user.name == ID:
            template['selected_follower']=user
    return render_template('otherpage.html',template=template)
#물품 정보
@APP.route('/product-info/<int:product_id>')
def product_info(product_id):
    product = Product.search(product_id)
    img_url="../static/images/"+product.image_name
    return render_template('product_info.html', template=template, product=product,img_url=img_url);

@APP.route('/mypage')
def mypage():
    return render_template('mypage.html', template=template)

#물품 정보 업데이트
@APP.route('/product-update/<int:product_id>', methods=["GET","POST"])
def product_update(product_id):
    product = Product.search(product_id)
    print(product ,"update...")

    product.name=request.form['name']
    product.keyword=request.form['keyword']
    product.price=request.form['price']
    file=request.files['image']
    filename = secure_filename(file.filename)
    os.makedirs("./static/images", exist_ok=True)
    file.save(os.path.join("./static/images/", filename))
    product.image_name=filename
    product.desc=request.form['desc']

    template['all_Products'] = Product.product_list;
    print(product, '...updated')
    return redirect(f'/product-info/{product_id}')

@APP.route('/soldout', methods=["GET","POST"])
def soldout():
    num=int(request.args.get("soldout"))
    if template['all_Products'][num].soldout == 1:
        Product.product_list[num].soldout=0
        template['all_Products'][num].soldout = 0
    else:
        Product.product_list[num].soldout=1
        template['all_Products'][num].soldout = 1
    return redirect('/mypage')


#물품 정보 삭제
@APP.route('/product-delete/<int:product_id>')
def product_delete(product_id):
    Product.delete(product_id);

    template['all_Products'] = Product.product_list
    return redirect('/product');

#FOllOW
@APP.route('/Follow')
def follow():
    if template['user']!= None:
        ID=request.args.get('ID')
        if ID not in template['user'].followerlist:
            template['user'].AddFollow(ID)
        else:
            template['user'].DelFollow(ID)
        return redirect('/mypage')
    else:
        return redirect('/login')

    
#페이지네이션
@APP.route('/page_up')
def pageUp():
    if template['current_page'] < len(Product.product_list)/10 - 1:
        template['current_page'] += 1
    return redirect('/product')

@APP.route('/page_down')
def pageDown():
    if template['current_page']*10 > 1:
        template['current_page'] -= 1
    return redirect('/product')

#실행코드
if __name__ == "__main__":
    APP.run(debug=True)
