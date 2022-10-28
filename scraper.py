import asyncio
from time import perf_counter

from playwright.async_api import async_playwright, Page, Browser

from src.page_objects.CategoryPage import CategoryPage


async def create_page(browser: Browser) -> Page:
    context = await browser.new_context(base_url="https://barbora.lt")
    page = await context.new_page()
    await page.context.add_cookies([
        {'url': 'https://barbora.lt', 'name': 'ageLimitationWarning', 'value': '20'},
        {'url': 'https://barbora.lt', 'name': 'CookieConsent', 'value': 'reeee'},
    ])

    return page


async def browse_products(browser: Browser, urls: [str]):
    async with async_playwright() as pw:
        page = await create_page(browser)
        products: [str] = []
        for url in urls:
            await page.goto(url)
            products.append(await page.title())
        return products


if __name__ == '__main__':
    async def main() -> None:
        async with async_playwright() as pw:
            time_before = perf_counter()
            browser = await pw.chromium.launch(headless=False)
            page = await create_page(browser)
            await page.goto("/gerimai/stiprieji-alkoholiniai-gerimai/")

            category = CategoryPage(page)
            links = await category.go_trough_all_pages()

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
