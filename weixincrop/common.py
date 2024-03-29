#!coding=utf-8



WEIXIN_RESPONSE_CODE =  {'-1':'系统繁忙',
            '0':'请求成功',
            '40001':u'获取access_token时AppSecret错误，或者access_token无效',
            '40002':u'不合法的凭证类型',
            '40003':u'不合法的OpenID',
            '40004':u'不合法的媒体文件类型',
            '40005':u'不合法的文件类型',
            '40006':u'不合法的文件大小',
            '40007':u'不合法的媒体文件id',
            '40008':u'不合法的消息类型',
            '40009':u'不合法的图片文件大小',
            '40010':u'不合法的语音文件大小',
            '40011':u'不合法的视频文件大小',
            '40012':u'不合法的缩略图文件大小',
            '40013':u'不合法的APPID',
            '40014':u'不合法的access_token',
            '40015':u'不合法的菜单类型',
            '40016':u'不合法的按钮个数',
            '40017':u'不合法的按钮个数',
            '40018':u'不合法的按钮名字长度',
            '40019':u'不合法的按钮KEY长度',
            '40020':u'不合法的按钮URL长度',
            '40021':u'不合法的菜单版本号',
            '40022':u'不合法的子菜单级数',
            '40023':u'不合法的子菜单按钮个数',
            '40024':u'不合法的子菜单按钮类型',
            '40025':u'不合法的子菜单按钮名字长度',
            '40026':u'不合法的子菜单按钮KEY长度',
            '40027':u'不合法的子菜单按钮URL长度',
            '40028':u'不合法的自定义菜单使用用户',
            '40029':u'不合法的oauth_code',
            '40030':u'不合法的refresh_token',
            '40031':u'不合法的openid列表',
            '40032':u'不合法的openid列表长度',
            '40033':u'不合法的请求字符，不能包含uxxxx格式的字符',
            '40035':u'不合法的参数',
            '40038':u'不合法的请求格式',
            '40039':u'不合法的URL长度',
            '40050':u'不合法的分组id',
            '40051':u'分组名字不合法',
            '41001':u'缺少access_token参数',
            '41002':u'缺少appid参数',
            '41003':u'缺少refresh_token参数',
            '41004':u'缺少secret参数',
            '41005':u'缺少多媒体文件数据',
            '41006':u'缺少media_id参数',
            '41007':u'缺少子菜单数据',
            '41008':u'缺少oauth code',
            '41009':u'缺少openid',
            '42001':u'access_token超时',
            '42002':u'refresh_token超时',
            '42003':u'oauth_code超时',
            '43001':u'需要GET请求',
            '43002':u'需要POST请求',
            '43003':u'需要HTTPS请求',
            '43004':u'需要接收者关注',
            '43005':u'需要好友关系',
            '44001':u'多媒体文件为空',
            '44002':u'POST的数据包为空',
            '44003':u'图文消息内容为空',
            '44004':u'文本消息内容为空',
            '45001':u'多媒体文件大小超过限制',
            '45002':u'消息内容超过限制',
            '45003':u'标题字段超过限制',
            '45004':u'描述字段超过限制',
            '45005':u'链接字段超过限制',
            '45006':u'图片链接字段超过限制',
            '45007':u'语音播放时间超过限制',
            '45008':u'图文消息超过限制',
            '45009':u'接口调用超过限制',
            '45010':u'创建菜单个数超过限制',
            '45015':u'回复时间超过限制',
            '45016':u'系统分组，不允许修改',
            '45017':u'分组名字过长',
            '45018':u'分组数量超过上限',
            '46001':u'不存在媒体数据',
            '46002':u'不存在的菜单版本',
            '46003':u'不存在的菜单数据',
            '46004':u'不存在的用户',
            '47001':u'解析JSON/XML内容错误',
            '48001':u'api功能未授权',
            '50001':u'用户未授权该api'}

#微信接口url
USER_INFO_DETAIL = 'https://api.weixin.qq.com/cgi-bin/user/info' #用户信息详情


def getResponseInfomation(code):
    if code not in WEIXIN_RESPONSE_CODE:
        return None
    return WEIXIN_RESPONSE_CODE[code]