from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    #Launch a browser
   browser= playwright.chromium.launch(headless=False,slow_mo=400)
    #Create a New Page
   page=browser.new_page()
    #Visit the playwright website
   page.goto("https://playwright.dev/python")

   docs_button=page.get_by_role('link',name="Docs")
   docs_button.click()

   browser.close()



