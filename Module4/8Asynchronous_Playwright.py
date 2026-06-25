import asyncio
                                                                               #for Asyn we need to wait for all Asynch method with "await" keyword#
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as playwright:
        browser= await playwright.chromium.launch()
        page = await browser.new_page()

        await page.goto("https://playwright.dev")

        print(await page.title())

        await browser.close()


#to run main function here is code

asyncio.run(main())

