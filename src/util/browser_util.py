import asyncio
from typing import List

from playwright.async_api import Browser, Page

from src.dataclasses.ProductInfo import ProductInfo
from src.page_objects.CategoryPage import CategoryPage
from src.page_objects.ProductPage import ProductPage


async def create_page(browser: Browser) -> Page:
    context = await browser.new_context(base_url="https://barbora.lt")
    page = await context.new_page()
    await page.context.add_cookies([
        {'url': 'https://barbora.lt', 'name': 'ageLimitationWarning', 'value': '20'},
        {'url': 'https://barbora.lt', 'name': 'CookieConsent', 'value': 'reeee'},
    ])
    print(f'Creating new BrowserContext. Current count: {len(browser.contexts)}')

    return page


async def scrape_product(page: Page, url: str) -> ProductInfo:
    await page.goto(url)
    product_page = ProductPage(page)
    return await product_page.get_product_info()


async def scrape_product_list(browser: Browser, urls: List[str]) -> List[ProductInfo]:
    page = await create_page(browser)
    products: [ProductInfo] = []
    for url in urls:
        products.append(await scrape_product(page, url))
    await page.context.close()
    return products


async def collect_product_links(browser: Browser, category_url: str) -> List[str]:
    page = await create_page(browser)
    await page.goto(category_url)

    category = CategoryPage(page)
    links = await category.go_trough_all_pages()
    await page.context.close()
    return links


async def collect_product_data(browser: Browser, link_batches: List) -> List[ProductInfo]:
    result = await asyncio.gather(*[scrape_product_list(browser, split) for split in link_batches])
    return [item for sublist in result for item in sublist]
