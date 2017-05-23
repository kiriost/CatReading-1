# -*- coding: utf-8 -*-
import top.api
import random

appkey = "23368540"
secret = "ada606d5b7d446e0d4173348e0af1044"

code = random.randint(1000, 9999)

req = top.api.AlibabaAliqinFcSmsNumSendRequest()
req.set_app_info(top.appinfo(appkey, secret))

# req.extend = "123456"
req.sms_type = "normal"
req.sms_free_sign_name = "袋鼠账号"
req.sms_param = "{\"code\":\"" + repr(code) + "\",\"product\":\"猫阅读\"}"
req.rec_num = "13260676152"
req.sms_template_code = "SMS_9680408"
try:
    resp = req.getResponse()
    print "ok"
    print(resp)
except Exception, e:
    print(e)