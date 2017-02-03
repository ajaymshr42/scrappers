import scrapy


class QuotesSpider(scrapy.Spider):
    name = "fetchflight"

    def start_requests(self):
        urls = [
            'https://en.wikipedia.org/wiki/List_of_airports_in_India'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        data=[]
        cities=response.xpath('//*[@id="mw-content-text"]/table/tr/td[1]/a/text()').extract()
        types=response.xpath('//*[@id="mw-content-text"]/table/tr/td[5]/text()').extract()
        names=response.xpath('//*[@id="mw-content-text"]/table/tr/td[2]/text()').extract()
        for city,name,tp in zip(cities,names,types):
            dp={}
            dp['name']=name
            dp['city']=str(city)
            dp['type']='domestic'
            print dp
            data.append(dp)
        print len(data)