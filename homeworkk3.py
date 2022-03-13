class Webpush:
    def __init__(self, platform, optin: bool, global_frequency_capping, start_date, end_date, language, push_type):
        self.platform = platform
        self.optin = optin
        self.global_frequency_capping = global_frequency_capping
        self.start_date = start_date
        self.end_date = end_date
        self.language = language
        self.push_type = push_type

    @staticmethod
    def send_push():
        print("**********\nPush Gönderildi!")


class Triggerpush(Webpush):
    def __init__(self, trigger_page: str, platform, optin: bool, global_frequency_capping, start_date, end_date,
                 language, push_type):
        super().__init__(platform, optin, global_frequency_capping, start_date, end_date, language, push_type)
        self.trigger_page = trigger_page

    def triggerpush(self):
        print("**********\nTrigger Page: {} \nPlatform: {} \nOptin: {} \nGFC: {} \nStart Date: {} \nEnd Date: {} "
              "\nLanguage: {}"
              " \nPush Type: {}".format(self.trigger_page,
                                        self.platform, self.optin, self.global_frequency_capping, self.start_date,
                                        self.end_date, self.language,
                                        self.push_type))


class Bulkpush(Webpush):
    def __init__(self, send_date: int, platform, optin: bool, global_frequency_capping, start_date, end_date, language,
                 push_type):
        super().__init__(platform, optin, global_frequency_capping, start_date, end_date, language, push_type)
        self.send_date = send_date

    def bulkpush(self):
        print("**********\nSend Date: {} \nPlatform: {} \nOptin: {} \nGFC: {} \nStart Date: {} \nEnd Date: {}"
              " \nLanguage: {}"
              " \nPush Type: {}".format(self.send_date,
                                        self.platform, self.optin, self.global_frequency_capping, self.start_date,
                                        self.end_date, self.language,
                                        self.push_type))


class Segmentpush(Webpush):
    def __init__(self, segment_name: str, platform, optin: bool, global_frequency_capping, start_date, end_date,
                 language, push_type):
        super().__init__(platform, optin, global_frequency_capping, start_date, end_date, language, push_type)
        self.segment_name = segment_name

    def segmentpush(self):
        print(
            "**********\nSegment Name: {} \nPlatform: {} \nOptin: {} \nGFC: {} \nStart Date: {} \nEnd Date: {}"
            " \nLanguage: {}"
            " \nPush Type: {}".format(
                self.segment_name,
                self.platform, self.optin, self.global_frequency_capping, self.start_date, self.end_date, self.language,
                self.push_type))


class Pricealertpush(Webpush):
    def __init__(self, price_info: int, discount_rate: float, platform, optin: bool,
                 global_frequency_capping,
                 start_date, end_date, language, push_type):
        super().__init__(platform, optin, global_frequency_capping, start_date, end_date, language, push_type)
        self.discountprice = None
        self.price_info = price_info
        self.discount_rate = discount_rate

    def discount_price(self):
        discount = self.price_info * self.discount_rate
        self.discountprice = self.price_info - discount
        return self.discountprice

    def pricealertpush(self):
        print(
            "**********\nPrice Information: {} \nDiscount Rate: {} \nDiscount Price: {} \nPlatform: {} \nOptin: {}"
            " \nGFC: {}"
            " \nStart Date: {} \nEnd Date: {} \nLanguage: {} \nPush Type: {}".format(
                self.price_info, self.discount_rate, self.discount_price(), self.platform, self.optin,
                self.global_frequency_capping, self.start_date, self.end_date, self.language, self.push_type))


class Instockpush(Webpush):
    def __init__(self, stock_info: bool, platform, optin: bool, global_frequency_capping, start_date, end_date,
                 language, push_type):
        super().__init__(platform, optin, global_frequency_capping, start_date, end_date, language, push_type)
        self.stock_info = stock_info

    def stockupdate(self):
        if not self.stock_info:
            self.stock_info = True
        else:
            self.stock_info = False
        print(
            "**********\nStock Information: {}  \nPlatform: {} \nOptin: {} \nGFC: {} \nStart Date: {} \nEnd Date: {} "
            "\nLanguage: {} \nPush Type: {}".format(
                self.stock_info, self.platform, self.optin,
                self.global_frequency_capping, self.start_date, self.end_date, self.language, self.push_type))


webpush1 = Triggerpush("PDP", "windows", True, "Bir", "01/03/22", "01/03/23", "All Language", "Trigger Push")
webpush1.send_push()
webpush1.triggerpush()
webpush2 = Bulkpush(5, "windows", True, "Bir", "01/03/22", "01/03/23", "All Language", "Bulk Push")
webpush2.send_push()
webpush2.bulkpush()
webpush3 = Segmentpush("Purchase History", "windows", True, "Bir", "01/03/22", "01/03/23", "Turkish", "Segment Push")
webpush3.send_push()
webpush3.segmentpush()
webpush4 = Pricealertpush(100, 0.10, "windows", True, "Bir", "01/03/22", "01/03/23", "Spanish", "Price Alert Push")
webpush4.send_push()
webpush4.pricealertpush()
webpush5 = Instockpush(True, "windows", True, "Bir", "01/03/22", "01/03/23", "All Language", "In Stock Push")
webpush5.send_push()
webpush5.stockupdate()
