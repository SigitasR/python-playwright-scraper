from playwright.async_api import Page

from src.dataclasses.ProductData import ProductData


class ProductPage:
    def __init__(self, page: Page):
        self.page = page
        self.product_title = self.page.locator('h1[itemprop="name"]')
        self.product_price = self.page.locator('div.b-product-info--price-and-quantity span[itemprop="price"]')
        self.out_of_stock_badge = self.page.locator('a.b-product-out-of-stock')

    async def get_product_data(self) -> ProductData:
        return ProductData(title=(await self.product_title.text_content()).strip(),
                           price=(await self.product_price.text_content()).strip(),
                           in_stock=not await self.out_of_stock_badge.is_visible())
