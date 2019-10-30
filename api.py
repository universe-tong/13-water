#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import json

def error_report(key):
    keys = {
        0: '成功',
        1001: '用户名已被使用',
        1002: '学号已绑定',
        1003: '教务处认证失败',
        1004: 'Token过期',
        2001: '未结束战局过多',
        2002: '出千！！！',
        2003: '不合法墩牌',
        3001: '战局不存在或未结束',
        3002: '玩家不存在'
    }
    if key in keys:
        print(keys[key])
    else:
        print('KeyError %d' % key)  # 出现未知错误码
class Player(object):
    def __init__(self, user, psw):
        self.user = user
        self.psw = psw
#        self.student_number = student_number
#       self.student_password = student_password
        self.user_id = None
        self.token = None
        self.is_register = None
        self.logged = None
        self.id = None
        self.cards = None
    def show(self):
        print()
        print(self.user)
        print(self.psw)
        print(self.user_id)
        print(self.token)
        print(self.is_register)
        print(self.logged)
        print(self.id)
        print(self.cards)
        print()
    def registerbang(self):
        def register_(user, psw, student_number, student_password):
            url = 'http://www.revth.com:12300/auth/register2'
            headers = {
                'Content-Type': 'application/json'
            }
            data = {
                'username': user,
                'password': psw,
                "student_number": student_number,
                "student_password": student_password
            }
            r = requests.post(url, headers=headers, data=json.dumps(data))
            return r
        r = register_(self.user, self.psw, self.student_number, self.student_password)
        status = r.json()['status']
        if status == 0 and 'user_id' in r.json()['data']:
            self.user_id = r.json()['data']['user_id']
            self.is_register = True
            print('register may be successful')
            print(r.text)
        else:
            print('register failed!')
            error_report(status)
            print(r.text)
    def login(self):
        def login_(user, psw):
            url = "http://api.revth.com/auth/login"
            headers = {
                'content-type': 'application/json'
            }
            data = {
                "username": user,
                "password": psw
            }
            r = requests.post(url, data=json.dumps(data), headers=headers)
            return r
        r = login_(self.user, self.psw)
        status = r.json()['status']
        if status == 0 and 'user_id' in r.json()['data']:
            self.user_id = r.json()['data']['user_id']
            self.token = r.json()['data']['token']
            self.logged = True
            print('Login may be successful')
            print(r.text)
        else:
            print('login failed!')
            error_report(status)
            print(r.text)
    def logout(self):
        def logout_(token):
            url = "http://api.revth.com/auth/logout"
            headers = {
                'x-auth-token': token
            }
            r = requests.post(url, headers=headers)
            return r
        r = logout_(self.token)
        status = r.json()['status']
        if status == 0:
            self.logged = False
            print('Logout may be successful')
            print(r.text)
        else:
            print('logout failed!')
            error_report(status)
            print(r.text)
# 登陆验证
    def validate_token(self):
        def validate_(token):
            url = 'http://api.revth.com/auth/validate'
            headers = {
                'X-Auth-Token': token
            }
            r = requests.get(url, headers=headers)
            return r
        r = validate_(self.token)
        status = r.json()['status']
        if status == 0 and 'user_id' in r.json()['data']:
            if 'token' in r.json()['data']:
                self.token = r.json()['data']['token']
            print('validate may be successful')
            print(r.text)
        else:
            print('validate failed!')
            error_report(status)
            print(r.text)
# 返回登陆状态
    def check_login_status(self):
        return self.logged
# 出牌
    def game_submit(self, submit_card):
        url = "http://api.revth.com/game/submit"
        data = {
            'id': self.id,
            'card': submit_card
        }
        headers = {
            'Content-Type': "application/json",
            'X-Auth-Token': self.token
        }
        r = requests.post(url, data=json.dumps(data), headers=headers)
        status = r.json()['status']
        if status == 0:
            print('submit successfully')
        else:
            print('game_submit failed!')
            print(r.text)
# 历史战绩
    def get_history(self, page, limit, play_id):
        def history(token, page, limit, play_id):
            url = "http://api.revth.com/history"
            querystring = {
                "page": page,
                "limit": limit,
                "player_id": play_id
            }
            headers = {
                'x-auth-token': token
            }
            r = requests.get(url, headers=headers, params=querystring)
            return r
        data = []
        r = history(self.token, page, limit, play_id)
        status = r.json()['status']
        if status == 0:
            data = r.json()['data']
        else:
            print('get_history failed!')
            error_report(status)
            print(r.text)
        print(data)
# 战局详情
    def get_history_detail(self, zjid):
        def history_detail(token, _id):
            url = "http://api.revth.com/history/" + str(_id)
            headers = {
                'x-auth-token': token
            }
            r = requests.get(url, headers=headers)
            return r
        r = history_detail(self.token, zjid)
        status = r.json()['status']
        if status == 0:
            print(r.json()['data'])
        else:
            print('get_history_detail failed!')
            error_report(status)
            print(r.text)
# 获取排行榜
    def get_rank(self):
        url = "http://api.revth.com/rank"
        r = requests.get(url)
        print(r.text)
# 获取手牌
    def getCard(self):
        url = 'http://api.revth.com/game/open'
        headers = {'X-Auth-Token': self.token}
        response = requests.post(url, headers=headers)
        response_dict = response.json()
        status = response_dict['status']
        if (status == 0):
            self.id = response_dict['data']['id']
            card = response_dict['data']['card'].split(' ')
            self.cards = card
        else:
            print('getCard Failed!')
            print(response.text)
        return card

