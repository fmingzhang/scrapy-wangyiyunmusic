import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from music.items import MusicItem

class PopmusicSpider(CrawlSpider):
    name = 'popmusic'
    allowed_domains = ['music.163.com']
    start_urls = ['https://music.163.com/discover/playlist/?cat=%E6%B5%81%E8%A1%8C']
    #网易云音乐url应该去掉#号
    rules = (
        #?应该加上转义字符,\d表示数字，+表示许多个
        Rule(LinkExtractor(allow=r'playlist\?id=\d+'), callback='parse_item'),
        Rule(LinkExtractor(restrict_xpaths='//*[@id="m-pl-pager"]/div/a'), follow=False),
    )
    #follow=true 表示翻页，follow=false 表示不翻页当前页
    #根据网站结构确定是否需要多个rule
    #第二个rule只是翻页不需要处理，无需callback，第一个rule只需要解析当前页无需翻页


    def parse_item(self, response):
        #print('=============')
        name=response.xpath('//*[@class="m-info f-cb"]/div[2]/div/div[1]/div/h2/text()').extract_first()
        ct=response.xpath('//*[@class="m-info f-cb"]/div[2]/div/div[2]/span[2]/text()').extract_first()
        createTime=ct.rstrip('\xa0创建')#去掉右侧字符串
        tag=response.xpath('//*[@class="m-info f-cb"]/div[2]/div/div[4]/a/i/text()').extract_first()
        intro=response.xpath('//*[@id="album-desc-more"]/text()').extract_first()
        introduce = intro.lstrip('\n')
        cov=response.xpath('//*[@class="m-info f-cb"]/div[1]/img/@src').extract_first()
        cover=cov.rstrip('?param=200y200')
        sheet=MusicItem(name=name,createTime=createTime,tag=tag,introduce=introduce,cover=cover)
        yield sheet



