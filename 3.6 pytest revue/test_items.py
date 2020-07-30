# import time

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_check_the_button_add_to_basket_on_the_product_page(browser):
    browser.get(link)
    # time.sleep(30)
    btn_add_to_basket = browser.find_element_by_css_selector('.btn-add-to-basket')
    
    assert btn_add_to_basket, 'add to basket button not found'
