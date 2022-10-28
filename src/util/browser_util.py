from playwright.async_api import Browser, Page

from src.page_objects.ProductPage import ProductPage


async def create_page(browser: Browser) -> Page:
    context = await browser.new_context(base_url="https://barbora.lt")
    page = await context.new_page()
    await page.context.add_cookies([
        {'url': 'https://barbora.lt', 'name': 'ageLimitationWarning', 'value': '20'},
        {'url': 'https://barbora.lt', 'name': 'CookieConsent', 'value': 'reeee'},
    ])

    return page


async def browse_products(browser: Browser, urls: [str]):
    page = await create_page(browser)
    products: [str] = []
    for url in urls:
        await page.goto(url)
        product_page = ProductPage(page)
        products.append(await product_page.get_product_data())
    await page.context.close()
    return products
