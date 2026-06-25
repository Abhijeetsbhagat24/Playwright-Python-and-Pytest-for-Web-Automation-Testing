from playwright.sync_api import Playwright, sync_playwright

#with event
def on_download(download):
    print("Download received!")
    download.save_as("night.jpg")


with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False, slow_mo = 500)
    page = browser.new_page()
    page.goto("https://unsplash.com/photos/a-full-moon-is-seen-in-the-dark-sky-qe2RkzzMx9A")

    btn = page.get_by_role("link", name = "Download free")

    with page.expect_download() as download_info:
        btn.click()

    #download = download_info.value  #download image in temp variable

    #download.save_as("moon.jpg") #save image in our machine

    browser.close()

