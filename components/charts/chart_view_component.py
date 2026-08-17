from playwright.sync_api import Page, expect

from components.base_component import BaseComponent
from elements.text import Text


class ChartViewComponent(BaseComponent):
    def __init__(self, page: Page, identifier: str, chart_type: str):
        super().__init__(page)

        self.title = Text(page, f'{identifier}-widget-title-text', 'Chart title')
        self.chart = page.get_by_test_id(f'{identifier}-{chart_type}-chart')

    def check_visible(self, title: str):
        self.title.check_have_text(title)
        expect(self.chart).to_be_visible()
