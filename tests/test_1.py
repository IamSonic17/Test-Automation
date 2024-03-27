from selenium.common import ElementNotInteractableException
from selenium.webdriver import ActionChains

from TestPages import Helper


def test_1(browser):
    main_page = Helper(browser, url="https://sbis.ru/")
    main_page.go_to_site()
    main_page.click_on_the_navigation_bar()
    main_page.click_on_the_banner()
    new_tab = browser.window_handles[1]
    browser.switch_to.window(new_tab)
    main_page.check_block()

    try:
        main_page.click_on_the_agreement()
    except ElementNotInteractableException:
        pass

    main_page.click_on_the_block_element()
    actions = ActionChains(browser)
    actions.move_to_element(main_page.find_photo_block())
    actions.perform()
    main_page.check_photos_sizes()
