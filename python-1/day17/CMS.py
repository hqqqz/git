from day17.customer import Customer


class CMS:
    def __init__(self):
        #初始化存储客户的字典
        #k：customer_id   v: customer对象
        self.customer_id_dict={}
        #k: customer_name   v: {k: customer_id  v:customer对象}
        self.customer_name_dict={}
    def start(self):
        #启动CMS系统
        while True:
            #显示系统菜单
            self.display_menu()
            #获取用户输入
            choise=input("请输入您要进行的操作（1-6）：")
            match choise:
                case '1':
                    self.add_customer()
                case '2':
                    self.delete_customer()
                case '3':
                    self.edit_customer()
                case '4':
                    self.search_customer()
                case '5':
                    self.all_customer()
                case '6':
                    print("您已经退出系统")
                    break
                case _:
                    print("您的输入不合理，需要在1-6之间，请重新输入")

    def display_menu(self):
        ###显示操作菜单###
        print("""
            =====================================欢迎来到CMS系统=====================================
                                            1.添加客户
                                            2.删除客户
                                            3.修改客户
                                            4.查询客户
                                            5.显示所有客户
                                            6.退出客户
            """)

    def add_customer(self):
        if not (customer_id:= self.set_customer_id()):
            return
        if not (customer_name:= self.set_customer_name()):
            return
        if not (customer_age:=self.set_customer_age()):
            return
        customer_phone=self.set_customer_phone()
        customer_email=self.set_customer_email()
        #封装客户对象
        customer_obj= Customer(customer_id, customer_name, customer_age, customer_phone, customer_email)
        #将封装好的对象导入字典   k:id  v:客户对象
        self.customer_id_dict[customer_id]=customer_obj
        #将封装好的对象导入字典2  k：name v:{k:id v：客户对象}
        customer_inner_name=self.customer_name_dict.get(customer_name)
        if customer_inner_name is None:
            self.customer_name_dict[customer_name]={customer_id:customer_obj}
        else:
            customer_inner_name[customer_id]=customer_obj
        print("#####添加客户成功######")
    def delete_customer(self):
        #删除客户 第一个字典
        customer_id=input("请输入id")
        if customer_id in self.customer_id_dict:
            #在id字典中查找id对应的数据
            customer=self.customer_id_dict[customer_id]
            #在对应数据中找到名字
            customer_name=customer.name
            #如果可以再id字典中查到id，删除这个字典
            del self.customer_id_dict[customer_id]
            #在name字典中找到对应的 v中有 k：id ，v：所有信息
            inner_dict=self.customer_name_dict.get(customer_name)
            #删除嵌套字典id对应的v
            del inner_dict[customer_id]
            #说明name字典中名字没有重复直接删除
            if len(inner_dict)==0:
                del self.customer_name_dict[customer_name]
            print('用户删除成功')
            return
        else:
            print("您输入的id不对，无法执行")

    def set_customer_id(self):
        #添加客户id
        id="None"
        for i in range(3):
            if i<2:
                id = input("请输入客户id：")
                #对id进行校验
                if Customer.check_id(id):
                    break
                else:
                    print("客户的id必须为纯数字")
            else:
                #i=2最后一次机会
                id = input("只剩最后一次机会了")
                # 对id进行校验
                if Customer.check_id(id):
                    break
                else:
                    print("机会用完")
                    return False
        if id in self.customer_id_dict:
            print("id已存在")
            return False
        return id

    def set_customer_name(self):
        #添加客户name
        name="None"
        for i in range(3):
            if i<2:
                name=input("请输入名字:")
                #对名字进行校验
                if Customer.check_name(name):
                    break
                else:
                    print("名字必须为字符")
            else:
                #i=2最后一次机会
                name=input('您还有最后一次机会')
                if Customer.check_name(name):
                    break
                else:
                    print('次数已用完')
                    return False
        return name

    def set_customer_age(self):
        age="None"
        for i in range(3):
            if i<2:
                age=input('请输入年龄')
                #判断年龄格式是否正确
                if Customer.check_age(age):
                    break
                else:
                    print('年龄错误必须为0-120内')
            else:
                #最后一次机会
                age=input('您还剩最后一次机会')
                #判断年龄是否正确
                if Customer.check_age(age):
                    break
                else:
                    print("机会用完，注册失败")
                    return False
        return age

    def set_customer_phone(self):
        phone="None"
        for i in range(3):
            if i<2:
                phone=input("请输入手机号")
                #判断格式是否正确
                if Customer.check_phone(phone):
                    break
                else:
                    print("输入手机号必须为十一位")
            else:
                phone=input('还有最后一次机会')
                if Customer.check_phone(phone):
                    break
                else:
                    print("机会用完,号码保存为默认值")
                    return "None"
        return phone

    def set_customer_email(self):
        email="None"
        email = input("请输入客户邮箱：")
        if Customer.check_email(email):
            return email
        else:
            print("格式不对，已使用默认值")
            return "None"

    def edit_customer(self):
        customer_id=input("请输入您的id")
        #判断id是否在字典中
        if customer_id in self.customer_id_dict:
            #如果在则提取字典
            edit=self.customer_id_dict[customer_id]
            #让用户选择修改什么内容
            print('1.修改年龄，2.修改手机号3.修改邮箱')
            choice=input("请您选择要修改的类型")
            if choice=='1':
                new_age=input("请输入新年龄")
                #验证年龄格式是否正确
                if Customer.check_age(new_age):
                    edit.age=new_age
                else:
                    print("您输入的年龄格式错误，修改失败")
            if choice=='2':
                new_phone=input("请输入新手机号")
                #验证手机号格式是否正确
                if Customer.check_phone(new_phone):
                    #修改手机号
                    edit.phone=new_phone
                else:
                    print("您输入的手机号格式错误，修改失败")
            if choice=='3':
                new_email=input('请输入新的邮箱')
                #判断邮箱格式是否正确
                if Customer.check_email(new_email):
                    edit.email=new_email
                else:
                    print("您输入的新邮箱格式错误，修改失败")
            if choice not in ['1','2','3']:
                print('输入的选项不对，请选择1/2/3')
        else:
            print("您输入的id错误,无法修改")
        return

    def search_customer(self):
        id=input("请输入要查询账户的id")
        #验证id是否在字典中
        if id in self.customer_id_dict:
            #如果在则分别遍历出v
            v = self.customer_id_dict[id]
            print(v)
        else:
            print('您输入的id错误,查询失败')
        return

    def all_customer(self):
        for v in self.customer_id_dict.values():
            print(v)


if __name__=="__main__":
    cms=CMS()
    cms.start()