import itchat

# itchat.auto_login()
# itchat.send('Hello ,filehelper',toUserName='filehelper')

@itchat.msg_register(itchat.content.TEXT)
def TEXT_Reply(msg):
    return msg['Text']

itchat.auto_login()
itchat.run()