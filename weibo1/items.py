# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class UserInfo(Item):
    # define the fields for your item here like:
    # name = Field()
    __slots__ = 'uid'

    uid = Field()
    nickname =Field()
    fan_num = Field()
    follow_num = Field()
    weibo_num = Field()
    level = Field()
    location = Field()
    sex = Field()
    birth = Field()
    blog = Field()
    domain = Field()
    intro = Field()
    email = Field()
    QQ = Field()
    University = Field()
    Tags = Field()
    interests = Field()

