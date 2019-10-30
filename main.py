#!/usr/bin/python
# -*- coding: utf-8 -*-
from ui import *
from funcs import *
from api import *
import json
p1 = Player('031702621', '031702621')
p1.login()
json = p1.get_history(0, 20, p1.user_id)
while True:
    card = p1.getCard()
    print(card)
    ans = findAns(card)
    print(ans)
    p1.game_submit(ans)





