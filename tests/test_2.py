import time

from TestPages import Helper


def test_2(browser):
    main_page = Helper(browser, url="https://sbis.ru/")
    main_page.go_to_site()
    main_page.click_on_the_navigation_bar()
    main_page.check_location()
    main_page.check_partners()
    main_page.change_location()
    time.sleep(10)
    main_page.choose_location()
    time.sleep(15)
    main_page.region_on_page_check()
    assert "41-kamchatskij-kraj" in browser.current_url
    assert "Камчатский край" in browser.title
