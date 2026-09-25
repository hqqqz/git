import re
class Customer:
    def __init__(self,c_id,name,age='None',phone='None',email='None'):
       #属性初始化
        self.c_id=c_id
        self.name=name
        self.age=age
        self.phone=phone
        self.email=email
    def __str__(self):
        #格式化输出
        return f"ID:{self.c_id:<15},Name:{self.name:<15},Age:{self.age:<15},Phone:{self.phone:<15}，Email:{self.email:<15}"

    #定义一个静态方法，对客户id进行校验
    @staticmethod
    def check_id(id):
        return id.isdigit()
    #对客户name进行验证
    @staticmethod
    def check_name(name):
        return name.isalnum()
    #对客户年龄进行验证
    @staticmethod
    def check_age(age):
        return age.isdigit() and 0<int(age)<120

    @staticmethod
    def check_phone(phone):
        return phone.isdigit() and len(phone)==11

    @staticmethod
    def check_email(email):
        pattern = r'^[a-zA-Z0-9_\-.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return bool(re.match(pattern, email))