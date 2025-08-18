# install using pip install firecrawl-py
import asyncio
from firecrawl import AsyncFirecrawlApp

async def main():
    app = AsyncFirecrawlApp(api_key='fc-32d27550d70c4eddb5e0f16cfc3bda92')
    response = await app.scrape_url(
        url='https://arpitpatelsitapur.github.io/',		
        formats= [ 'markdown' ],
        only_main_content= True,
        parse_pdf= True,
        max_age= 14400000
    )
    print(response.markdown) # get only markdown


asyncio.run(main())


