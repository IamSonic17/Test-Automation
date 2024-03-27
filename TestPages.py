import os
import time

from BaseApp import BasePage
from selenium.webdriver.common.by import By

from loguru import logger


class PagesLocators:
    LOCATOR_SBIS_NAVIGATION_BAR = (By.CSS_SELECTOR, "li[class*=sbisru-Header__menu-item-1]")
    LOCATOR_SBIS_BANNER = (By.CSS_SELECTOR, ".sbisru-Contacts .sbisru-Contacts__logo-tensor[href='https://tensor.ru/']")
    LOCATOR_TENSOR_BLOCK = (By.CSS_SELECTOR, ".s-Grid-col .tensor_ru-Index__block4-content ")
    LOCATOR_TENSOR_AGREEMENT = (By.CSS_SELECTOR, ".tensor_ru-CookieAgreement__close")
    LOCATOR_TENSOR_ELEMENT = (By.CSS_SELECTOR, ".tensor_ru-Index__block4 .tensor_ru-Index__link")
    LOCATOR_TENSOR_PHOTO_BLOCK = (By.CSS_SELECTOR, ".tensor_ru-About__block3-image-wrapper")
    LOCATOR_PHOTOS = (By.CSS_SELECTOR, ".tensor_ru-About__block3-image-wrapper")
    LOCATOR_TENSOR_REGION = (By.CSS_SELECTOR, ".ml-xm-0 .sbis_ru-Region-Chooser__text")
    LOCATOR_TENSOR_PARTNERS = (By.ID, "city-id-2")
    LOCATOR_TENSOR_REGION_2 = (By.CSS_SELECTOR, ".sbis_ru-Region-Panel__item .sbis_ru-link[title='Камчатский край']")
    LOCATOR_TITLE = (By.CSS_SELECTOR, "[class*=state-1]")
    LOCATOR_SBIS_AGREEMENT = (By.CSS_SELECTOR, ".sbis_ru-CookieAgreement__close")
    LOCATOR_SBIS_FOOTER_DOWNLOAD = (By.CSS_SELECTOR, ".sbisru-Footer__link[href='/download']")
    LOCATOR_SBIS_PLUGIN_DOWNLOAD = (By.CSS_SELECTOR, "div[data-id='plugin']")
    LOCATOR_PLUGIN_LINK = (By.CSS_SELECTOR,
                           ".js-link[href='https://update.sbis.ru/Sbis3Plugin/master/win32/sbisplugin-setup-web.exe']")


class Helper(BasePage):
    logger.add("debug.log", format="{time} {level} {message}", level="DEBUG")

    def click_on_the_navigation_bar(self):
        logger.info('Перехожу в раздел "Контакты" (Тест №1)')
        return self.find_element(PagesLocators.LOCATOR_SBIS_NAVIGATION_BAR, time=15).click()

    def click_on_the_banner(self):
        logger.info('Кликаю на баннер "Тензор" (Тест №1)')
        return self.find_element(PagesLocators.LOCATOR_SBIS_BANNER, time=15).click()

    def check_block(self):
        logger.info('Проверяю наличие блока "Сила в людях" (Тест №1)')
        return self.find_element(PagesLocators.LOCATOR_TENSOR_BLOCK, time=15)

    def click_on_the_agreement(self):
        logger.info('Закрываю окно соглашения (Тест №1)')
        return self.find_element(PagesLocators.LOCATOR_TENSOR_AGREEMENT, time=20).click()

    def click_on_the_block_element(self):
        logger.info('Перехожу в "Подробнее" (Тест №1)')
        return self.find_element(PagesLocators.LOCATOR_TENSOR_ELEMENT, time=20).click()

    def find_photo_block(self):
        logger.info('Проверяю наличие блока "Работаем" (Тест №1)')
        target = self.find_element(PagesLocators.LOCATOR_TENSOR_PHOTO_BLOCK, time=10)
        return target

    def check_photos_sizes(self):
        logger.info('Проверяю размер фотографий (Тест №1)')
        sizes_collection = self.find_elements(PagesLocators.LOCATOR_PHOTOS, time=10)
        width_collection = [x.size['width'] for x in sizes_collection if len(x.size) > 0]
        height_collection = [x.size['height'] for x in sizes_collection if len(x.size) > 0]
        sizes_set = set()
        for index in range(4):
            sizes_set.add(width_collection[index])
            sizes_set.add(height_collection[index])
        assert len(sizes_set) == 2

    def check_location(self):
        logger.info('Проверяю регион (Тест №2)')
        return self.find_element(PagesLocators.LOCATOR_TENSOR_REGION, time=10)

    def check_partners(self):
        logger.info('Проверяю список партнеров (Тест №2)')
        return self.find_element(PagesLocators.LOCATOR_TENSOR_PARTNERS, time=10)

    def change_location(self):
        logger.info('Открываю раздел смены региона (Тест №2)')
        return self.find_element(PagesLocators.LOCATOR_TENSOR_REGION, time=35).click()

    def choose_location(self):
        logger.info('Выбираю регион (Тест №2)')
        return self.find_clickable_element(PagesLocators.LOCATOR_TENSOR_REGION_2, time=25).click()

    def region_on_page_check(self):
        logger.info('Проверяю результат смены региона (Тест №2)')
        region = self.find_element(PagesLocators.LOCATOR_TENSOR_REGION, time=10).text
        city = self.find_element(PagesLocators.LOCATOR_TENSOR_PARTNERS, time=10).text
        assert region == "Камчатский край"
        assert city == "Петропавловск-Камчатский"

    def open_download_page(self):
        logger.info('Открываю раздел загрузки приложений (Тест №3)')
        return self.find_element(PagesLocators.LOCATOR_SBIS_FOOTER_DOWNLOAD, time=20).click()

    def click_on_sbis_agreement(self):
        logger.info('Закрываю окно соглашения (Тест №3)')
        return self.find_element(PagesLocators.LOCATOR_SBIS_AGREEMENT, time=20).click()

    def choose_plugin(self):
        logger.info('Выбираю раздел "Плагин" (Тест №3)')
        return self.find_element(PagesLocators.LOCATOR_SBIS_PLUGIN_DOWNLOAD, time=20).click()

    def click_download(self):
        logger.info('Скачиваю файл и сверяю размер (Тест №3)')
        current_directory = os.getcwd()
        before = os.listdir(current_directory[:-5])
        self.find_element(PagesLocators.LOCATOR_PLUGIN_LINK, time=25).click()
        time.sleep(60)
        max_wait = 10
        current_wait = 0
        file_name = ''
        while current_wait < max_wait:
            after = os.listdir(current_directory[:-5])
            change = set(after) - set(before)
            if len(change) == 1:
                file_name = str(change.copy())
                break
            else:
                current_wait += 1
                time.sleep(1)
        return file_name
