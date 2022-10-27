import asyncio

from playwright.async_api import async_playwright

from CategoryPage import CategoryPage


async def browse_products(urls: [str]):
    async with async_playwright() as pw:
        browser = await pw.chromium.launch(headless=False)
        page = await browser.new_page(base_url="https://barbora.lt")
        await page.context.add_cookies([
            {'url': 'https://barbora.lt', 'name': 'ageLimitationWarning', 'value': '20'},
            {'url': 'https://barbora.lt', 'name': 'CookieConsent', 'value': 'reeee'},
        ])

        for url in urls:
            await page.goto(url)
            print(await page.title())

        await browser.close()


async def main():
    async with async_playwright() as pw:
        browser = await pw.chromium.launch(headless=False)
        page = await browser.new_page(base_url="https://barbora.lt")
        await page.context.add_cookies([
            {'url': 'https://barbora.lt', 'name': 'ageLimitationWarning', 'value': '20'},
            {'url': 'https://barbora.lt', 'name': 'CookieConsent', 'value': 'reeee'},
        ])
        await page.goto("/gerimai/stiprieji-alkoholiniai-gerimai/")

        category = CategoryPage(page)
        links = await category.go_trough_all_pages()

        number_of_links = 15
        splits = [links[i:i + number_of_links] for i in range(0, len(links), number_of_links)]

        print(len(splits))

        await asyncio.gather(*[browse_products(split) for split in splits])

        await browser.close()


asyncio.run(main())
