from flask import Flask, render_template, request, redirect
from user import User
from product import Product

# 웹 서버 생성
APP = Flask(__name__)

# 템플릿을 렌더할 때 공통적으로 거치는 인터페이스 
template = {
    'user': None,                   # 현재 로그인된 유저
    'user_list': User.user_list,    # 가입된 전체 유저 리스트
    'product_list': [],             # 페이지네이션 번호를 통해 물품을 보여줄 리스트(10개 제한)
    'current_page': 0,              # 페이지네이션 번호
    'user_id_list': {},
    'all_Products': []
}

#초기화 -> 매번 회원가입하기 매우 귀찮기 때문에 미리 초기화 해두기!
User.add_user('nojy99', '1234')
User.add_user('junsu', '1111')
User.add_user('leejunsoo','1111');

Product.add_product('Mouse','old mouse, and expensive', 20000, 'nojy99')
Product.add_product('Math book','5학년때 썼던 교과서', 15000, 'junsu')
Product.add_product('자아와 명상 book','000교수님 자아아 명상 교재', 6000, 'leejunsoo')
Product.add_product('오마이걸 음원','리얼러브 앨범', 30000, 'nojy99')
Product.add_product('컴퓨터 구조 족보','2009년부터 21년까지의 족보모음집', 40000, 'leejunsoo')
Product.add_product('디지털 신호 처리 솔루션','퀴즈 및 과제 솔루션', 28000, 'junsu')
Product.add_product('오마이걸 음원','리얼러브 앨범', 30000, 'nojy99')
Product.add_product('컴퓨터 구조 족보','2009년부터 21년까지의 족보모음집', 40000, 'leejunsoo')
Product.add_product('디지털 신호 처리 솔루션','퀴즈 및 과제 솔루션', 28000, 'junsu')
Product.add_product('오마이걸 음원','리얼러브 앨범', 30000, 'nojy99')
Product.add_product('컴퓨터 구조 족보','2009년부터 21년까지의 족보모음집', 40000, 'leejunsoo')
Product.add_product('Mouse','old mouse, and expensive', 20000, 'nojy99')
Product.add_product('Math book','5학년때 썼던 교과서', 15000, 'junsu')
Product.add_product('자아와 명상 book','000교수님 자아아 명상 교재', 6000, 'leejunsoo')
Product.add_product('오마이걸 음원','리얼러브 앨범', 30000, 'nojy99')
Product.add_product('컴퓨터 구조 족보','2009년부터 21년까지의 족보모음집', 40000, 'leejunsoo')
Product.add_product('디지털 신호 처리 솔루션','퀴즈 및 과제 솔루션', 28000, 'junsu')
Product.add_product('오마이걸 음원','리얼러브 앨범', 30000, 'nojy99')
Product.add_product('컴퓨터 구조 족보','2009년부터 21년까지의 족보모음집', 40000, 'leejunsoo')
Product.add_product('디지털 신호 처리 솔루션','퀴즈 및 과제 솔루션', 28000, 'junsu')
Product.add_product('오마이걸 음원','리얼러브 앨범', 30000, 'nojy99')
Product.add_product('Mouse','old mouse, and expensive', 20000, 'nojy99')
Product.add_product('Math book','5학년때 썼던 교과서', 15000, 'junsu')
Product.add_product('자아와 명상 book','000교수님 자아아 명상 교재', 6000, 'leejunsoo')
Product.add_product('오마이걸 음원','리얼러브 앨범', 30000, 'nojy99')
Product.add_product('컴퓨터 구조 족보','2009년부터 21년까지의 족보모음집', 40000, 'leejunsoo')
Product.add_product('디지털 신호 처리 솔루션','퀴즈 및 과제 솔루션', 28000,'junsu')
Product.add_product('오마이걸 음원','리얼러브 앨범', 30000, 'nojy99')
Product.add_product('컴퓨터 구조 족보','2009년부터 21년까지의 족보모음집', 40000, 'leejunsoo')
Product.add_product('디지털 신호 처리 솔루션','퀴즈 및 과제 솔루션', 28000, 'junsu')
Product.add_product('오마이걸 음원','리얼러브 앨범', 30000, 'nojy99')
Product.add_product('컴퓨터 구조 족보','2009년부터 21년까지의 족보모음집', 40000, 'leejunsoo')
Product.add_product('Mouse','old mouse, and expensive', 20000, 'nojy99')
Product.add_product('Math book','5학년때 썼던 교과서', 15000, 'junsu')
Product.add_product('자아와 명상 book','000교수님 자아아 명상 교재', 6000, 'leejunsoo')
Product.add_product('오마이걸 음원','리얼러브 앨범', 30000, 'nojy99')
Product.add_product('컴퓨터 구조 족보','2009년부터 21년까지의 족보모음집', 40000, 'leejunsoo')
Product.add_product('디지털 신호 처리 솔루션','퀴즈 및 과제 솔루션', 28000, 'junsu')
Product.add_product('오마이걸 음원','리얼러브 앨범', 30000, 'nojy99')
Product.add_product('컴퓨터 구조 족보','2009년부터 21년까지의 족보모음집', 40000, 'leejunsoo')
Product.add_product('디지털 신호 처리 솔루션','퀴즈 및 과제 솔루션', 28000, 'junsu')
Product.add_product('오마이걸 음원','리얼러브 앨범', 30000, 'nojy99')


#메인화면
@APP.route("/")
def index():
    template['all_Products'] = Product.product_list[0:len(Product.product_list)]
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