import pytest
import httpx

from playwright.sync_api import Page, expect


# Set up a fixture for the API client to be used in tests
@pytest.fixture(scope="session")
def api_client():
    with httpx.Client(base_url="https://crc-website-visit-counter-ayavekgjaggfcvha.australiaeast-01.azurewebsites.net") as client:
        yield client


# Test to check if the API returns the current visit count
def test_api_returns_visits(api_client):
    # Get current visit count from the API
    new_request = api_client.get("/api/get_visits")
    assert new_request.status_code == 200

    # confirm the visitor count is returned as an integer
    assert isinstance(new_request.json()['count'], int) 


# Test to check if the API increments the visit count correctly
def test_api_increments_visits(api_client):
    # Get the initial count of visits
    initial_request = api_client.get("/api/get_visits")
    initial_count = initial_request.json()['count']

    # Increment the visit count by making a POST request to the API
    increment_request = api_client.post("/api/visits")
    assert increment_request.status_code == 200

    # Verify that the visit count has incremented by 1
    assert increment_request.json()['count'] == initial_count + 1


# Test to check if the visit count on the website increments (after a page reload)
def test_site_visit_count_increment(page: Page):
    # Go to the website and check the initial visit count
    page.goto("https://resume.voyous.dev/")
    visitor_count = page.locator("#visit-count")
    expect(visitor_count).to_be_visible()

    initial_count_text = int(visitor_count.inner_text())

    # Reload the page and check if the visit count has incremented by 1
    page.reload()
    expect(visitor_count).to_have_text(str(initial_count_text + 1))
