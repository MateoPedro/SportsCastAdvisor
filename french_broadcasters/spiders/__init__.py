# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.
import scrapy

class BroadcasterSpider(scrapy.Spider):
    name = 'broadcaster'

    start_urls = ['https://www.echosdunet.net/dossiers/sports'] 

    def parse(self, response):
        for sports in response.css("div.table--swap"):
            sport = sports.css("caption::text").get()
            for row in sports.css("tr"):
                yield {
                    "sport": sport,
                    "Competition": row.css("td:first-child::text, td:first-child a::text, td:first-child strong::text").getall(),
                    "broadcaster": row.css("td:nth-child(2)::text, td:nth-child(2) a::text, td:nth-child(2) strong::text").getall()
                    
                }

                
class BroadcasterPriceSpider(scrapy.Spider):
    name = 'broadcaster_price'
    
    start_urls = ["https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&ved=2ahUKEwjUwcfozaiAAxWoVaQEHb_oDWMQFnoECBIQAw&url=https%3A%2F%2Fwww.cnetfrance.fr%2Fproduits%2Fligue-1-ligue-des-champions-sur-quelles-chaines-regarder-le-foot-et-a-quel-prix-39906357.htm%23%3A~%3Atext%3DSi%2520vous%2520voulez%2520faire%2520d%2Cmois%2520(engagement%252024%2520mois).&usg=AOvVaw35V9bw-ejJ0RmrWS-BzGKa&opi=89978449"]

    def parse(self, response):
        for row in response.css('table tbody tr'):
            yield {
            'Offer': row.css('td:nth-child(1) *::text').getall(),
            'Price': row.css('td:nth-child(3) *::text').getall(),
        }