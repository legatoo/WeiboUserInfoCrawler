# encoding: utf-8

__author__ = 'steven'

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector
from scrapy.http import Request, FormRequest
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor as sle
from cookies import returnCookie, weibo_accounts
from weibo1.auxFunctions import generateHTML
from weibo1.elementSetting import QUERY_INFO, QUERY_FANS, QUERY_FOLLOWERS
from pyquery import PyQuery as pq
from weibo1.parser import InfoParser
import random
import re
import codecs

from weibo1.items import UserInfo


class WeiboUserInfo(CrawlSpider):

    name = "weibo_user"
    allowed_domains = ["weibo.com"]
    current_cookie = None

    start_urls = [
        "http://weibo.com/mclybosc"
    ]

    count = 0


    def start_requests(self):
        self.current_cookie = returnCookie(random.choice(weibo_accounts.keys()))

        yield Request(self.start_urls[0],
            cookies= self.current_cookie,
            callback=self.parse
        )

    def parse(self, response):
        #this function will locate the follower page
        html = generateHTML(response.body, QUERY_FANS)
        doc = pq(html)
        baseURL = "http://weibo.com"

        connect_follow = doc.find('ul.user_atten li.follower a')
        for a in connect_follow:
            url = baseURL+ a.attrib['href'].split('?')[0]
            #print "URL to my followers page--> ", url
            yield Request(url,
                cookies= self.current_cookie,
                callback=self.parseFollower
            )

        connect_info = doc.find('ul.pftb_ul li.pftb_itm a')
        for a in connect_info:
            b = pq(a)
            if b.text() == u'个人资料':
                url = baseURL + a.attrib['href'].split('?')[0]
                #print "URL to my info page",url
                yield Request(url, cookies= self.current_cookie, callback=self.parseInfo)

    def parseFollower(self, response):
        html = generateHTML(response.body, QUERY_FOLLOWERS)
        if len(html) == 0:
            return
        doc = pq(html)
        baseURL = "http://weibo.com"
        connect = doc.find('ul.cnfList div.face a')
        if connect:
            for a in connect:
                infoURL = baseURL + a.attrib['href']
                #print "New user page -> ",infoURL

                yield Request(infoURL,
                    cookies= self.current_cookie,
                    callback=self.parse
                )


    def parseInfo(self,response):
        m = re.search("\$CONFIG\['oid'\]='(\d+)'", response.body)
        uid = m.group(1)
        html = generateHTML(response.body, QUERY_INFO)
        iParser = InfoParser(html, uid)


        if iParser.process():
            info = iParser.returnDict
            return self.fillItem(info)

        print "something wrong"

        return None


    def fillItem(self, infoDict):
        self.count += 1
        item = UserInfo()
        item['nickname'] = infoDict['nickname']
        item['sex'] = infoDict['sex']
        item['birth'] = infoDict['birth']
        item['location'] = infoDict['location']
        item['email'] = infoDict['email']
        item['blog'] = infoDict['blog']
        item['domain'] = infoDict['domain']
        item['fan_num'] = infoDict['n_fans']
        item['weibo_num'] = infoDict['n_weibos']
        item['follow_num'] = infoDict['n_follows']
        item['interests'] = infoDict['interests']
        item['level'] = infoDict['level']
        item['University'] = infoDict['university']
        item['Tags'] = infoDict['tag']
        item['intro'] = infoDict['intro']
        item['QQ'] = infoDict['QQ']
        item['uid'] = infoDict['uid']

        if self.count == 300:
            self.current_cookie = returnCookie(random.choice(weibo_accounts.keys()))
            self.count = 0

        #print '\n'.join(['%s : %s' %(k.encode('utf-8'),v.encode('utf-8')) for k,v in infoDict.iteritems()])
        #print '-----------------------------'

        return item



