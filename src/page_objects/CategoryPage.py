from playwright.async_api import Page

from src.page_objects.Pagination import Pagination


class CategoryPage:
    def __init__(self, page: Page):
        self.page = page
        self.products_list = page.locator('div.b-products-list--wrapper')

        self.pagination = Pagination(self.page)

    async def get_page_products(self) -> [str]:
        await self.page.wait_for_load_state('networkidle')
        links: [str] = []
        await self.pagination.pagination_container.wait_for()
        product_count = await self.products_list.locator('div.b-product--wrap2.b-product--desktop-grid').count()
        print(product_count)
        for i in range(0, product_count):
            product_box = self.products_list.locator(
                'div.b-product--wrap2.b-product--desktop-grid a.b-product-title--desktop').nth(i)
            await product_box.wait_for()
            # await product_box.scroll_into_view_if_needed()
            product_href = await product_box.get_attribute('href')
            if product_href:
                links.append(product_href)
        return links

    async def go_trough_all_pages(self) -> [str]:
        links: [str] = []
        while not await self.pagination.is_last_page():
            links.extend(await self.get_page_products())
            await self.pagination.click_next()
        links.extend(await self.get_page_products())
        return links
