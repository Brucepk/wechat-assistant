from wxpy import *

"""
本文首发自公众号：Python知识圈（id：PythonCircle）
作者：pk哥

「Python知识圈」公众号定时分享大量有趣有料的 Python 爬虫和实战项目，值得你的关注。
关注后回复1024免费领取学习资料！
"""

bot = Bot(cache_path=True)
# 定位亲人群
group_lists = ['小群', '小群2']
for group_list in group_lists:
    group_family = (bot.groups().search(group_list))

    @bot.register(group_family)
    def forward_message(msg):
        user = msg.sender
        if '生日' in msg.text:
            user.send('生日快乐！！！')

embed()
#
#
# # 回复随机祝福语
#
# from wxpy import *
# from random import choice
#
# bot = Bot(cache_path=True)
# # 定位亲人群
# group_lists = ['小群', '小群2']
# for group_list in group_lists:
#     group_family = (bot.groups().search(group_list))
#
#     @bot.register(group_family)
#     def forward_message(msg):
#         user = msg.sender
#         greeting_text = ['生日快乐！！！', '祝生日快乐，身体健康！', '祝生日快乐，每天开心！']
#         if '生日' in msg.text:
#             user.send(choice(greeting_text))
#
# embed()
#
#
# # 发送祝福图片
# from wxpy import *
# from random import choice
#
# bot = Bot(cache_path=True)
# # 定位亲人群
# group_lists = ['小群', '小群2']
# for group_list in group_lists:
#     group_family = (bot.groups().search(group_list))
#
#     @bot.register(group_family)
#     def forward_message(picture):
#         user = picture.sender
#         greeting_text = ['生日快乐！！！', '祝生日快乐，身体健康！', '祝生日快乐，每天开心！']
#         if '生日' in picture.text:
#             user.send(choice(greeting_text))
#             user.send_image('hd.jpg')
# embed()

# # 发送提醒消息给文件传输助手
# from wxpy import *
#
# bot = Bot(cache_path=True)
#
# # 定位亲人群
# group_family = (bot.groups().search('小群'))
# print(group_family)
#
#
# @bot.register(group_family)
# def forward_message(msg):
#     if '生日' in msg.text:
#         bot.file_helper.send(group_family)
#         bot.file_helper.send('群里出现生日关键字，请及时查看！')
#
#
# embed()


"""
本文首发自公众号：Python知识圈（id：PythonCircle）
作者：pk哥

「Python知识圈」公众号定时分享大量有趣有料的 Python 爬虫和实战项目，值得你的关注。
关注后回复1024免费领取学习资料！
"""

