# install using pip install firecrawl-py
import asyncio
from firecrawl import AsyncFirecrawlApp

async def main():
    app = AsyncFirecrawlApp(api_key='FIRECRAWL_API_KEY')
    response = await app.scrape_url(
        url='your_url_here',
        formats= [ 'markdown' ],
        only_main_content= True,
        parse_pdf= True,
        max_age= 14400000
    )
    print(response.markdown) # get only markdown


asyncio.run(main())


