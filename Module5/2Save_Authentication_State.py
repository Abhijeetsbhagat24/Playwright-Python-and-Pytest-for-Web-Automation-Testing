from playwright.sync_api import Playwright, sync_playwright

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False, slow_mo = 500, args=["--disable-dev-shm-usage", "--disable-blink-features = AutomationControlled"]) #if we try with google it may show error

    context = browser.new_context() #it allows to store authentication state and save it when we have performed our login
    page = context.new_page()
    page.goto("https://accounts.google.com/")

    email_input = page.get_by_label("Email or phone")
    email_input.fill("")
    page.get_by_role("button", name = "Next").click()

    password_input = page.get_by_label("Enter your password")
    password_input.fill("")
    page.get_by_role("button", name = "Next").click()


    #from here 2 step authentications stpes there
    page.pause()

    #save authentication state
    context.storage_state(path = "playwright/.auth/storage_state.json")

    context.close()






