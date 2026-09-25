#用于匹配和操作文本的工具
#python中的re模块提供了正则表达式匹配操作
'''
    .任意字符
    \d数字  \w字母/数字/下划线 \s 空白
    +至少一次  *0次多次  ？ 0或1次非贪婪
    {n}恰好n次   {n，}最少n次  {n，m}n到m次
    【】任选一个；  【^】取反
    （）分组捕获；（？：）分组不捕获
    ^开头  $结尾
'''
        #import re
        #
        # re.search(pat,str)  找第一个匹配，返回Match对象，找不到None
        # re.findall(pat,str)  全部匹配，返回列表
        # re.sub(pat,new,str) 替换
        # re.split(pat,str) 按照匹配内容分割字符串