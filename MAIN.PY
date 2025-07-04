from playwright.sync_api import sync_playwright
import os

# Create output directory if it doesn't exist
output_dir = "Blockchain Developer"

os.makedirs(output_dir, exist_ok=True)

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=50)
    page = browser.new_page()

    # Login
    page.goto("https://www.linkedin.com/login")
    page.fill('input#username', '##########')
    page.fill('input#password', '*********')
    page.click('button[type="submit"]')
    page.wait_for_timeout(15000)

    # Navigate to Jobs
    page.click("a.global-nav__primary-link[href*='/jobs/']")
    page.wait_for_timeout(5000)

    # Search Jobs
    page.fill("input[aria-label='Search by title, skill, or company']", "Blockchain Developer")
    page.fill("input[aria-label='City, state, or zip code']", "India")
    page.keyboard.press("Enter")
    page.wait_for_timeout(7000)

    job_count = 0

    while True:
        print(" New page of results...")
       
        # Locate the scroll container
        scroll_container = page.locator("div.CENSNYyjUBqTokbIXTuybRoMlHoEzrBFvw")

        # Scroll to load all jobs
        for _ in range(30):
            scroll_container.evaluate("el => el.scrollBy(0, el.scrollHeight)")
            page.wait_for_timeout(1000)

        # Collect job cards
        job_cards = page.locator("[data-control-id]")
        count = job_cards.count()
        print(f" Loaded and found {count} jobs.")

        for i in range(count):
            try:
                job_cards.nth(i).scroll_into_view_if_needed()
                job_cards.nth(i).click()
                page.wait_for_timeout(3000)

                job_html = page.locator(".jobs-details__main-content").inner_html()
                job_count += 1
                file_name = f"{output_dir}/job_{job_count}.html"
                with open(file_name, "w", encoding="utf-8") as f:
                    f.write(job_html)
                print(f"Saved job {job_count}")

            except Exception as e:
                print(f" Error on job {i}: {e}")
                continue

        # Go to next page
        try:
            next_btn = page.locator("button[aria-label='View next page']")
            if next_btn.is_enabled():
                next_btn.click()
                page.wait_for_timeout(5000)
            else:
                print("Reached last page. Done!")
                break
        except Exception as e:
            print(f" Failed to click next: {e}")
            break
