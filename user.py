from product import Product

class User:
    user_list = []
    user_ID_list={}
    def __init__(self, id, name, password):
        self.id = id
        self.name = name
        self.password = password
        self.isLogged = False;
        self.product_list = []
        self.followerlist=[]
    
    @classmethod
    def add_user(cls, name, password):
        for user in cls.user_list:
            if name == user.name and password == user.password:
                return False
        id = len(cls.user_list)
        cls.user_list.append(User(id ,name, password))
        cls.user_ID_list[name]=id;
        return True

    @classmethod
    def login(cls, name, password):
        for user in cls.user_list:
            if name == user.name and password == user.password:
                user.log_instance()
                return user
        return None
    
    @classmethod
    def logout(cls):
        for user in cls.user_list:
            user.logout_instance()
            
    def add_follower(self,otherID):
        self.followerlist.append(otherID)

    def log_instance(self):
        self.isLogged = True;
    
    def logout_instance(self):
        self.isLogged = False;
    
    def set_product(self, product_name, desc, price):
        product_id = Product.add_product(product_name, desc, price, self.id)
        self.product_list.append(product_id)
        
    def __repr__(self):
        return self.name