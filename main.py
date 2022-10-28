import asyncio
from time import perf_counter

from playwright.async_api import async_playwright

from src.page_objects.CategoryPage import CategoryPage
from src.util.browser_util import create_page, browse_products

if __name__ == '__main__':
    async def main() -> None:
        async with async_playwright() as pw:
            time_before = perf_counter()
            browser = await pw.chromium.launch(headless=False)
            page = await create_page(browser)
            await page.goto("/gerimai/stiprieji-alkoholiniai-gerimai/")

            category = CategoryPage(page)
            links = await category.go_trough_all_pages()
            await page.context.close()

            number_of_links_per_browser = 20
            splits = [links[i:i + number_of_links_per_browser] for i in
                      range(0, len(links), number_of_links_per_browser)]

            result = await asyncio.gather(*[browse_products(browser, split) for split in splits])
            result = [item for sublist in result for item in sublist]

            print(result)
            print(len(result))

            print(f'Total time: {perf_counter() - time_before}')

            await browser.close()


    asyncio.run(main())
