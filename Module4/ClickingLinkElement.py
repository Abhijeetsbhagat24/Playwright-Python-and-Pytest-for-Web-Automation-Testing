#Click on DOC button on web page

from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:

        #Launch browser
    browser = playwright.chromium.launch(headless = False, slow_mo = 5000  )

        #create a new page
    page = browser.new_page()

        #visit the playwright website
    page.goto("https://playwright.dev/python")

    #here is code for click on DOC
    #Locate a link element with "Docs" text
    docs_button = page.get_by_role('link' , name = "Docs")
    docs_button.click()

    browser.close()