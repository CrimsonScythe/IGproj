import scrapy


class IGSpider(scrapy.Spider):
    name = "ig"

    start_urls = [
        # 'https://en.wikipedia.org/wiki/Ibn_Arabi#Legacy'
        # 'https://www.instagram.com/explore/tags/food/',
        'https://www.tiktok.com/discover?lang=en'
            # 'https://www.instagram.com/explore/tags/cook/'
            # 'http://quotes.toscrape.com/page/2/',
    ]
        

    def parse(self, response):
        # value = response.xpath('//*[@id="mw-content-text"]/div/p[1]')
        # value = response.xpath('//*[@id="react-root"]/section/main/header/div[2]/div[1]/div[2]')
        # value = response.xpath('//*[@id="react-root"]/section/main/header/div[2]/div[1]/div[2]/span/text()')
        value = response.selector.xpath('//*[@id="main"]/div[2]/div[2]/div/div/div/div[2]/div[1]/div/div[1]/div[1]/div[1]/div/a[2]/div/strong[1]/text()').extract_first()
        print(value)
        # page = response.url.split("/")[-2]
        # filename = 'quotes-%s.html' % page
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        # self.log('Saved file %s' % filename)