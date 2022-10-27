import asyncio

from playwright.async_api import async_playwright


async def main():
    async with async_playwright() as pw:
        browser = await pw.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.context.add_cookies([
            {'url': 'https://barbora.lt', 'name': 'ageLimitationWarning', 'value': '20'},
            {'url': 'https://barbora.lt', 'name': 'CookieConsent', 'value': 'reeee'},
        ])
        await page.goto("https://barbora.lt/gerimai/stiprieji-alkoholiniai-gerimai")
        await browser.close()


asyncio.run(main())
