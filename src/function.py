class Shopping:

    def _init_(self, context):
        self.driver = context.driver
        self.screen = context.driver.screen

    def select_id(self, label_text, option, option_list):
        select_request = self.screen.get_by_id(label_text)
        select_request.send_keys(option)
        options = self.screen.find_all_by_text(option)
        options[option_list].click()

    def login(self):
        self.screen.find_by_text('Swag Labs')
        username= self.screen.get_by_id('user-name')
        username.send_keys('standard_user')
        password = self.screen.get_by_id('password')
        password.send_keys('secret_sauce')
        button_Login = self.screen.get_by_text('Login')
        button_Login.click()

