import pytest
from pages.registration_page import RegistrationPage
from pages.dashboard_page import DashboardPage


@pytest.mark.regression
@pytest.mark.registration
def test_successful_registration(registration_page: RegistrationPage, dashboard_page: DashboardPage):
    email = "user.name@gmail.com"
    username = "NoName123"
    password = "password"

    registration_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')
    registration_page.registration_form.fill(email=email, username=username, password=password)
    registration_page.click_registration_button()

    dashboard_page.students_chart_view.check_visible('Students')
    dashboard_page.activities_chart_view.check_visible('Activities')
    dashboard_page.courses_chart_view.check_visible("Courses")
    dashboard_page.scores_chart_view.check_visible("Scores")

