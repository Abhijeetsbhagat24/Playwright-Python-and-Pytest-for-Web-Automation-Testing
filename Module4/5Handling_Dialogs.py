#this method is not used much

from playwright.sync_api import Playwright, sync_playwright

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False, slow_mo = 1000)
    page = browser.new_page()
    page.goto("https://testpages.herokuapp.com/styled/alerts/alert-test.html")


    alert_btn = page.get_by_text("Show alert box")
    alert_btn.click()

    browser.close()
