from playwright.sync_api import expect

from components.base_component import BaseComponent


class RegistrationFormComponent(BaseComponent):
    def __init__(self, page):
        super().__init__(page)

        self.email_input_field = page.get_by_test_id('registration-form-email-input').locator('input')
        self.username_input_field = page.get_by_test_id('registration-form-username-input').locator('input')
        self.password_input_field = page.get_by_test_id('registration-form-password-input').locator('input')

    def fill(self, email: str, username: str, password: str):
        self.email_input_field.fill(email)
        self.username_input_field.fill(username)
        self.password_input_field.fill(password)

    def check_visible(self, email: str, username: str, password: str):
        expect(self.email_input_field).to_be_visible()
        expect(self.email_input_field).to_have_value(email)

        expect(self.username_input_field).to_be_visible()
        expect(self.username_input_field).to_have_value(username)

        expect(self.password_input_field).to_be_visible()
        expect(self.password_input_field).to_have_value(password)
