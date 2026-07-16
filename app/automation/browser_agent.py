from playwright.sync_api import sync_playwright
import time


def play_youtube_music(song_name: str):
    with sync_playwright() as p:

        browser = p.chromium.launch(
            channel="chrome",   # Installed Google Chrome use karega
            headless=False
        )

        page = browser.new_page()

        page.goto("https://www.youtube.com")

        page.wait_for_timeout(3000)

        # Search box me song type karo
        page.locator("input[name='search_query']").fill(song_name)

        page.keyboard.press("Enter")

        page.wait_for_timeout(3000)

        # First video par click
        page.locator("ytd-video-renderer").first.click()

        # Video load hone do
        time.sleep(5)

        return browser