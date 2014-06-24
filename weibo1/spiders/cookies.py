__author__ = 'steven'

import os
import re
from loginModule import login


#zombi accounts to login
weibo_accounts = {
    'w82z2zlsuu8' : '538ofb1mV',
    'iogg1n3c0mn0vb' : '1G1s87r5P',
    'a09czwkl48l' : '7O3ZmWr7K',
    'qxmoxox1' : '225N4l3kB',
    'bc4w200pg' : 'disT4IIQ0',
    'd4pie4cjbbqz1490q5' : '4u66W7YP1',
    'gbf6josovv7' : '69CRp8d48',
    'iin6if21pkbpdie8mn' : 'd0xv7aT51',
    'ccylmsfs1bh35tmsm' : '44GG0V3T4',
    'cq0q8ozvhtvruv86jw' : 'Wwc3nBXMs',
    'd52tf4v7' : 'PPti1I6cV',
    'fci2u71d50zh' : '6183sXeuC',
    'feq6alhtib1' : 'fwY44VMu0',
    'fkvna1oz9597wad' : '9KFb5VQtH',
    'fmwqwml4f' : 'zHR35csjP',
    'ghjfm6qb2f1ky' : 'RMU11Sxk5',
    'gqr39nrqbeljovho' : '4i3omf9kK',
    'birv4xnsd2fdrh1yy0' : 'VMULo794l',
    'tvyg62ee3' : 'hCm48i5qD',
    'a7kpamju' : 'Y5mVJLN30'

}


def returnCookie(cookie_file):
    if not os.path.exists(cookie_file):
        login(cookie_file+'@163.com', weibo_accounts[cookie_file], cookie_file)

    return generateCookieJar(cookie_file)

def generateCookieJar(cookie_file):
    cookies = []
    with open(cookie_file, 'r') as cookieJar:
        for cookie_line in cookieJar:
            if 'weibo.com' in cookie_line:
                cookies.append( process_cookie(cookie_line))
    return cookies

def process_cookie(cookie_line):
    #print 'original cookie ---> ', cookie_line
    cookie = {}
    cookie_remove_header = re.sub('^Set-Cookie3: ', '', cookie_line).strip()
    #print 'after remove header ---> ', cookie_remove_header
    cookie_element=cookie_remove_header.split('; ')

    name, value = cookie_element[0].split('=')
    cookie['name'] = name.strip("\"")
    cookie['value'] = value.strip("\"")
    cookie['path'] = cookie_element[1].split('=')[1].strip("\"")
    cookie['domain'] = cookie_element[2].split('=')[1].strip("\"")

    #print cookie
    return cookie
