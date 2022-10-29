import asyncio
from time import perf_counter

from playwright.async_api import async_playwright

from src.util.batch_util import split_product_links_into_batches
from src.util.browser_util import collect_product_links, collect_product_data
from src.util.commandline_util import get_commandline_parameters
from src.util.csv_util import write_to_file

if __name__ == '__main__':
    async def main() -> None:
        async with async_playwright() as pw:
            time_before = perf_counter()

            parameters = get_commandline_parameters()

            browser = await pw.chromium.launch(headless=parameters['headless'])

            links = await collect_product_links(browser, parameters['category'])
            link_batches = split_product_links_into_batches(links, parameters['batch_size'])
            result = await collect_product_data(browser, link_batches)

            print(f'Total products scraped: {len(result)}')
            write_to_file(result)

            await browser.close()
            print(f'Total time: {perf_counter() - time_before}')


    asyncio.run(main())
