from pages.home_page import HomePage
from pages.entry_ad_page import EntryAdPage

def test_entry_ad(driver):
    driver.get("https://the-internet.herokuapp.com/")

    homepage = HomePage(driver)
    homepage.click_entry_ad_link()

    entry_ad = EntryAdPage(driver)
    #Verify modal is displayed
    assert entry_ad.is_modal_displayed()

    #Close modal
    entry_ad.close_modal()
    entry_ad.refresh_page()


    #Modal is not displayed
    assert entry_ad.is_modal_not_displayed()


    #Re-enable modal
    entry_ad.click_reenable()
    entry_ad.refresh_page()

    assert entry_ad.is_modal_displayed()
