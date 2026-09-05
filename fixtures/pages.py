import pytest
from playwright.async_api import Page

from pages.authentication.login_page import LoginPage
from pages.authentication.registration_page import RegistrationPage
from pages.dashboard.dashboard_page import DashboardPage
from pages.courses.courses_list_page import CoursesListPage
from pages.courses.create_course_page import CreateCoursePage


@pytest.fixture
def login_page(page) -> LoginPage:
    return LoginPage(page=page)


@pytest.fixture
def registration_page(page) -> RegistrationPage:
    return RegistrationPage(page=page)


@pytest.fixture
def dashboard_page(page) -> DashboardPage:
    return DashboardPage(page=page)


@pytest.fixture
def dashboard_page_with_state(page_with_state) -> DashboardPage:
    return DashboardPage(page=page_with_state)


@pytest.fixture()
def courses_list_page(page_with_state) -> CoursesListPage:
    return CoursesListPage(page=page_with_state)


@pytest.fixture
def create_course_page(page_with_state) -> CreateCoursePage:
    return CreateCoursePage(page=page_with_state)