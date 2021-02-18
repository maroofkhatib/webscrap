import scrapy


class NewsSpider(scrapy.Spider):
	name = 'news'
	start_urls = ['https://www.ndtv.com/india']

	def parse(self, response):
		for article in response.css("div.news_Itm"):
			try:
				yield {
					'title': article.css("a::text").get().replace('\"','\''),
					'text' : article.css("p.newsCont::text").get(),
					'link' : article.css("a").attrib["href"].replace('\"','\'')
				}
			except:
				pass	

		try:

			next_page = response.css("a.btnLnk.arrowBtn.next").attrib["href"]

			if next_page is not None:
				yield response.follow(next_page, callback=self.parse)

		except:
			pass			