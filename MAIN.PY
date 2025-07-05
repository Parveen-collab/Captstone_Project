# Import Playwright's synchronous API for browser automation
from playwright.sync_api import sync_playwright
# Import os for file and directory operations
import os

# Set the output directory for saving job HTML files
output_dir = "Blockchain Developer"

# Create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Start Playwright context
with sync_playwright() as p:
    # Launch Chromium browser in non-headless mode with slow motion to mimic human behavior
    browser = p.chromium.launch(headless=False, slow_mo=50)
    page = browser.new_page()

    # Step 1: Login to LinkedIn
    page.goto("https://www.linkedin.com/login")
    page.fill('input#username', '##########')  # Fill in your LinkedIn username
    page.fill('input#password', '*********')  # Fill in your LinkedIn password
    page.click('button[type="submit"]')      # Click the login button
    page.wait_for_timeout(15000)              # Wait for login to complete

    # Step 2: Navigate to the Jobs section
    page.click("a.global-nav__primary-link[href*='/jobs/']")
    page.wait_for_timeout(5000)

    # Step 3: Search for jobs with the specified title and location
    page.fill("input[aria-label='Search by title, skill, or company']", "Blockchain Developer")
    page.fill("input[aria-label='City, state, or zip code']", "India")
    page.keyboard.press("Enter")
    page.wait_for_timeout(7000)

    job_count = 0  # Counter for saved job postings

    # Step 4: Loop through all job result pages
    while True:
        print(" New page of results...")
       
        # Locate the scrollable container for job cards
        scroll_container = page.locator("div.CENSNYyjUBqTokbIXTuybRoMlHoEzrBFvw")

        # Scroll multiple times to load all job cards on the page
        for _ in range(30):
            scroll_container.evaluate("el => el.scrollBy(0, el.scrollHeight)")
            page.wait_for_timeout(1000)

        # Collect all job card elements
        job_cards = page.locator("[data-control-id]")
        count = job_cards.count()
        print(f" Loaded and found {count} jobs.")

        # Step 5: Iterate through each job card on the page
        for i in range(count):
            try:
                # Scroll job card into view and click to open details
                job_cards.nth(i).scroll_into_view_if_needed()
                job_cards.nth(i).click()
                page.wait_for_timeout(3000)

                # Extract the HTML content of the job details section
                job_html = page.locator(".jobs-details__main-content").inner_html()
                job_count += 1
                file_name = f"{output_dir}/job_{job_count}.html"
                # Save the job HTML to a file
                with open(file_name, "w", encoding="utf-8") as f:
                    f.write(job_html)
                print(f"Saved job {job_count}")

            except Exception as e:
                # Handle errors for individual job cards
                print(f" Error on job {i}: {e}")
                continue

        # Step 6: Go to the next page of job results
        try:
            next_btn = page.locator("button[aria-label='View next page']")
            if next_btn.is_enabled():
                next_btn.click()
                page.wait_for_timeout(5000)
            else:
                print("Reached last page. Done!")
                break
        except Exception as e:
            # Handle errors when clicking the next page button
            print(f" Failed to click next: {e}")
            break
