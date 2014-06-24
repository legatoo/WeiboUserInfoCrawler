# encoding: utf-8
__author__ = 'steven'

from pyquery import PyQuery as pq
from weibo1.elementSetting import INFO_KEY
from weibo1.elementSetting import profile_map

class InfoParser(object):
    def __init__(self, html, uid):
        self.doc = pq(html)
        self.info = dict.fromkeys(INFO_KEY,u'')
        self.info['uid'] = uid


    #This part will get basic information
    #if you are friend, you will get more
    def getBasicInfo(self):
        connect = self.doc.find('div.pf_item')
        for item in connect:
            item = pq(item)
            key = item.children('div.label').text().strip()
            value = item.children('div.con').text().strip()
            if key in profile_map:
                try:
                    value = value.replace(',', u'，').replace(';', u'；')
                    self.info[profile_map[key]] = value
                except:
                    return False
        return True

    #This part will give you number of fans, weibos, and followers
    def getWeiboInfo(self):
        connect = self.doc.find('ul.user_atten li a strong')
        for a in connect:
            a = pq(a)
            if a.attr('node-type').lower() == 'follow':
                self.info['n_follows'] = a.text().strip()
            elif a.attr('node-type').lower() == 'fans':
                self.info['n_fans'] = a.text().strip()
            elif a.attr('node-type').lower() == 'weibo':
                self.info['n_weibos'] = a.text().strip()
        return True

    #This part will get the weibo level and daren interests
    def getDarenInfo(self):
        query = 'div.prm_app_pinfo div.info_block'
        pprofile_infoGrow = self.doc.find(query)

        self.info['interests'] = ''
        for infoblk in pprofile_infoGrow:
            infoblk = pq(infoblk)
            pinfo_title = infoblk.children('form.pinfo_title').text().strip()

            if u'达人信息' == pinfo_title:
                daren_info = infoblk.children('div.if_verified p.iv_vinfo a')
                try:
                    for a in daren_info:
                        a = pq(a)
                        if a.attr('href').endswith('&loc=darenint'):
                            self.info['interests'] += '-' + a.text().strip()

                    self.info['interests'] = self.info['interests'].strip()
                except:
                    return False

            elif u'等级信息' == pinfo_title:
                level = infoblk.children('div.if_level p.level_info span.info')
                for l in level:
                    l = pq(l)
                    try:
                        t = l.text().strip().split(u'：')
                        if u'当前等级' == t[0].strip():
                                self.info['level'] = t[1].strip()

                    except:
                        return False
        return True


    def process(self):
        return self.getBasicInfo() and self.getWeiboInfo() and self.getDarenInfo()

    @property
    def returnDict(self):
        return  self.info

