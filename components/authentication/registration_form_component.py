from playwright.sync_api import expect

from components.base_component import BaseComponent
from elements.input import Input


class RegistrationFormComponent(BaseComponent):
    def __init__(self, page):
        super().__init__(page)

        self.email_input_field = Input(page, 'registration-form-email-input', 'Email')
        self.username_input_field = Input(page, 'registration-form-username-input', 'Username')
        self.password_input_field = Input(page, 'registration-form-password-input', 'Password')

    def fill(self, email: str, username: str, password: str):
        self.email_input_field.fill(email)
        self.username_input_field.fill(username)
        self.password_input_field.fill(password)

    def check_visible(self, email: str, username: str, password: str):
        self.email_input_field.check_visible()
        self.email_input_field.check_have_text(email)

        self.username_input_field.check_visible()
        self.username_input_field.check_have_text(username)

        self.password_input_field.check_visible()
        self.password_input_field.check_have_text(password)
