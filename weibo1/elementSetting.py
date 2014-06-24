# encoding: utf-8
__author__ = 'steven'

#This prefix will match the personal information part
QUERY_INFO    = (
        ('<script>FM.view({"ns":"pl.header.head.index","domid":"Pl_Official_Header__1"'),
        ('<script>FM.view({"ns":"","domid":"Pl_Official_LeftInfo__28"'),
        ('<script>FM.view({"ns":"","domid":"Pl_Official_RightGrow__29"')
)

QUERY_FANS    = (
    ('<script>FM.view({"ns":"pl.header.head.index","domid":"Pl_Official_Header__1"'),
    ('<script>FM.view({"ns":"pl.nav.index","domid":"Pl_Core_Nav__2"')
    )

QUERY_FOLLOWERS  = ('<script>FM.view({"ns":"pl.content.followTab.index","domid":"Pl_Official_LeftHisRelation__31"')


TO_INFO_PAGE = ('<script>FM.view({"ns":"pl.nav.index","domid":"Pl_Core_Nav__2"')

INFO_KEY = [
    'uid', 'nickname', 'location', 'sex', 'birth', 'blog', 'domain', 'intro',
    'email', 'QQ', 'university', 'company', 'tag', 'n_follows',
    'n_fans', 'n_weibos', 'interests', 'level'
]

profile_map= {
    u'昵称': 'nickname',
    u'所在地':'location',
    u'性别':'sex',
    u'生日':'birth',
    u'博客':'blog',
    u'个性域名':'domain',
    u'简介':'intro',
    u'邮箱':'email',
    u'QQ':'QQ',
    u'大学':'university',
    u'公司':'company',
    u'标签':'tag'
}
