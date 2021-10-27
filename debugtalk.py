import hashlib
import time

import requests


def sleep(n_secs):
    time.sleep(n_secs)


# 定义实现md5复杂逻辑的函数
# 新知识点，如何在yaml中运用debugtalk.py当中函数所返回的值 $ {函数（）}
def sign():
    # {"phoneNum": "123434", "optCode": "testfan", "timestamp": "12112121212", "sign": "your sign data"}
    optCode = 'testfan'
    phoneNum = '11111'
    a = str(int(time.time()*1000))
    sign = phoneNum + optCode + a  # 字符串拼接
    # 对字符串进行md5加密
    md5_sign = hashlib.md5(sign.encode()).hexdigest()
    return {"phoneNum": phoneNum, "optCode": optCode, "timestamp": a, "sign": md5_sign}


def get_token():
    """
    获取token的值
    :return:
    """
    # 对登录接口进行访问，然后获取响应里面的data的值
    url = "http://localhost:8080/pinter/bank/api/login2"
    data = {'username': 'yaoyao', 'password': 'yaoyao'}
    res = requests.post(url, data=data)
    try:
        token = res.json().get('data')
    except:
        token = ''
    return token


def get_params():
    """
    获取列表嵌套列表数据
    :return:
    """
    return [
        ['正常登录', 'admin', 1234, 'success'],
        ['密码为空', 'admin', '', '参数为空'],
        ['用户名为空', '', 1234, '参数为空'],
        ['用户名和密码为空', '', '', '参数为空']
    ]


def str_to_int(args):
    """
    b接口依赖a接口响应中的字段data
    :param args: 从响应中提取的数据
    :return: int()转换成整数的数据
    """
    return int()


def hook_up():
    print('执行setup_hooks')


def hook_down():
    print('执行teardown_hooks')


def hook_log(info):
    print('info')


if __name__ == '__main__':
    print(get_token())
