from playwright.sync_api import sync_playwright, expect


with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    registration_email_input_field = page.locator("//input[@id=':r0:']")
    registration_email_input_field.fill("user.name@gmail.com")

    registration_username_input_field = page.locator("//input[@id=':r1:']")
    registration_username_input_field.fill("username")

    registration_password_input_field = page.locator("//input[@id=':r2:']")
    registration_password_input_field.fill("password")

    registration_button = page.locator("//button[@data-testid='registration-page-registration-button']")
    registration_button.click()

    dashboard_title = page.get_by_test_id('dashboard-toolbar-title-text')
    dashboard_title.is_visible()
    expect(dashboard_title).to_have_text("Dashboard")












