import os
import time

from selenium.common import ElementNotInteractableException

from TestPages import Helper


def test_3(browser):
    current_directory = os.getcwd()
    main_page = Helper(browser, url="https://sbis.ru/")
    main_page.go_to_site()

    try:
        main_page.click_on_sbis_agreement()
    except ElementNotInteractableException:
        pass

    main_page.open_download_page()
    time.sleep(10)
    main_page.choose_plugin()
    time.sleep(10)
    name = main_page.click_download()
    file_info = os.stat(current_directory[:-5] + name[2:-2])
    assert file_info.st_size == 8699000
