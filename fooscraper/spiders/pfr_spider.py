from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector

class PFRSpider(BaseSpider):
  name = "pfr"
  allowed_domains = ["pro-football-reference.com"]
  start_urls = [
      "http://www.pro-football-reference.com/teams/cle/"]
  def parse(self, response):
    hxs = HtmlXPathSelector(response)
    teamIndex = hxs.select('//div[@id="div_team_index"]').extract()
    print teamIndex
