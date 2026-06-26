from playwright.sync_api import Playwright, sync_playwright

with sync_playwright() as playwright:
    browser = playwright.firefox.launch(headless=False, slow_mo = 500) #if we try with google it may show error

    context = browser.new_context(storage_state = "playwright/.auth/storage_state.json") #it allows to store authentication state and save it when we have performed our login

    page = context.new_page()
    page.goto("https://accounts.google.com/")

    #from here 2 step authentications stpes there
    page.pause()

    context.close()