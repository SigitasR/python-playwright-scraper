from playwright.async_api import Page


class Pagination:
    def __init__(self, page: Page):
        self.page = page
        self.pagination_container = page.locator('div.b-pagination-wrapper--desktop-top ul.pagination')

    async def click_next(self) -> None:
        await self.page.wait_for_load_state('networkidle')
        await self.pagination_container.locator('text="»"').click()

    async def is_first_page(self) -> bool:
        await self.page.wait_for_load_state('networkidle')
        first_pagination_item = self.pagination_container.locator('li').nth(1)
        return first_pagination_item.get_attribute('class') == 'active'

    async def is_last_page(self) -> bool:
        await self.page.wait_for_load_state('domcontentloaded')
        navigation_item_count: int = await self.pagination_container.locator('li').count()
        last_pagination_item = self.pagination_container.locator('li').nth(navigation_item_count - 2)
        return await last_pagination_item.get_attribute('class') == 'active'
