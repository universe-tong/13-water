import requests
import json
import http
import re

def findAns(card):
    global s, ths1, ths2, hua1, hua2, s,bmax,mid, hulu_num, hulu2_num, hulu, tonghua_da, da_hua, tonghua_xiao, xiao_hua, shunzi_da, shunzi_xiao,santiao_da, santiao_xiao,qdun, zdun, hdun
    global h1, h2, h3, h4, n1, n2, n3, n4, n5, n6, n7, n8, n9, n10, n11, n12, n13, ans
    s = card[0] + card[1] + card[2] + card[3] + card[4] + card[5] + card[6] + card[7] + card[8] + card[9] + card[10] + card[11] + card[12]
    s = s.replace("10", "T")
    s = s.replace(" ", "")
    qdun = ""
    zdun = ""
    hdun = ""
    def trans_num(i):
        if i == 'A':
            return 14
        if i == '2':
            return 2
        if i == '3':
            return 3
        if i == '4':
            return 4
        if i == '5':
            return 5
        if i == '6':
            return 6
        if i == '7':
            return 7
        if i == '8':
            return 8
        if i == '9':
            return 9
        if i == 'T':
            return 10
        if i == 'J':
            return 11
        if i == 'Q':
            return 12
        if i == 'K':
            return 13
    # 放墩里用
    def ntoc(i):
        if i == 14:
            return 'A'
        if i == 2:
            return '2'
        if i == 3:
            return '3'
        if i == 4:
            return '4'
        if i == 5:
            return '5'
        if i == 6:
            return '6'
        if i == 7:
            return '7'
        if i == 8:
            return '8'
        if i == 9:
            return '9'
        if i == 10:
            return '10'
        if i == 11:
            return 'J'
        if i == 12:
            return 'Q'
        if i == 13:
            return 'K'
    # 过程用
    def ntocT(i):
        if i == 14:
            return 'A'
        if i == 2:
            return '2'
        if i == 3:
            return '3'
        if i == 4:
            return '4'
        if i == 5:
            return '5'
        if i == 6:
            return '6'
        if i == 7:
            return '7'
        if i == 8:
            return '8'
        if i == 9:
            return '9'
        if i == 10:
            return 'T'
        if i == 11:
            return 'J'
        if i == 12:
            return 'Q'
        if i == 13:
            return 'K'
    def ntocTA(i):
        if i == 14:
            return 'A'
        if i == 2:
            return '2'
        if i == 3:
            return '3'
        if i == 4:
            return '4'
        if i == 5:
            return '5'
        if i == 6:
            return '6'
        if i == 7:
            return '7'
        if i == 8:
            return '8'
        if i == 9:
            return '9'
        if i == 10:
            return 'T'
        if i == 11:
            return 'J'
        if i == 12:
            return 'Q'
        if i == 13:
            return 'K'
    def nth(i):
        if i == 1:
            return '*'
        if i == 2:
            return '&'
        if i == 3:
            return '#'
        if i == 4:
            return '$'
    # 按花色分 * h1 & h2 # h3 $ h4
    h1 = []
    h2 = []
    h3 = []
    h4 = []
    n2 = []
    n3 = []
    n4 = []
    n5 = []
    n6 = []
    n7 = []
    n8 = []
    n9 = []
    n10 = []
    n11 = []
    n12 = []
    n13 = []
    n1 = []

    def cre_table():
        global s
        global h1,h2,h3,h4,n2,n3,n4,n5,n6,n7,n8,n9,n10,n11,n12,n13,n1
        h1.clear();h2.clear();h3.clear();h4.clear();n2.clear();n3.clear();n4.clear();n5.clear();n6.clear();n7.clear()
        n8.clear();n9.clear();n10.clear();n11.clear();n12.clear();n13.clear();n1.clear()
        # 按花色分 * h1 & h2 # h3 $ h4
        for i in list(range(len(s))):
            if s[i] == '*':
                n = trans_num(s[i + 1])
                h1.append(n)
            if s[i] == '&':
                n = trans_num(s[i + 1])
                h2.append(n)
            if s[i] == '#':
                n = trans_num(s[i + 1])
                h3.append(n)
            if s[i] == '$':
                n = trans_num(s[i + 1])
                h4.append(n)
        h1.sort();h2.sort();h3.sort();h4.sort()
        # 按数字分
        for i in list(range(len(s))):
            if s[i] == '2':
                n2.append(s[i - 1])
            if s[i] == '3':
                n3.append(s[i - 1])
            if s[i] == '4':
                n4.append(s[i - 1])
            if s[i] == '5':
                n5.append(s[i - 1])
            if s[i] == '6':
                n6.append(s[i - 1])
            if s[i] == '7':
                n7.append(s[i - 1])
            if s[i] == '8':
                n8.append(s[i - 1])
            if s[i] == '9':
                n9.append(s[i - 1])
            if s[i] == 'T':
                n10.append(s[i - 1])
            if s[i] == 'J':
                n11.append(s[i - 1])
            if s[i] == 'Q':
                n12.append(s[i - 1])
            if s[i] == 'K':
                n13.append(s[i - 1])
            if s[i] == 'A':
                n1.append(s[i - 1])

    # 同花顺
    ths1 = []
    ths2 = []
    hua1 = 0
    hua2 = 0
    # 炸弹
    bmax = 0
    mid = 0
    # 葫芦
    hulu = []
    hulu_num = []
    hulu2_num = []
    # 同花
    tonghua_da = 0
    da_hua = 0
    tonghua_xiao = 0
    xiao_hua = 0
    # 顺子
    shunzi_da = 0
    shunzi_xiao = 0
    # 三条
    santiao_da = 0
    santiao_xiao = 0
    # 散牌
    hdun = ""
    zdun = ""
    qdun = ""
    # 找同花顺
    def find_tonghuashun():
        # 返回值 0 没找到 1后墩有了 2后墩中墩都有了
        r = []
        global ths1,ths2,hua1,hua2
        get1 = 0  # 1只有后墩有同花，ths1被用

        # h1
        if len(h1) >= 5:  # 可能有同花顺
            for i in list(range(len(h1)-4)):
                if h1[i+4] == h1[i] + 4 and h1[i+3] == h1[i] + 3 and h1[i+2] == h1[i] + 2 and h1[i+1] == h1[i] + 1:
                    r.append(h1[i])  # 同花顺首

            if len(r) > 1:  # 有1个以上同花顺，可能重叠
                if r[len(r)-1] > r[0] + 4:  # 有两个不重叠同花顺
                    ths1 = list(range(r[0], r[0]+4+1, 1));hua1 = 1  # 小的给中墩
                    ths2 = list(range(r[len(r)-1], r[len(r)-1]+4+1, 1));hua2 = 1  # 大的给后墩
                    return 2
                else:  # 只有1个同花顺，随便取一个给后墩
                    ths1 = list(range(r[0], r[0] + 4 + 1, 1));get1 = 1;hua1 = 1
            elif len(r) == 1:  # 有1个同花顺，给后墩
                ths1 = list(range(r[0], r[0] + 4 + 1, 1));get1 = 1;hua1 = 1
        # h2
        r.clear()
        if len(h2) >= 5:  # 可能有同花顺
            for i in list(range(len(h2)-4)):
                if h2[i+4] == h2[i] + 4 and h2[i+3] == h2[i] + 3 and h2[i+2] == h2[i] + 2 and h2[i+1] == h2[i] + 1:
                    r.append(h2[i])  # 同花顺首

            if len(r) > 1:  # 有1个以上同花顺，可能重叠
                if r[len(r)-1] > r[0] + 4:  # 有两个不重叠同花顺
                    ths1 = list(range(r[0], r[0]+4+1, 1));hua1 = 2  # 小的给中墩
                    ths2 = list(range(r[len(r)-1], r[len(r)-1]+4+1, 1));hua2 = 2  # 大的给后墩
                    return 2
                else:  # 只有1个同花顺，随便取一个给后墩
                    if get1 == 1:
                        ths2 = list(range(r[0], r[0] + 4 + 1, 1));hua2 = 2;return 2
                    else:
                        ths1 = list(range(r[0], r[0] + 4 + 1, 1));hua1 = 2;get1 = 1
            elif len(r) == 1:  # 有1个同花顺，给后墩
                if get1 == 1:
                    ths2 = list(range(r[0], r[0] + 4 + 1, 1));hua2 = 2;return 2
                else:
                    ths1 = list(range(r[0], r[0] + 4 + 1, 1));hua1 = 2;get1 = 1
        # h3
        r.clear()
        if len(h3) >= 5:  # 可能有同花顺
            for i in list(range(len(h3) -4)):
                if h3[i + 4] == h3[i] + 4 and h3[i + 3] == h3[i] + 3 and h3[i + 2] == h3[i] + 2 and h3[i + 1] == h3[i] + 1:
                    r.append(h3[i])  # 同花顺首

            if len(r) > 1:  # 有1个以上同花顺，可能重叠
                if r[len(r) - 1] > r[0] + 4:  # 有两个不重叠同花顺
                    ths1 = list(range(r[0], r[0] + 4 + 1, 1));hua1 = 3  # 小的给中墩
                    ths2 = list(range(r[len(r) - 1], r[len(r) - 1] + 4 + 1, 1));hua2 = 3  # 大的给后墩
                    return 2
                else:  # 只有1个同花顺，随便取一个给后墩
                    if get1 == 1:
                        ths2 = list(range(r[0], r[0] + 4 + 1, 1));hua2 = 3;return 2
                    else:
                        ths1 = list(range(r[0], r[0] + 4 + 1, 1));hua1 = 3;get1 = 1
            elif len(r) == 1:  # 有1个同花顺，给后墩
                if get1 == 1:
                    ths2 = list(range(r[0], r[0] + 4 + 1, 1));hua2 = 3;return 2
                else:
                    ths1 = list(range(r[0], r[0] + 4 + 1, 1));hua1 = 3;get1 = 1
        # h4
        r.clear()
        if len(h2) >= 5:  # 可能有同花顺
            for i in list(range(len(h2) -4)):
                if h2[i + 4] == h2[i] + 4 and h2[i + 3] == h2[i] + 3 and h2[i + 2] == h2[i] + 2 and h2[i + 1] == h2[i] + 1:
                    r.append(h2[i])  # 同花顺首

            if len(r) > 1:  # 有1个以上同花顺，可能重叠
                if r[len(r) - 1] > r[0] + 4:  # 有两个不重叠同花顺
                    ths1 = list(range(r[0], r[0] + 4 + 1, 1));hua1 = 4  # 小的给中墩
                    ths2 = list(range(r[len(r) - 1], r[len(r) - 1] + 4 + 1, 1));hua2 = 4  # 大的给后墩
                    return 2
                else:  # 只有1个同花顺，随便取一个给后墩
                    if get1 == 1:
                        ths2 = list(range(r[0], r[0] + 4 + 1, 1));hua2 = 4;return 2
                    else:
                        ths1 = list(range(r[0], r[0] + 4 + 1, 1));hua1 = 4;get1 = 1
            elif len(r) == 1:  # 有1个同花顺，给后墩
                if get1 == 1:
                    ths2 = list(range(r[0], r[0] + 4 + 1, 1));hua2 = 4;return 2
                else:
                    ths1 = list(range(r[0], r[0] + 4 + 1, 1));hua1 = 4;get1 = 1
        if ths1 and ths2:
            return 2
        elif ths1:
            return 1
        else:
            return 0
    # 找炸弹
    def find_bomb():
        # 返回值 0 没找到 1后墩有了 2后墩中墩都有了
        # 若有炸弹，则一定是 后墩中墩都有了 或 后墩有了
        global s,bmax,mid
        if len(s) != 26:
            cre_table()
        bomb_num = []
        if len(n2) == 4:
            bomb_num.append(2)
        if len(n3) == 4:
            bomb_num.append(3)
        if len(n4) == 4:
            bomb_num.append(4)
        if len(n5) == 4:
            bomb_num.append(5)
        if len(n6) == 4:
            bomb_num.append(6)
        if len(n7) == 4:
            bomb_num.append(7)
        if len(n8) == 4:
            bomb_num.append(8)
        if len(n9) == 4:
            bomb_num.append(9)
        if len(n10) == 4:
            bomb_num.append(10)
        if len(n11) == 4:
            bomb_num.append(11)
        if len(n12) == 4:
            bomb_num.append(12)
        if len(n13) == 4:
            bomb_num.append(13)
        if len(n1) == 4:
            bomb_num.append(14)

        if len(s) == 26:
            if len(bomb_num) == 3:  # 3个炸弹
                bmax = bomb_num[0]
                if bomb_num[1] > bmax:
                    bmax = bomb_num[1]
                if bomb_num[2] > bmax:
                    bmax = bomb_num[2]  #最大给后墩
                # 中间给中墩
                if bomb_num[0] == bmax:
                    if bomb_num[1] < bomb_num[2]:
                        mid = bomb_num[2]
                    else:
                        mid = bomb_num[1]
                if bomb_num[1] == bmax:
                    if bomb_num[0] < bomb_num[2]:
                        mid = bomb_num[2]
                    else:
                        mid = bomb_num[0]
                if bomb_num[2] == bmax:
                    if bomb_num[1] < bomb_num[0]:
                        mid = bomb_num[0]
                    else:
                        mid = bomb_num[1]
                return 2
            elif len(bomb_num) == 2:  # 2个炸弹
                bmax = bomb_num[0]
                if bmax < bomb_num[1]:
                    bmax = bomb_num[1]
                    mid = bomb_num[0]
                else:
                    mid = bomb_num[1]
                return 2
            elif len(bomb_num) == 1:  # 1个炸弹
                bmax =  bomb_num[0]
                return 1
            else:
                return 0  # 没炸弹
        else:  # 找给中墩
            if len(bomb_num) == 2:  # 2个炸弹
                mid = bomb_num[0]
                if mid < bomb_num[1]:
                    mid = bomb_num[1]
                return 2
            elif len(bomb_num) == 1:  # 1个炸弹
                mid =  bomb_num[0]
            else:
                return 0  # 没炸弹
    # 找葫芦
    def find_hulu():
        # 返回 2 够2个葫芦 1 1葫芦  0 无葫芦
        if len(s) != 26:
            cre_table()
        global hulu_num, hulu2_num, hulu
        if len(n2) == 3:
            hulu_num.append(2)
        if len(n3) == 3:
            hulu_num.append(3)
        if len(n4) == 3:
            hulu_num.append(4)
        if len(n5) == 3:
            hulu_num.append(5)
        if len(n6) == 3:
            hulu_num.append(6)
        if len(n7) == 3:
            hulu_num.append(7)
        if len(n8) == 3:
            hulu_num.append(8)
        if len(n9) == 3:
            hulu_num.append(9)
        if len(n10) == 3:
            hulu_num.append(10)
        if len(n11) == 3:
            hulu_num.append(11)
        if len(n12) == 3:
            hulu_num.append(12)
        if len(n13) == 3:
            hulu_num.append(13)
        if len(n1) == 3:
            hulu_num.append(14)

        if len(n2) == 2:
            hulu2_num.append(2)
        if len(n3) == 2:
            hulu2_num.append(3)
        if len(n4) == 2:
            hulu2_num.append(4)
        if len(n5) == 2:
            hulu2_num.append(5)
        if len(n6) == 2:
            hulu2_num.append(6)
        if len(n7) == 2:
            hulu2_num.append(7)
        if len(n8) == 2:
            hulu2_num.append(8)
        if len(n9) == 2:
            hulu2_num.append(9)
        if len(n10) == 2:
            hulu2_num.append(10)
        if len(n11) == 2:
            hulu2_num.append(11)
        if len(n12) == 2:
            hulu2_num.append(12)
        if len(n13) == 2:
            hulu2_num.append(13)
        if len(n1) == 2:
            hulu2_num.append(14)

        if len(hulu_num) == 0 or len(hulu2_num) == 0:
            return 0
        elif len(hulu_num) == 1 and len(hulu2_num) == 1:
            return 0
        elif len(hulu_num) == 1 and len(hulu2_num) > 1:
            hulu.append(hulu_num[0])
            if hulu_num[0] in hulu2_num:
                hulu2_num.remove(hulu_num[0])
            return 1
        elif len(hulu_num) > 1 and len(hulu2_num) == 1:
            if hulu2_num[0] in hulu_num:
                hulu_num.remove(hulu2_num[0])
            hulu.append(max(hulu_num))
            return 1
        elif len(hulu_num) > 1 and len(hulu2_num) > 1:
            if len(hulu_num) == 2 and len(hulu2_num) == 2:
                if hulu_num[0] not in hulu2_num and hulu_num[1] not in hulu2_num:
                    return 2
                elif hulu_num[0] not in hulu2_num and hulu_num[1] in hulu2_num:
                    hulu.append(max(hulu_num))
                    hulu2_num.remove(hulu[0])
                    return 1
                elif hulu_num[0] in hulu2_num and hulu_num[1] not in hulu2_num:
                    hulu.append(max(hulu_num))
                    hulu2_num.remove(hulu[0])
                    return 1
                elif hulu_num[0] in hulu2_num and hulu_num[1] in hulu2_num:
                    hulu.append(max(hulu_num))
                    hulu2_num.remove(hulu[0])
                    return 1
            elif len(hulu_num) == 2 and len(hulu2_num) == 3:  #直接用，hulu和hulu2_num没相交，另外hulu数目最多就2
                if hulu_num[0] in hulu2_num and hulu_num[1] in hulu2_num:
                    hulu.append(max(hulu_num))
                    hulu2_num.remove(hulu[0])
                    return 1
                if hulu_num[0] in hulu2_num and hulu_num[1] not in hulu2_num:
                    hulu.append(hulu_num[0])
                    hulu.append(hulu_num[1])
                    hulu2_num.remove(hulu_num[0])
                    return 2
                if hulu_num[0] not in hulu2_num and hulu_num[1] in hulu2_num:
                    hulu.append(hulu_num[0])
                    hulu.append(hulu_num[1])
                    hulu2_num.remove(hulu_num[1])
                    return 2
                if hulu_num[0] not in hulu2_num and hulu_num[1] not in hulu2_num:
                    hulu.append(hulu_num[0])
                    hulu.append(hulu_num[1])
                    return 2
            elif len(hulu_num) == 3 and len(hulu2_num) == 2:
                if hulu2_num[0] in hulu_num and hulu2_num[1] in hulu_num:
                    hulu.append(max(hulu_num))
                    hulu2_num.remove(hulu[0])
                    return 1
                if hulu2_num[0] in hulu_num and hulu2_num[1] not in hulu_num:
                    hulu_num.remove(hulu2_num[0])
                    hulu.append(hulu_num[0])
                    hulu.append(hulu_num[1])
                    return 2
                if hulu2_num[0] not in hulu_num and hulu2_num[1] in hulu_num:
                    hulu_num.remove(hulu2_num[1])
                    hulu.append(hulu_num[0])
                    hulu.append(hulu_num[1])
                    return 2
                if hulu2_num[0] not in hulu_num and hulu2_num[1] not in hulu_num:
                    hulu.append(max(hulu_num))
                    hulu_num.remove(hulu[0])
                    hulu.append(max(hulu_num))
                    return 2
            elif len(hulu_num) == 3 and len(hulu2_num) == 3:
                if hulu_num[0] in hulu2_num and hulu_num[1] in hulu2_num and hulu_num[2] in hulu2_num:
                    hulu.append(max(hulu_num))
                    hulu2_num.remove(hulu[0])
                    return 1
                if hulu_num[0] not in hulu2_num and hulu_num[1] in hulu2_num and hulu_num[2] in hulu2_num:
                    hulu.append(hulu_num[0])
                    hulu_num.remove(hulu[0])
                    hulu.append(max(hulu_num))
                    hulu2_num.remove(hulu[1])
                    return 2
                if hulu_num[0] in hulu2_num and hulu_num[1] not in hulu2_num and hulu_num[2] in hulu2_num:
                    hulu.append(hulu_num[1])
                    hulu_num.remove(hulu[0])
                    hulu.append(max(hulu_num))
                    hulu2_num.remove(hulu[1])
                    return 2
                if hulu_num[0] in hulu2_num and hulu_num[1] in hulu2_num and hulu_num[2] not in hulu2_num:
                    hulu.append(hulu_num[2])
                    hulu_num.remove(hulu[0])
                    hulu.append(max(hulu_num))
                    hulu2_num.remove(hulu[1])
                    return 2
                if hulu_num[0] in hulu2_num and hulu_num[1] not in hulu2_num and hulu_num[2] not in hulu2_num:
                    hulu.append(max(hulu_num))
                    hulu_num.remove(hulu[0])
                    hulu.append(max(hulu_num))
                    if hulu[0] in hulu2_num:
                        hulu2_num.remove(hulu[0])
                    if hulu[1] in hulu2_num:
                        hulu2_num.remove(hulu[1])
                    return 2
                if hulu_num[0] not in hulu2_num and hulu_num[1] in hulu2_num and hulu_num[2] not in hulu2_num:
                    hulu.append(max(hulu_num))
                    hulu_num.remove(hulu[0])
                    hulu.append(max(hulu_num))
                    if hulu[0] in hulu2_num:
                        hulu2_num.remove(hulu[0])
                    if hulu[1] in hulu2_num:
                        hulu2_num.remove(hulu[1])
                    return 2
                if hulu_num[0] not in hulu2_num and hulu_num[1] not in hulu2_num and hulu_num[2] in hulu2_num:
                    hulu.append(max(hulu_num))
                    hulu_num.remove(hulu[0])
                    hulu.append(max(hulu_num))
                    if hulu[0] in hulu2_num:
                        hulu2_num.remove(hulu[0])
                    if hulu[1] in hulu2_num:
                        hulu2_num.remove(hulu[1])
                    return 2
                if hulu_num[0] not in hulu2_num and hulu_num[1] not in hulu2_num and hulu_num[2] not in hulu2_num:
                    hulu.append(max(hulu_num))
                    hulu_num.remove(hulu[0])
                    hulu.append(max(hulu_num))
                    return 2
            elif len(hulu_num) == 3 and len(hulu2_num) == 4:
                hulu.append(max(hulu_num))
                hulu_num.remove(hulu[0])
                hulu.append(max(hulu_num))
                if hulu[0] in hulu2_num:
                    hulu2_num.remove(hulu[0])
                if hulu[1] in hulu2_num:
                    hulu2_num.remove(hulu[1])
                return 2
            elif len(hulu_num) == 4 and len(hulu2_num) == 3:
                if hulu2_num[0] in hulu_num and hulu2_num[1] in hulu_num and hulu2_num[2] in hulu_num:
                    for ii in hulu_num:
                        if ii not in hulu2_num:
                            hulu.append(ii)
                            hulu_num.remove(ii)
                    hulu.append(max(hulu_num))
                    hulu2_num.remove(hulu[1])
                    return 2
                elif hulu2_num[0] not in hulu_num and hulu2_num[1] in hulu_num and hulu2_num[2] in hulu_num:
                    if hulu2_num[1] > hulu2_num[2]:
                        hulu.append(hulu2_num[1])
                        hulu2_num.remove(hulu2_num[1])
                        hulu_num.remove(hulu2_num[1])
                        hulu_num.remove(hulu2_num[2])
                        hulu.append(max(hulu_num))
                    else:
                        hulu.append(hulu2_num[2])
                        hulu2_num.remove(hulu2_num[2])
                        hulu_num.remove(hulu2_num[1])
                        hulu_num.remove(hulu2_num[2])
                        hulu.append(max(hulu_num))
                    return 2
                elif hulu2_num[0] in hulu_num and hulu2_num[1] not in hulu_num and hulu2_num[2] in hulu_num:
                    if hulu2_num[0] > hulu2_num[2]:
                        hulu.append(hulu2_num[0])
                        hulu2_num.remove(hulu2_num[0])
                        hulu_num.remove(hulu2_num[0])
                        hulu_num.remove(hulu2_num[2])
                        hulu.append(max(hulu_num))
                    else:
                        hulu.append(hulu2_num[2])
                        hulu2_num.remove(hulu2_num[2])
                        hulu_num.remove(hulu2_num[0])
                        hulu_num.remove(hulu2_num[2])
                        hulu.append(max(hulu_num))
                    return 2
                elif hulu2_num[0] in hulu_num and hulu2_num[1] in hulu_num and hulu2_num[2] not in hulu_num:
                    if hulu2_num[0] > hulu2_num[1]:
                        hulu.append(hulu2_num[0])
                        hulu2_num.remove(hulu2_num[0])
                        hulu_num.remove(hulu2_num[0])
                        hulu_num.remove(hulu2_num[1])
                        hulu.append(max(hulu_num))
                    else:
                        hulu.append(hulu2_num[1])
                        hulu2_num.remove(hulu2_num[1])
                        hulu_num.remove(hulu2_num[0])
                        hulu_num.remove(hulu2_num[1])
                        hulu.append(max(hulu_num))
                    return 2
                else:
                    hulu.append(max(hulu_num))
                    hulu_num.remove(hulu[0])
                    hulu.append(max(hulu_num))
                    if hulu[0] in hulu2_num:
                        hulu2_num.remove(hulu[0])
                    if hulu[1] in hulu2_num:
                        hulu2_num.remove(hulu[1])
                    return 2
            elif len(hulu_num) == 4 and len(hulu2_num) == 4:
                hulu.append(max(hulu_num))
                hulu_num.remove(hulu[0])
                hulu.append(max(hulu_num))
                hulu2_num.remove(hulu[0])
                hulu2_num.remove(hulu[1])
                return 2
    # 找同花
    def find_tonghua():
        # 返回2 2同花 1 1同花 0 无同花
        global tonghua_da, da_hua, tonghua_xiao, xiao_hua
        tonghua_max = 0
        if len(s) != 26:
            cre_table()
        tonghua = []
        if len(h1) >= 5:
            tonghua.append(1)
        if len(h2) >= 5:
            tonghua.append(2)
        if len(h3) >= 5:
            tonghua.append(3)
        if len(h4) >= 5:
            tonghua.append(4)
        if len(tonghua) == 2:  # 有2个同花
            for i in tonghua:
                if i == 1:
                    if max(h1) > tonghua_da:
                        tonghua_da = max(h1);da_hua = 1
                if i == 2:
                    if max(h2) > tonghua_da:
                        tonghua_da = max(h2);da_hua = 2
                if i == 3:
                    if max(h3) > tonghua_da:
                        tonghua_da = max(h3);da_hua = 3
                if i == 4:
                    if max(h4) > tonghua_da:
                        tonghua_da = max(h4);da_hua = 4
            for j in tonghua:
                if j == 1:
                    if max(h1) != tonghua_da:
                        tonghua_xiao = max(h1);xiao_hua = 1
                if j == 2:
                    if max(h2) != tonghua_da:
                        tonghua_xiao = max(h2);xiao_hua = 2
                if j == 3:
                    if max(h3) != tonghua_da:
                        tonghua_xiao = max(h3);xiao_hua = 3
                if j == 4:
                    if max(h4) != tonghua_da:
                        tonghua_xiao = max(h4);xiao_hua = 4
            return 2
        elif len(tonghua)  == 1:  # 有1个同花
            for i in tonghua:
                if i == 1:
                    tonghua_da = max(h1);da_hua = 1
                if i == 2:
                    tonghua_da = max(h2);da_hua = 2
                if i == 3:
                    tonghua_da = max(h3);da_hua = 3
                if i == 4:
                    tonghua_da = max(h4);da_hua = 4
            return 1
        else:  # 无同花
            return 0
    # 找顺子
    def find_shunzi():
        # 返回2 2顺子 1 1顺子 0 无顺子
        global shunzi_da, shunzi_xiao
        shu = []
        shunzi = []
        for i in s:
            if i in ['2','3','4','5','6','7','8','9','T','J','Q','K','A']:
                shu.append(trans_num(i))
        shu.sort()
        for j in range(len(shu)-5):
            if shu[j] + 4 == shu[j+4] and shu[j] + 3 == shu[j+3] and shu[j] + 2 == shu[j+2] and shu[j] + 1 == shu[j+1]:
                shunzi.append(shu[j])
        if shunzi:
            if max(shunzi) - min(shunzi) > 4:  # 有2个顺子
                shunzi_da = max(shunzi)
                shunzi.remove(shunzi_da)
                shunzi_xiao = max(shunzi)
                return 2
            else:  # 1个顺子
                shunzi_da = max(shunzi)
                return 1
        else:
            return 0
    # 找三条
    def find_santiao():
        # 返回 2 2三条 1 1三条  0无三条
        if len(s) != 26:
            cre_table()
        santiao_num = []
        global santiao_da, santiao_xiao
        if len(n2) == 3:
            santiao_num.append(2)
        if len(n3) == 3:
            santiao_num.append(3)
        if len(n4) == 3:
            santiao_num.append(4)
        if len(n5) == 3:
            santiao_num.append(5)
        if len(n6) == 3:
            santiao_num.append(6)
        if len(n7) == 3:
            santiao_num.append(7)
        if len(n8) == 3:
            santiao_num.append(8)
        if len(n9) == 3:
            santiao_num.append(9)
        if len(n10) == 3:
            santiao_num.append(10)
        if len(n11) == 3:
            santiao_num.append(11)
        if len(n12) == 3:
            santiao_num.append(12)
        if len(n13) == 3:
            santiao_num.append(13)
        if len(n1) == 3:
            santiao_num.append(14)
        if len(santiao_num) == 0:  # 没有三条
            return 0
        elif len(santiao_num) == 1:  # 1个三条
            santiao_da = santiao_num[0];return 1
        elif len(santiao_num) > 1:  # 两个及以上三条
            santiao_da = max(santiao_num)
            santiao_num.remove(max(santiao_num))
            santiao_xiao = max(santiao_num)
            return 2
    # 处理散牌
    def chuli_sanpai():
        global qdun, zdun, hdun
        if len(s) == 26:
            t = [[0 for i in range(2)]for i in range(13)]
            p = 0
            for i in list(range(0, len(s), 2)):
                t[p][0] = s[i]
                t[p][1] = trans_num(s[i + 1])
                p += 1
            t = sorted(t, key=lambda x: x[1])
            for i in list(range(0,3,1)):
                qdun += t[i][0]
                qdun += ntoc(t[i][1])
            for i in list(range(3,8,1)):
                zdun += t[i][0]
                zdun += ntoc(t[i][1])
            for i in list(range(8,13,1)):
                hdun += t[i][0]
                hdun += ntoc(t[i][1])
        else:  # 后墩已好
            t = [[0 for i in range(2)] for i in range(8)]
            p = 0
            for i in list(range(0, len(s), 2)):
                t[p][0] = s[i]
                t[p][1] = trans_num(s[i + 1])
                p += 1
            t = sorted(t, key=lambda x: x[1])
            for i in list(range(0,3,1)):
                qdun += t[i][0]
                qdun += ntoc(t[i][1])
            for i in list(range(3,8,1)):
                zdun += t[i][0]
                zdun += ntoc(t[i][1])
    # 主函数
    def AI():
        global qdun, hdun, zdun, s, ans
        cre_table()
        #  先处理后墩中墩
        a1 = find_tonghuashun()
        if a1 == 2:  #后墩中墩好了
            if ths1[0] > ths2[0]:
                i = 0
                while 1:
                    if i == 5:
                        break
                    hdun += nth(hua1)
                    hdun += ntoc(ths1[i])
                    s = s.replace(nth(hua1)+ntocT(ths1[i]), '', 1)
                    i += 1
                j = 0
                while 1:
                    if j == 5:
                        break
                    zdun += nth(hua2)
                    zdun += ntoc(ths2[j])
                    s = s.replace(nth(hua2) + ntocT(ths2[j]), '', 1)
                    j += 1
            else:
                i = 0
                while 1:
                    if i == 5:
                        break
                    zdun += nth(hua1)
                    zdun += ntoc(ths1[i])
                    s = s.replace(nth(hua1) + ntocT(ths1[i]), '', 1)
                    i += 1
                j = 0
                while 1:
                    if j == 5:
                        break
                    hdun += nth(hua2)
                    hdun += ntoc(ths2[j])
                    s = s.replace(nth(hua2) + ntocT(ths2[j]), '', 1)
                    j += 1
        elif a1 == 1:  # 后墩好了
            i = 0
            while 1:
                if i == 5:
                    break
                hdun += nth(hua1)
                hdun += ntoc(ths1[i])
                s = s.replace(nth(hua1) + ntocT(ths1[i]), '', 1)
                i += 1
            a2 = find_bomb()
            if a2 >= 1:  #后墩中墩好了
                zdun += '*'
                zdun += ntoc(mid)
                z = '*' + ntocT(mid)
                s = s.replace(z, '', 1)
                zdun += '&'
                zdun += ntoc(mid)
                z = '&' + ntocT(mid)
                s = s.replace(z, '', 1)
                zdun += '#'
                zdun += ntoc(mid)
                z = '#' + ntocT(mid)
                s = s.replace(z, '', 1)
                zdun += '$'
                zdun += ntoc(mid)
                z = '$' + ntocT(mid)
                s = s.replace(z, '', 1)
            elif a2 == 0:
                a3 = find_hulu()
                if a3 == 1:
                    m = 0
                    k = 0
                    while 1:
                        if k > len(s)-1:
                            break
                        if s[k] == ntocTA(hulu_num[0]):
                            z = s[k-1] + s[k]
                            zdun += z
                            s = s.replace(z, '', 1)
                            k = k - 2
                        if m < 2:
                            if s[k] == ntocTA(max(hulu2_num)):
                                z = s[k-1] + s[k]
                                zdun += z
                                s = s.replace(z, '', 1)
                                k = k - 2
                                m+=1
                        k += 1
                elif a3 == 0:
                    a4 = find_tonghua()
                    if a4 == 1:  # 后墩中墩好了
                        zdun += nth(da_hua)
                        zdun += ntoc(tonghua_da)
                        s = s.replace(nth(da_hua)+ntocT(tonghua_da), '', 1)
                        ro = 0
                        k2 = 0
                        while 1:
                            if k2 > len(s)-1:
                                break
                            if ro == 4:
                                break
                            if s[k2] == nth(da_hua):
                                zdun += s[k2]
                                zdun += s[k2+1]
                                s = s.replace(s[k2] + s[k2+1], '', 1)
                                k2 = k2 - 2
                                ro += 1
                            k2 += 1
                    elif a4 == 0:
                        a5 = find_shunzi()
                        if a5 == 1:  # 后墩中墩好了
                            k3 = 0
                            while 1:
                                if k3 > len(s)-1:
                                    break
                                if s[k3] == ntocT(shunzi_da):
                                    zdun += s[k3-1]
                                    zdun += s[k3]
                                    s = s.replace(s[k3-1] + s[k3], '', 1)
                                    k3 = k3 - 2
                                if s[k3] == ntocT(shunzi_da+1):
                                    zdun += s[k3-1]
                                    zdun += s[k3]
                                    s = s.replace(s[k3-1] + s[k3], '', 1)
                                    k3 = k3 - 2
                                if s[k3] == ntocT(shunzi_da+2):
                                    zdun += s[k3-1]
                                    zdun += s[k3]
                                    s = s.replace(s[k3-1] + s[k3], '', 1)
                                    k3 = k3 - 2
                                if s[k3] == ntocT(shunzi_da+3):
                                    zdun += s[k3-1]
                                    zdun += s[k3]
                                    s = s.replace(s[k3-1] + s[k3], '', 1)
                                    k3 = k3 - 2
                                if s[k3] == ntocT(shunzi_da+4):
                                    zdun += s[k3-1]
                                    zdun += s[k3]
                                    s = s.replace(s[k3-1] + s[k3], '', 1)
                                    k3 = k3 - 2
                                k3 += 1
                        elif a5 == 0:
                            a6 = find_santiao()
                            if a6 >= 1:  # 后墩中墩好了
                                k4 = 0
                                while 1:
                                    if k4 > len(s) - 1:
                                        break
                                    if s[k4] == ntocT(santiao_da):
                                        zdun += s[k4 - 1]
                                        zdun += s[k4]
                                        s = s.replace(s[k4 - 1] + s[k4], '', 1)
                                        k4 = k4 - 2
                                    k4 += 1
                                zdun += s[0]
                                zdun += s[1]
                                zdun += s[2]
                                zdun += s[3]
                                s = s.replace(s[0] + s[1] + s[2] + s[3], '', 1)
                            elif a6 == 0:
                                chuli_sanpai()
        elif a1 == 0:  #无同花顺
            a2 = find_bomb()
            if a2 == 2:  # 后墩中墩好了
                hdun += '*'
                hdun += ntoc(bmax)
                z = '*' + ntocT(bmax)
                s = s.replace(z, '', 1)
                hdun += '&'
                hdun += ntoc(bmax)
                z = '&' + ntocT(bmax)
                s = s.replace(z, '', 1)
                hdun += '#'
                hdun += ntoc(bmax)
                z = '#' + ntocT(bmax)
                s = s.replace(z, '', 1)
                hdun += '$'
                hdun += ntoc(bmax)
                z = '$' + ntocT(bmax)
                s = s.replace(z, '', 1)
                H = 0
                for h in list(range(1, len(s), 2)):
                    if H > 0:
                        break
                    if(s[h] != ntocTA(mid)):
                        hdun += s[h-1]
                        hdun += s[h]
                        s = s.replace(s[h-1] + s[h], '', 1)
                        H += 1
                zdun += '*'
                zdun += ntoc(mid)
                z = '*' + ntocTA(mid)
                s = s.replace(z, '', 1)
                zdun += '&'
                zdun += ntoc(mid)
                z = '&' + ntocTA(mid)
                s = s.replace(z, '', 1)
                zdun += '#'
                zdun += ntoc(mid)
                z = '#' + ntocTA(mid)
                s = s.replace(z, '', 1)
                zdun += '$'
                zdun += ntoc(mid)
                z = '$' + ntocTA(mid)
                s = s.replace(z, '', 1)
                zdun += s[0]
                zdun += s[1]
                s = s.replace(s[0] + s[1], '', 1)
            elif a2 == 1:  # 后墩好了
                hdun += '*'
                hdun += ntoc(bmax)
                z = '*' + ntocT(bmax)
                s = s.replace(z, '', 1)
                hdun += '&'
                hdun += ntoc(bmax)
                z = '&' + ntocT(bmax)
                s = s.replace(z, '', 1)
                hdun += '#'
                hdun += ntoc(bmax)
                z = '#' + ntocT(bmax)
                s = s.replace(z, '', 1)
                hdun += '$'
                hdun += ntoc(bmax)
                z = '$' + ntocT(bmax)
                s = s.replace(z, '', 1)
                hdun += s[0]
                hdun += s[1]
                s = s.replace(s[0] + s[1], '', 1)
                a3 = find_hulu()
                if a3 == 1:
                    m = 0
                    k = 0
                    while 1:
                        if k > len(s)-1:
                            break
                        if s[k] == ntocTA(hulu_num[0]):
                            z = s[k-1] + s[k]
                            zdun += z
                            s = s.replace(z, '', 1)
                            k = k - 2
                        if m < 2:
                            if s[k] == ntocTA(max(hulu2_num)):
                                z = s[k-1] + s[k]
                                zdun += z
                                s = s.replace(z, '', 1)
                                k = k - 2
                                m+=1
                        k += 1
                elif a3 == 0:
                    a4 = find_tonghua()
                    if a4 == 1:  # 后墩中墩好了
                        zdun += nth(da_hua)
                        zdun += ntoc(tonghua_da)
                        s = s.replace(nth(da_hua)+ntocT(tonghua_da), '', 1)
                        ro = 0
                        k2 = 0
                        while 1:
                            if k2 > len(s)-1:
                                break
                            if ro == 4:
                                break
                            if s[k2] == nth(da_hua):
                                zdun += s[k2]
                                zdun += s[k2+1]
                                s = s.replace(s[k2] + s[k2+1], '', 1)
                                k2 = k2 - 2
                                ro += 1
                            k2 += 1
                    elif a4 == 0:
                        a5 = find_shunzi()
                        if a5 == 1:  # 后墩中墩好了
                            k3 = 0
                            while 1:
                                if k3 > len(s)-1:
                                    break
                                if s[k3] == ntocT(shunzi_da):
                                    zdun += s[k3-1]
                                    zdun += s[k3]
                                    s = s.replace(s[k3-1] + s[k3], '', 1)
                                    k3 = k3 - 2
                                if s[k3] == ntocT(shunzi_da+1):
                                    zdun += s[k3-1]
                                    zdun += s[k3]
                                    s = s.replace(s[k3-1] + s[k3], '', 1)
                                    k3 = k3 - 2
                                if s[k3] == ntocT(shunzi_da+2):
                                    zdun += s[k3-1]
                                    zdun += s[k3]
                                    s = s.replace(s[k3-1] + s[k3], '', 1)
                                    k3 = k3 - 2
                                if s[k3] == ntocT(shunzi_da+3):
                                    zdun += s[k3-1]
                                    zdun += s[k3]
                                    s = s.replace(s[k3-1] + s[k3], '', 1)
                                    k3 = k3 - 2
                                if s[k3] == ntocT(shunzi_da+4):
                                    zdun += s[k3-1]
                                    zdun += s[k3]
                                    s = s.replace(s[k3-1] + s[k3], '', 1)
                                    k3 = k3 - 2
                                k3 += 1
                        elif a5 == 0:
                            a6 = find_santiao()
                            if a6 >= 1:  # 后墩中墩好了
                                k4 = 0
                                while 1:
                                    if k4 > len(s)-1:
                                        break
                                    if s[k4] == ntocT(santiao_da):
                                        zdun += s[k4-1]
                                        zdun += s[k4]
                                        s = s.replace(s[k4 - 1] + s[k4], '', 1)
                                        k4 = k4 - 2
                                    k4 += 1
                                zdun += s[0]
                                zdun += s[1]
                                zdun += s[2]
                                zdun += s[3]
                                s = s.replace(s[0] + s[1] + s[2] + s[3], '', 1)
                            elif a6 == 0:
                                chuli_sanpai()
            elif a2 == 0:
                a3 = find_hulu()
                if a3 == 2:  # 后墩中墩好了
                    if hulu_num[0] < hulu_num[1]:
                        m = 0
                        m2 = 0
                        k = 0
                        while 1:
                            if k > len(s)-1:
                                break
                            if s[k] == ntocTA(hulu_num[0]):
                                z = s[k-1] + s[k]
                                zdun += z
                                s = s.replace(z, '', 1)
                                k = k - 2
                            if m < 2:
                                if s[k] == ntocTA(min(hulu2_num)):
                                    z = s[k-1] + s[k]
                                    zdun += z
                                    s = s.replace(z, '', 1)
                                    k = k - 2
                                    m += 1
                            if s[k] == ntocTA(hulu_num[1]):
                                z = s[k-1] + s[k]
                                hdun += z
                                s = s.replace(z, '', 1)
                                k = k - 2
                            if m2 < 2:
                                if s[k] == ntocTA(max(hulu2_num)):
                                    z = s[k-1] + s[k]
                                    hdun += z
                                    s = s.replace(z, '', 1)
                                    k = k - 2
                                    m2 += 1
                            k += 1
                    else:
                        m = 0
                        m2 = 0
                        k = 0
                        while 1:
                            if k > len(s)-1:
                                break
                            if s[k] == ntocTA(hulu_num[1]):
                                z = s[k-1] + s[k]
                                zdun += z
                                s = s.replace(z, '', 1)
                                k = k - 2
                            if m < 2:
                                if s[k] == ntocTA(min(hulu2_num)):
                                    z = s[k-1] + s[k]
                                    zdun += z
                                    s = s.replace(z, '', 1)
                                    k = k - 2
                                    m += 1
                            if s[k] == ntocTA(hulu_num[0]):
                                z = s[k-1] + s[k]
                                hdun += z
                                s = s.replace(z, '', 1)
                                k = k - 2
                            if m2 < 2:
                                if s[k] == ntocTA(max(hulu2_num)):
                                    z = s[k-1] + s[k]
                                    hdun += z
                                    s = s.replace(z, '', 1)
                                    k = k - 2
                                    m2 += 1
                            k += 1
                elif a3 == 1:  # 后墩好了
                    m = 0
                    k = 1
                    while 1:
                        if k > len(s)-1:
                            break
                        if s[k] == ntocTA(hulu_num[0]):
                            z = s[k-1] + s[k]
                            hdun += z
                            s = s.replace(z, '', 1)
                            k = k - 2
                        if m < 2:
                            if s[k] == ntocTA(max(hulu2_num)):
                                z = s[k-1] + s[k]
                                hdun += z
                                s = s.replace(z, '', 1)
                                k = k - 2
                                m += 1
                        k += 1
                    a4 = find_tonghua()
                    if a4 == 1:  # 后墩中墩好了
                        zdun += nth(da_hua)
                        zdun += ntoc(tonghua_da)
                        s = s.replace(nth(da_hua) + ntocT(tonghua_da), '', 1)
                        ro = 0
                        k2 = 0
                        while 1:
                            if k2 > len(s)-1:
                                break
                            if ro == 4:
                                break
                            if s[k2] == nth(da_hua):
                                zdun += s[k2]
                                zdun += s[k2 + 1]
                                s = s.replace(s[k2] + s[k2 + 1], '', 1)
                                k2 = k2 - 2
                                ro += 1
                            k2 += 1
                    elif a4 == 0:
                        a5 = find_shunzi()
                        if a5 == 1:  # 后墩中墩好了
                            k3 = 0
                            y1 = 0
                            y2 = 0
                            y3 = 0
                            y4 = 0
                            y5 = 0
                            while 1:
                                if k3 > len(s)-1:
                                    break
                                if y1 < 1:
                                    if s[k3] == ntocT(shunzi_da):
                                        zdun += s[k3 - 1]
                                        zdun += s[k3]
                                        s = s.replace(s[k3 - 1] + s[k3], '', 1)
                                        k3 = k3 - 2
                                        y1 += 1
                                if y2 < 1:
                                    if s[k3] == ntocT(shunzi_da + 1):
                                        zdun += s[k3 - 1]
                                        zdun += s[k3]
                                        s = s.replace(s[k3 - 1] + s[k3], '', 1)
                                        k3 = k3 - 2
                                        y2 += 1
                                if y3 < 1:
                                    if s[k3] == ntocT(shunzi_da + 2):
                                        zdun += s[k3 - 1]
                                        zdun += s[k3]
                                        s = s.replace(s[k3 - 1] + s[k3], '', 1)
                                        k3 = k3 - 2
                                        y3 += 1
                                if y4 < 1:
                                    if s[k3] == ntocT(shunzi_da + 3):
                                        zdun += s[k3 - 1]
                                        zdun += s[k3]
                                        s = s.replace(s[k3 - 1] + s[k3], '', 1)
                                        k3 = k3 - 2
                                        y4 += 1
                                if y5 < 1:
                                    if s[k3] == ntocT(shunzi_da + 4):
                                        zdun += s[k3 - 1]
                                        zdun += s[k3]
                                        s = s.replace(s[k3 - 1] + s[k3], '', 1)
                                        k3 = k3 - 2
                                        y5 += 1
                                k3 += 1
                        elif a5 == 0:
                            a6 = find_santiao()
                            if a6 >= 1:  # 后墩中墩好了
                                k4 = 0
                                while 1:
                                    if k4 > len(s)-1:
                                        break
                                    if s[k4] == ntocT(santiao_da):
                                        zdun += s[k4 - 1]
                                        zdun += s[k4]
                                        s = s.replace(s[k4 - 1] + s[k4], '', 1)
                                        k4 = k4 - 2
                                    k4 += 1
                                zdun += s[0]
                                zdun += s[1]
                                zdun += s[2]
                                zdun += s[3]
                                s = s.replace(s[0] + s[1] + s[2] + s[3], '', 1)
                            elif a6 == 0:
                                chuli_sanpai()
                elif a3 == 0:
                    a4 = find_tonghua()
                    if a4 == 2:  # 后墩中墩好了
                        hdun += nth(da_hua)
                        hdun += ntoc(tonghua_da)
                        s = s.replace(nth(da_hua)+ntocT(tonghua_da), '', 1)
                        ro = 0
                        k2 = 0
                        while 1:
                            if k2 > len(s)-1:
                                break
                            if ro == 4:
                                break
                            if s[k2] == nth(da_hua):
                                hdun += s[k2]
                                hdun += s[k2+1]
                                s = s.replace(s[k2] + s[k2+1], '', 1)
                                k2 = k2 - 2
                                ro += 1
                            k2 += 1
                        zdun += nth(xiao_hua)
                        zdun += ntoc(tonghua_xiao)
                        s = s.replace(nth(xiao_hua) + ntocT(tonghua_xiao), '', 1)
                        ro = 0
                        k2 = 0
                        while 1:
                            if k2 > len(s)-1:
                                break
                            if ro == 4:
                                break
                            if s[k2] == nth(xiao_hua):
                                zdun += s[k2]
                                zdun += s[k2 + 1]
                                s = s.replace(s[k2] + s[k2 + 1], '', 1)
                                k2 = k2 - 2
                                ro += 1
                            k2 += 1
                    elif a4 == 1:  # 后墩好了
                        hdun += nth(da_hua)
                        hdun += ntoc(tonghua_da)
                        s = s.replace(nth(da_hua) + ntocT(tonghua_da), '', 1)
                        ro = 0
                        k2 = 0
                        while 1:
                            if k2 > len(s)-1:
                                break
                            if ro == 4:
                                break
                            if s[k2] == nth(da_hua):
                                hdun += s[k2]
                                hdun += s[k2 + 1]
                                s = s.replace(s[k2] + s[k2 + 1], '', 1)
                                k2 = k2 - 2
                                ro += 1
                            k2 += 1
                        a5 = find_shunzi()
                        if a5 == 1:  # 后墩中墩好了
                            k3 = 0
                            y1 = 0
                            y2 = 0
                            y3 = 0
                            y4 = 0
                            y5 = 0
                            while 1:
                                if k3 > len(s)-1:
                                    break
                                if y1 < 1:
                                    if s[k3] == ntocT(shunzi_da):
                                        zdun += s[k3 - 1]
                                        zdun += s[k3]
                                        s = s.replace(s[k3 - 1] + s[k3], '', 1)
                                        k3 = k3 - 2
                                        y1 += 1
                                if y2 < 1:
                                    if s[k3] == ntocT(shunzi_da + 1):
                                        zdun += s[k3 - 1]
                                        zdun += s[k3]
                                        s = s.replace(s[k3 - 1] + s[k3], '', 1)
                                        k3 = k3 - 2
                                        y2 += 1
                                if y3 < 1:
                                    if s[k3] == ntocT(shunzi_da + 2):
                                        zdun += s[k3 - 1]
                                        zdun += s[k3]
                                        s = s.replace(s[k3 - 1] + s[k3], '', 1)
                                        k3 = k3 - 2
                                        y3 += 1
                                if y4 < 1:
                                    if s[k3] == ntocT(shunzi_da + 3):
                                        zdun += s[k3 - 1]
                                        zdun += s[k3]
                                        s = s.replace(s[k3 - 1] + s[k3], '', 1)
                                        k3 = k3 - 2
                                        y4 += 1
                                if y5 < 1:
                                    if s[k3] == ntocT(shunzi_da + 4):
                                        zdun += s[k3 - 1]
                                        zdun += s[k3]
                                        s = s.replace(s[k3 - 1] + s[k3], '', 1)
                                        k3 = k3 - 2
                                        y5 += 1
                                k3 += 1
                        elif a5 == 0:
                            a6 = find_santiao()
                            if a6 >= 1:  # 后墩中墩好了
                                k4 = 0
                                while 1:
                                    if k4 > len(s)-1:
                                        break
                                    if s[k4] == ntocT(santiao_da):
                                        zdun += s[k4 - 1]
                                        zdun += s[k4]
                                        s = s.replace(s[k4 - 1] + s[k4], '', 1)
                                        k4 = k4 - 2
                                    k4 += 1
                                zdun += s[0]
                                zdun += s[1]
                                zdun += s[2]
                                zdun += s[3]
                                s = s.replace(s[0] + s[1] + s[2] + s[3], '', 1)
                            elif a6 == 0:
                                chuli_sanpai()
                    elif a4 == 0:
                        a5 = find_shunzi()
                        if a5 == 2:  # 后墩中墩好了
                            k3 = 0
                            while 1:
                                if k3 > len(s)-1:
                                    break
                                if s[k3] == ntocT(shunzi_da):
                                    hdun += s[k3-1]
                                    hdun += s[k3]
                                    s = s.replace(s[k3-1] + s[k3], '', 1)
                                    k3 = k3 - 2
                                if s[k3] == ntocT(shunzi_da+1):
                                    hdun += s[k3-1]
                                    hdun += s[k3]
                                    s = s.replace(s[k3-1] + s[k3], '', 1)
                                    k3 = k3 - 2
                                if s[k3] == ntocT(shunzi_da+2):
                                    hdun += s[k3-1]
                                    hdun += s[k3]
                                    s = s.replace(s[k3-1] + s[k3], '', 1)
                                    k3 = k3 - 2
                                if s[k3] == ntocT(shunzi_da+3):
                                    hdun += s[k3-1]
                                    hdun += s[k3]
                                    s = s.replace(s[k3-1] + s[k3], '', 1)
                                    k3 = k3 - 2
                                if s[k3] == ntocT(shunzi_da+4):
                                    hdun += s[k3-1]
                                    hdun += s[k3]
                                    s = s.replace(s[k3-1] + s[k3], '', 1)
                                    k3 = k3 - 2
                                k3 += 1
                            k3 = 0
                            while 1:
                                if k3 > len(s)-1:
                                    break
                                if s[k3] == ntocT(shunzi_xiao):
                                    zdun += s[k3-1]
                                    zdun += s[k3]
                                    s = s.replace(s[k3-1] + s[k3], '', 1)
                                    k3 = k3 - 2
                                if s[k3] == ntocT(shunzi_xiao+1):
                                    zdun += s[k3-1]
                                    zdun += s[k3]
                                    s = s.replace(s[k3-1] + s[k3], '', 1)
                                    k3 = k3 - 2
                                if s[k3] == ntocT(shunzi_xiao+2):
                                    zdun += s[k3-1]
                                    zdun += s[k3]
                                    s = s.replace(s[k3-1] + s[k3], '', 1)
                                    k3 = k3 - 2
                                if s[k3] == ntocT(shunzi_xiao+3):
                                    zdun += s[k3-1]
                                    zdun += s[k3]
                                    s = s.replace(s[k3-1] + s[k3], '', 1)
                                    k3 = k3 - 2
                                if s[k3] == ntocT(shunzi_xiao+4):
                                    zdun += s[k3-1]
                                    zdun += s[k3]
                                    s = s.replace(s[k3-1] + s[k3], '', 1)
                                    k3 = k3 - 2
                                k3 += 1
                        elif a5 == 1:  # 后墩好了
                            k3 = 0
                            y1 = 0
                            y2 = 0
                            y3 = 0
                            y4 = 0
                            y5 = 0
                            while 1:
                                if k3 > len(s)-1:
                                    break
                                if y1 <1:
                                    if s[k3] == ntocT(shunzi_da):
                                        hdun += s[k3 - 1]
                                        hdun += s[k3]
                                        s = s.replace(s[k3 - 1] + s[k3], '', 1)
                                        k3 = k3 - 2
                                        y1 += 1
                                if y2 < 1:
                                    if s[k3] == ntocT(shunzi_da + 1):
                                        hdun += s[k3 - 1]
                                        hdun += s[k3]
                                        s = s.replace(s[k3 - 1] + s[k3], '', 1)
                                        k3 = k3 - 2
                                        y2 += 1
                                if y3 < 1:
                                    if s[k3] == ntocT(shunzi_da + 2):
                                        hdun += s[k3 - 1]
                                        hdun += s[k3]
                                        s = s.replace(s[k3 - 1] + s[k3], '', 1)
                                        k3 = k3 - 2
                                        y3 += 1
                                if y4 < 1:
                                    if s[k3] == ntocT(shunzi_da + 3):
                                        hdun += s[k3 - 1]
                                        hdun += s[k3]
                                        s = s.replace(s[k3 - 1] + s[k3], '', 1)
                                        k3 = k3 - 2
                                        y4 += 1
                                if y5 < 1:
                                    if s[k3] == ntocT(shunzi_da + 4):
                                        hdun += s[k3 - 1]
                                        hdun += s[k3]
                                        s = s.replace(s[k3 - 1] + s[k3], '', 1)
                                        k3 = k3 - 2
                                        y5 += 1
                                k3 += 1
                            a6 = find_santiao()
                            if a6 >= 1:  # 后墩中墩好了
                                k4 = 0
                                while 1:
                                    if k4 > len(s)-1:
                                        break
                                    if s[k4] == ntocT(santiao_da):
                                        zdun += s[k4 - 1]
                                        zdun += s[k4]
                                        s = s.replace(s[k4 - 1] + s[k4], '', 1)
                                        k4 = k4 - 2
                                    k4 += 1
                                zdun += s[0]
                                zdun += s[1]
                                zdun += s[2]
                                zdun += s[3]
                                s = s.replace(s[0] + s[1] + s[2] + s[3], '', 1)
                            elif a6 == 0:
                                chuli_sanpai()
                        elif a5 == 0:
                            a6 = find_santiao()
                            if a6 == 2:  # 后墩中墩好了
                                k4 = 0
                                while 1:
                                    if k4 > len(s)-1:
                                        break
                                    if s[k4] == ntocT(santiao_da):
                                        hdun += s[k4-1]
                                        hdun += s[k4]
                                        s = s.replace(s[k4 - 1] + s[k4], '', 1)
                                        k4 = k4 - 2
                                    k4 += 1
                                hdun += s[0]
                                hdun += s[1]
                                hdun += s[2]
                                hdun += s[3]
                                s = s.replace(s[0] + s[1] + s[2] + s[3], '', 1)
                                k4 = 0
                                while 1:
                                    if k4 > len(s)-1:
                                        break
                                    if s[k4] == ntocT(santiao_xiao):
                                        zdun += s[k4-1]
                                        zdun += s[k4]
                                        s = s.replace(s[k4 - 1] + s[k4], '', 1)
                                        k4 = k4 - 2
                                    k4 += 1
                                zdun += s[0]
                                zdun += s[1]
                                zdun += s[2]
                                zdun += s[3]
                                s = s.replace(s[0] + s[1] + s[2] + s[3], '', 1)
                            elif a6 == 1:
                                k4 = 0
                                while 1:
                                    if k4 > len(s) - 1:
                                        break
                                    if s[k4] == ntocT(santiao_da):
                                        hdun += s[k4 - 1]
                                        hdun += s[k4]
                                        s = s.replace(s[k4 - 1] + s[k4], '', 1)
                                        k4 = k4 - 2
                                    k4 += 1
                                hdun += s[0]
                                hdun += s[1]
                                hdun += s[2]
                                hdun += s[3]
                                s = s.replace(s[0] + s[1] + s[2] + s[3], '', 1)
                                chuli_sanpai()
                            elif a6 == 0:
                                chuli_sanpai()
        if qdun:
            for i in list(range(0,len(qdun)-1,1)):
                if qdun[i] == '1' and qdun[i+1] != '0':
                    qdun = qdun.replace('1','A')
                if qdun[i] == 'T':
                    qdun = qdun.replace('T', '10')
            for i in list(range(0, len(zdun) - 1, 1)):
                if zdun[i] == '1' and zdun[i + 1] != '0':
                    zdun = zdun.replace('1', 'A')
                if zdun[i] == 'T':
                    zdun = zdun.replace('T', '10')
            for i in list(range(0, len(hdun) - 1, 1)):
                if hdun[i] == '1' and hdun[i + 1] != '0':
                    hdun = hdun.replace('1', 'A')
                if hdun[i] == 'T':
                    hdun = hdun.replace('T', '10')
        else:
            qdun = s
            for i in list(range(0,len(qdun)-1,1)):
                if qdun[i] == '1' and qdun[i+1] != '0':
                    qdun = qdun.replace('1','A')
                if qdun[i] == 'T':
                    qdun = qdun.replace('T', '10')
            for i in list(range(0, len(zdun) - 1, 1)):
                if zdun[i] == '1' and zdun[i + 1] != '0':
                    zdun = zdun.replace('1', 'A')
                if zdun[i] == 'T':
                    zdun = zdun.replace('T', '10')
            for i in list(range(0, len(hdun) - 1, 1)):
                if hdun[i] == '1' and hdun[i + 1] != '0':
                    hdun = hdun.replace('1', 'A')
                if hdun[i] == 'T':
                    hdun = hdun.replace('T', '10')
        qdun = qdun.replace("10", "T")
        zdun = zdun.replace("10", "T")
        hdun = hdun.replace("10", "T")

        qdun = qdun[0] + qdun[1] + " " + qdun[2] + qdun[3] + " " + qdun[4] + qdun[5]
        zdun = zdun[0] + zdun[1] + " " + zdun[2] + zdun[3] + " " + zdun[4] + zdun[5] + " " + zdun[6] + zdun[7] + " " + zdun[8] + zdun[9]
        hdun = hdun[0] + hdun[1] + " " + hdun[2] + hdun[3] + " " + hdun[4] + hdun[5] + " " + hdun[6] + hdun[7] + " " + hdun[8] + hdun[9]

        qdun = qdun.replace("T", "10")
        zdun = zdun.replace("T", "10")
        hdun = hdun.replace("T", "10")
        ans = []
        ans.append(qdun)
        ans.append(zdun)
        ans.append(hdun)
    AI()
    return(ans)
