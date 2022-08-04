import pytest
from pages.loginPage import LoginPage
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen
import time

class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()


    def test_homePageTitle(self, setup):
        self.logger.info("****************************** Test_001_Login **********************************************")
        self.logger.info("****************************** Verifying HomePage Title ************************************")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        if act_title == "Swag Labs":
            assert True
            self.driver.close()
            self.logger.info("****************************** HomePage Title test is passed ***************************")
        else:
            self.driver.save_screenshot(r'.\\Screenshots\\' + 'test_homePageTitle.png')
            self.driver.close()
            self.logger.info("****************************** HomePage Title test is failed ***************************")
            assert False

    # @pytest.mark.sanity
    # @pytest.mark.regression
    def test_loginPage(self, setup):
        self.logger.info("****************************** Verifying Login Test ************************************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)           #self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.driver.implicitly_wait(3)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(3)
        act_title = self.driver.title
        if act_title == "Swag Labs":
            assert True
            self.driver.close()
            self.logger.info("****************************** Login test is passed ***************************")
        else:
            self.driver.save_screenshot(r'.\\Screenshots\\' + 'test_loginPage.png')
            self.driver.close()
            self.logger.info("****************************** Login test is failed ***************************")
            assert False

        # self.driver.quit()

