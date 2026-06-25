from playwright.sync_api import Playwright, sync_playwright
from time import perf_counter

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False, slow_mo = 800)
    page = browser.new_page()
    page.goto("https://www.scrapethissite.com/pages/ajax-javascript/")


    link = page.get_by_role("link", name="2015")
    link.click()

    print("Loading Oscor for 2015...")
    start = perf_counter()

    first_table_data = page.locator("td.film-title").first  #If only one selector is there like "td.film-title" then we used css selector (page.wait_for_selector(selector = "td.film-title")
    first_table_data.wait_for() #here we wait in script

    time_taken = perf_counter() - start
    print(f"...Movies are loaded , in {round(time_taken, 2)}s!")

    browser.close()