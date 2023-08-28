from playwright.sync_api import Playwright, expect


def test_hw(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://cloud.ru/ru")
    page.locator("#__next > div > header > div.Header_wrapper__5Ytgo > nav > ul > li:nth-child(3)").click()
    page.locator("div.ScrollbarsCustom-Wrapper > div > div > div:nth-child(2)").click()
    page.locator("div.ScrollbarsCustom-Wrapper > div > div > div > div:nth-child(2) > a:nth-child(6) > div > h3").click()
    expect(page).to_have_url("https://cloud.ru/ru/products/oblachnyj-api-gateway-hosting")
    con = playwright.request.new_context()
    res = con.get("https://cloud.ru/ru/products/oblachnyj-api-gateway-hosting")
    assert res.status == 200
    context.close()
    browser.close()
