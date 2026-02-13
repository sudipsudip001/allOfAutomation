import time
from playwright.sync_api import sync_playwright
from gmail_api import get_messages
import logging
from dotenv import load_dotenv
import os

load_dotenv()
EMAIL = os.getenv("email")
PHONE = os.getenv("phone")
PASSWORD = os.getenv("password")

logging.basicConfig(filemode="operations.log", level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=False,
            slow_mo=500
        )

        page = browser.new_page()

        page.goto("https://authorized-partner.vercel.app/")
        page.wait_for_load_state("networkidle")

        page.click("text=Get Started")
        page.wait_for_load_state("networkidle")


        page.get_by_label('I agree to the Terms of Service and Privacy Policy').check()

        page.click("text=Continue")
        page.wait_for_load_state("networkidle")

        # 1. FOR SETTING UP ACCOUNT
        try:
            page.fill("#«r0»-form-item", "John")
            page.fill("#«r1»-form-item", "Doe")
            page.fill("#«r2»-form-item", EMAIL)
            page.fill("#«r4»-form-item", PHONE)
            page.fill('input[name="password"]', PASSWORD)
            page.fill('input[name="confirmPassword"]', PASSWORD)

            page.click("text=Next")
            page.wait_for_load_state("networkidle")
            logger.info("SETTING UP ACCOUNT COMPLETED")
        except Exception as e:
            logger.error(f"Error encountered in setting up your account: {e}")


        # 2.1. FOR AGENCY DETAILS
        time.sleep(10)
        try:
            otp = get_messages()
            page.locator('input[data-input-otp="true"]').fill(str(otp))
            page.click("text=Verify Code")
            page.wait_for_load_state("networkidle")

            # 2.2. REAL AGENCY DETAILS
            page.fill('input[name="agency_name"]', "John Doe Agency")
            page.fill('input[name="role_in_agency"]', "Financial Consultant")
            page.fill('input[name="agency_email"]', EMAIL)
            page.fill('input[name="agency_website"]', "www.sydney.com")
            page.fill('input[name="agency_address"]', "Sydney")

            button = page.locator('label:has-text("Region of Operation") + button')
            button.click()

            countries_to_select = ["Australia", "France", "United States of America"]
            for country in countries_to_select:
                page.get_by_text(country, exact=True).click()

            page.click("text=Next")
            page.wait_for_load_state("networkidle")
            logger.info("AGENCY DETAILS COMPLETED")
        except Exception as e:
            logger.error(f"Error encountered in filling the agency details: {e}")


        # 3. FOR PROFESSIONAL EXPERIENCE
        try:
            try:
                page.locator('select').select_option('5')
            except Exception as e:
                print(f"Error occured: {e}")

            page.fill('input[name="number_of_students_recruited_annually"]', "50000")
            page.fill('input[name="focus_area"]', "Graduate students admission to Sydney")
            page.fill('input[name="success_metrics"]', "85")

            try:
                page.get_by_label("Career Counseling").check()
            except Exception as e:
                print(f"Error occured: {e}")

            page.click("text=Next")
            page.wait_for_load_state("networkidle")
            logger.info("PROFESSIONAL EXPERIENCE FILLING COMPLETED")
        except Exception as e:
            logger.error(f"Error encountered in filling the professional experience: {e}")


        # 4. FOR VERIFICATION AND PREFERENCES.
        try:
            page.fill('input[name="business_registration_number"]', "92472")
            button = page.locator('label:has-text("Preferred Countries") + button')
            button.click()
            countries_to_select = ["Australia", "France", "United States of America"]
            for country in countries_to_select:
                page.get_by_text(country, exact=True).click()

            try:
                page.get_by_label("Colleges").check()
            except Exception:
                print(f"Error occured: {e}")

            page.fill('input[name="certification_details"]', "988823")
            try:
                page.locator('input[type="file"]').nth(0).set_input_files('first.pdf')
                page.locator('input[type="file"]').nth(1).set_input_files('second.jpeg')
            except Exception:
                print(f"Failed to add files")


            page.click("text=Submit")
            page.wait_for_load_state("networkidle")
            logger.info("ALL FILES AND DETAILS HAS BEEN SUBMITTED SUCCESSFULLY")
        except Exception as e:
            logger.error(f"Error encountered in the Verification and Preferences step: {e}")

        page.wait_for_timeout(5000)
        browser.close()

if __name__ == "__main__":
    main()