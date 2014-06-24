# Scrapy settings for weibo1 project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'weibo1'

SPIDER_MODULES = ['weibo1.spiders']
NEWSPIDER_MODULE = 'weibo1.spiders'

RETRY_ENABLED = False
COOKIES_ENABLED = True
MYEXT_ENABLED = True
MYEXT_ITEMCOUNT = 100

EXTENSIONS = {
    'weibo1.itemNumberControl.StopAfterNum': 500
}

ITEM_PIPELINES = ['weibo1.pipelines.WeiboUserInfoPipeline']

MONGODB_SERVER = "localhost"
MONGODB_PORT = 27017
MONGODB_DB = "weibo"
MONGODB_COLLECTION = "user_info1"
#MONGODB_UNIQUE_KEY = 'uid'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'weibo1 (+http://www.yourdomain.com)'
