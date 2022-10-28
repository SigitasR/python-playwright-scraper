import asyncio
from time import perf_counter

from playwright.async_api import async_playwright

from src.util.batch_util import split_product_links_into_batches
from src.util.browser_util import collect_product_links, collect_product_data
from src.util.csv_util import write_to_file

if __name__ == '__main__':
    async def main() -> None:
        async with async_playwright() as pw:
            time_before = perf_counter()
            browser = await pw.chromium.launch(headless=True)

            links = await collect_product_links(browser, '/gerimai/stiprieji-alkoholiniai-gerimai/')
            link_batches = split_product_links_into_batches(links, 10)
            result = await collect_product_data(browser, link_batches)

            print(len(result))
            write_to_file(result)
            print(f'Total time: {perf_counter() - time_before}')

            await browser.close()


    asyncio.run(main())
