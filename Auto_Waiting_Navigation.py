
from playwright.sync_api import Playwright, sync_playwright
from time import perf_counter

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False, slow_mo = 800)
    page = browser.new_page()
    print("Page Loading...")
    start = perf_counter()  #it use to count browser loading time


    page.goto("https://playwright.dev/python/" , wait_until="domcontentloaded")  #event "load" loads all the resource in the website including images,icons  and other stuff and its default
                                                                         # event "domcontentloaded" = documents and all html file and text content
                                                                        # event "commit" is used only for html response
                                                                        #event "networkidle" all n/w ins and out finish in browser


    time_taken = perf_counter() - start
    print(f".. page loaded in {round(time_taken , 2)}s")

    browser.close()