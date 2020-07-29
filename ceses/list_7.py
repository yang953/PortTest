import re

def choice_email():
    while 1:
        email = input(r"请输入邮箱地址:")
        if email=="Q" or email=="q":
            # break
            exit()
        elif re.match(r"^(\w+)*@(\w+)+(\.com)$",email):
            user_name = re.findall("(\w+)*@",email)[0]
            company_name = re.findall("@(\w+).com$",email)[0]
            print("邮件中用户名称是:{0}\n公司名称是:{1}".format(user_name,company_name))
        else:
            print("incorrect email format")



if __name__=="__main__":
    choice_email()

# import re
# pat = r'^(\w)+(\.\w+)*@(\w)+((\.\w+)+)$'
# email_address = 'ddy_davie@aaa.com'
# matched_address = re.match(pat, email_address)
# print(matched_address.group())

#
# while 1:
#     mail = input(r"请输入邮箱地址：")
#     if mail = "Q"