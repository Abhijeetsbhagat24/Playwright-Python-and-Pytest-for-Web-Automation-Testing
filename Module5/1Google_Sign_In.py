from playwright.sync_api import Playwright, sync_playwright

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False, slow_mo = 500, args = ["--disable-dev-shm-Usage", "--disable-blink-features = AutomationControlled"]) #if we try with google it may show error
    page = browser.new_page()
    page.set_viewport_size({"width" : 922, "height": 950 }) # to set page width and height

    page.goto("https://accounts.google.com")


    email_input = page.get_by_label("Email or Phone")
    email_input.fill("")
    next_btn = page.get_by_role("button", name = "Next")
    next_btn.click()

    password_input = page.get_by_label("Enter your password")
    password_input.fill("")
    next_btn.click()

    browser.close()
