import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import traceback


class TestCodedUI:
    def test_search_and_buy(self):
        CHROME_DRIVER_PATH = r"E:\Project\Test\drivers\chromedriver.exe"
        service = Service(executable_path=CHROME_DRIVER_PATH)
        driver = webdriver.Chrome(service=service)
        driver.maximize_window()

        try:
            # 1. 打开首页
            driver.get("http://www.litemall360.com:8082")
            print("首页已打开")

            # 2. 点击首页搜索框
            first_search = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "input[placeholder='点击前往搜索']"))
            )
            first_search.click()
            print("进入搜索页面")

            # 3. 输入关键词并搜索
            second_input = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input[placeholder='请输入商品名称']"))
            )
            second_input.clear()
            second_input.send_keys("母亲节")
            second_input.send_keys(Keys.ENTER)
            print("已搜索母亲节")

            # 4. 等待商品列表出现
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".van-card"))
            )
            print("搜索结果已加载")

            # 5. 点击第一个商品图片进入详情页
            product_img = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "img.van-image__img"))
            )
            product_img.click()
            print("已进入详情页")

            # 6. 点击立即购买按钮
            buy_btn = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button.van-button--danger.van-button--large"))
                )
            print(f"按钮文本：{buy_btn.text}")
            buy_btn.click()
            print("已点击立即购买按钮")

            # 7. 选择商品规格（先规格后颜色）
            try:
                # 点击规格（1.5m床垫*1+枕头*2）
                spec_btn = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable(
                        (By.XPATH, "//div[@class='van-sku-row__item-name' and contains(text(), '1.5m床垫')]"))
                )
                spec_btn.click()
                print("已选择：1.5m床垫*1+枕头*2")

                # 点击颜色（浅杏粉）
                spec_color = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable(
                        (By.XPATH, "//div[@class='van-sku-row__item-name' and contains(text(), '浅杏粉')]"))
                )
                spec_color.click()
                print("已选择：浅杏粉")
            except Exception as e:
                print(f"选择规格时出错: {e}")
                # 如果未找到，尝试点击任意第一个规格选项
                try:
                    any_spec = WebDriverWait(driver, 5).until(
                        EC.element_to_be_clickable((By.CSS_SELECTOR, ".van-sku-row__item-name"))
                    )
                    any_spec.click()
                    print("已选择第一个可用规格")
                except:
                    print("未找到任何规格选项，可能无需选择")

            # 8. 点击立即购买按钮
            buy_btn = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button.van-button--danger.van-button--large"))
            )
            print(f"按钮文本：{buy_btn.text}")
            buy_btn.click()
            print("已点击立即购买按钮")

            # 可选：等待确认页面或弹窗
            time.sleep(2)
            # driver.save_screenshot("after_buy.png")

        except Exception as e:
            print(f"执行出错: {e}")
            # driver.save_screenshot("error.png")
            traceback.print_exc()
            raise  # 让 pytest 知道测试失败
        finally:
            time.sleep(3)
            driver.quit()


if __name__ == "__main__":
    pytest.main()