from flask import Flask, render_template, request, redirect, url_for
from user import User
from product import Product

# 웹 서버 생성
APP = Flask(__name__)

product_images = ['books', 'kitchen', 'pig', 'vegetables', 'watch']

# 템플릿을 렌더할 때 공통적으로 거치는 인터페이스 
template = {
    'user': None,                   # 현재 로그인된 유저
    'user_list': User.user_list,    # 가입된 전체 유저 리스트
    'product_list': [],             # 페이지네이션 번호를 통해 물품을 보여줄 리스트(10개 제한)
    'current_page': 0,              # 페이지네이션 번호
    'user_id_list': {},
    'all_Products': Product.product_list, # 등록된 전체 물품 리스트
}

#초기화 -> 매번 회원가입하기 매우 귀찮기 때문에 미리 초기화 해두기!
User.add_user('nojy99', '1234')
User.add_user('junsu', '1111')
User.add_user('leejunsoo','1111');

Product.add_product('삼성 갤럭시 핸드폰','2년 정도 지났지만 여전히 쓸만한 최신 핸드폰', 100000,  '중고', 'junsu', 0)
Product.add_product('Mouse','old mouse, and expensive', 20000, '중고', 'nojy99', 0)
Product.add_product('Math book','5학년때 썼던 교과서', 15000, '쓸만한', 'junsu', 1)
Product.add_product('자아와 명상 book','000교수님 자아아 명상 교재', 6000, '필수교재', 'leejunsoo', 2)
Product.add_product('오마이걸 음원','리얼러브 앨범', 30000, '최신', 'nojy99', 3)
Product.add_product('컴퓨터 구조 족보','2009년부터 21년까지의 족보모음집', 40000, '필수', 'leejunsoo', 2)
Product.add_product('디지털 신호 처리 솔루션','퀴즈 및 과제 솔루션', 28000, '필수교재', 'junsu', 4)


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
            return redirect('/');
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
       ImageId=request.form['image']
       Desc=request.form['desc']
    else:
        return redirect('')
    Product.add_product(name,Desc, Price,keword, template['user'].name, ImageId)
    template['all_Products']=Product.product_list
    return redirect('/product')

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

#물품 정보
@APP.route('/product-info/<int:product_id>')
def product_info(product_id):
    img_url = url_for('static', filename='images/{}.jpg'.format(product_images[int(template['all_Products'][product_id].selected_id)]));
    return render_template('product_info.html', template=template, selected_product = product_id, img_url = img_url);

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
    
    def fsdfs():
        print("hello")