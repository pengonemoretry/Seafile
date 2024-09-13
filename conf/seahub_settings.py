# -*- coding: utf-8 -*-
SECRET_KEY = "b'1jwsxvb0ct&_1x6u&d+u8nf0m6ccwtv&n6w2%kr24^+u0gyip*'"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'seahub-db',
        'USER': 'seafile',
        'PASSWORD': 'tuyou@123',
        'HOST': '127.0.0.1',
        'PORT': '3306'
    }
}

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.mxhichina.com'        
EMAIL_HOST_USER = 'seafile@tuyoogame.com'    
EMAIL_HOST_PASSWORD = 'Tuyou@op123'    
EMAIL_PORT = '25'
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
SERVER_EMAIL = EMAIL_HOST_USER

#nginx域名配置
FILE_SERVER_ROOT = 'https://seafile.tuyoo.com/seafhttp'

#memcached配置
CACHES = {
            'default': {
                'BACKEND': 'django_pylibmc.memcached.PyLibMCCache',
                'LOCATION': '127.0.0.1:11211',
            },
            'locmem': {
                'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
            },
}
COMPRESS_CACHE_BACKEND = 'locmem'


# 设置钉钉扫描登录
ENABLE_DINGTALK = True
# 扫码登录相关
DINGTALK_QR_CONNECT_APP_ID = "dingoas2c3eljictequjas"
DINGTALK_QR_CONNECT_APP_SECRET = "iK7UDrtpQUEY6onJlIsXeHbe0PwUC2SoEwp68t-jQFnfPuEkqm1Dr0siMCx57FCO"
DINGTALK_QR_CONNECT_REDIRECT_URL = 'http{s}://seafile.tuyoo.com/accounts/login/' 

# 默认为True，新用户扫码登录后自动新建 seafile 用户。设置为False后，禁止新用户扫码注册，原有账号依旧可以扫码登录，并且管理员依旧可以通过导入钉钉用户的方式添加新用户。
DINGTALK_QR_CONNECT_CREATE_UNKNOWN_USER = True
# 默认为True，新用户扫码注册后，新建的 seafile 用户会自动激活。设置为False后，新用户扫码注册后需要管理员手动激活。
DINGTALK_QR_CONNECT_ACTIVATE_USER_AFTER_CREATION = True



# 导入钉钉用户相关
ENABLE_DINGTALK = True
DINGTALK_DEPARTMENT_APP_KEY = 'dingn7zwpq1daul2b7mo'
DINGTALK_DEPARTMENT_APP_SECRET = '5-MOnMkQXFCWeBUNtlj2LtzE002Rw1p94cV_KTk53XfwOHRmfmLOeBULJ8tmZJgE'


# 发送钉钉消息通知相关
ENABLE_DINGTALK = True
DINGTALK_AGENT_ID = '958313062'

