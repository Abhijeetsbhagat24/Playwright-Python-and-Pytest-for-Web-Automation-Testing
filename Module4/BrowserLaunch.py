# sync playwright
from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:

        #Launch browser
    browser = playwright.chromium.launch(headless = False, slow_mo = 1000  )

        #create a new page
    page = browser.new_page()

        #visit the playwright website
    page.goto("https://playwright.dev/python")

    browser.close()
#till here the code runs in background to see the web page need to add below commands in browser
#(headless=False)  by default its always true
#(slow_mo= ) to delay the page time so can visible properly