import scrapy
from ..items import laptops

class Flipspyder(scrapy.Spider):
 name = 'Flipcraw'
 page =2
 n= int(input())
 i=1
 start_urls = [
     'https://www.flipkart.com/laptops/pr?sid=6bo%2Cb5g&marketplace=FLIPKART&page=2'
 ]
 def parse(self, response):

     items = laptops()

     all_div = response.css('div._1UoZlX')

     for divis in all_div:
         if Flipspyder.i <= Flipspyder.n:

            title = divis.css('._3wU53n::text').extract()
            price = divis.css('._2rQ-NK::text').extract()
            rating = divis.css('.hGSR34::text').extract()

            items['title']= title
            items['price']= price
            items['rating'] = rating
            yield items
            Flipspyder.i +=1

    nextp='https://www.flipkart.com/laptops/pr?sid=6bo%2Cb5g&marketplace=FLIPKART&page=' +str(Flipspyder.page)

    if Flipspyder.i <= Flipspyder.n:
        Flipspyder.page +=1
        yield response.follow(nextp, callback = self.parse)
