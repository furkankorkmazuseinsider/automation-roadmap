class WebPush:

    def __init__(self, platform, optin: bool, global_frequency_capping, start_date, end_date, language, push_type):
        self.platform = platform
        self.optin = optin
        self.global_frequency_capping = global_frequency_capping
        self.start_date = start_date
        self.end_date = end_date
        self.language = language
        self.push_type = push_type

    def send_push(self):
        print("**********\n{} Gönderildi!".format(self.push_type))


class TriggerPush(WebPush):

    def __init__(self, trigger_page: str, platform, optin: bool, global_frequency_capping, start_date, end_date,
                 language, push_type):
        super().__init__(platform, optin, global_frequency_capping, start_date, end_date, language, push_type)

        self.trigger_page = trigger_page

    def trigger_push(self):
        print("**********\nTrigger Page: {} \nPlatform: {} \nOptin: {} \nGFC: {} \nStart Date: {} \nEnd Date: {} "
              "\nLanguage: {} \nPush Type: {}".format(self.trigger_page, self.platform, self.optin,
                                                      self.global_frequency_capping, self.start_date, self.end_date,
                                                      self.language, self.push_type))


class BulkPush(WebPush):

    def __init__(self, send_date: int, platform, optin: bool, global_frequency_capping, start_date, end_date, language,
                 push_type):
        super().__init__(platform, optin, global_frequency_capping, start_date, end_date, language, push_type)

        self.send_date = send_date

    def bulk_push(self):
        print("**********\nSend Date: {} \nPlatform: {} \nOptin: {} \nGFC: {} \nStart Date: {} \nEnd Date: {}"
              " \nLanguage: {} \nPush Type: {}".format(self.send_date, self.platform, self.optin,
                                                       self.global_frequency_capping, self.start_date,
                                                       self.end_date, self.language, self.push_type))


class SegmentPush(WebPush):

    def __init__(self, segment_name: str, platform, optin: bool, global_frequency_capping, start_date, end_date,
                 language, push_type):
        super().__init__(platform, optin, global_frequency_capping, start_date, end_date, language, push_type)

        self.segment_name = segment_name

    def segment_push(self):
        print("**********\nSegment Name: {} \nPlatform: {} \nOptin: {} \nGFC: {} \nStart Date: {} \nEnd Date: {}"
              " \nLanguage: {} \nPush Type: {}".format(self.segment_name, self.platform, self.optin,
                                                       self.global_frequency_capping, self.start_date,
                                                       self.end_date, self.language, self.push_type))


class PriceAlertPush(WebPush):

    def __init__(self, price_info: int, discount_rate: float, platform, optin: bool, global_frequency_capping,
                  start_date, end_date, language, push_type):
        super().__init__(platform, optin, global_frequency_capping, start_date, end_date, language, push_type)

        self.discounted_price = None
        self.price_info = price_info
        self.discount_rate = discount_rate

    def discount_price(self):
        discount = self.price_info * self.discount_rate
        self.discounted_price = self.price_info - discount

        return self.discounted_price

    def price_alert_push(self):
        print("**********\nPrice Information: {} \nDiscount Rate: {} \nDiscount Price: {} \nPlatform: {} \nOptin: {}"
              " \nGFC: {} \nStart Date: {} \nEnd Date: {} \nLanguage:"
              " {} \nPush Type: {}".format(self.price_info, self.discount_rate, self.discount_price(), self.platform,
                                           self.optin, self.global_frequency_capping, self.start_date, self.end_date,
                                           self.language, self.push_type))


class InStockPush(WebPush):

    def __init__(self, stock_info: bool, platform, optin: bool, global_frequency_capping, start_date, end_date,
                 language, push_type):
        super().__init__(platform, optin, global_frequency_capping, start_date, end_date, language, push_type)

        self.stock_info = stock_info

    def stock_update(self):
        self.stock_info = not self.stock_info

        return self.stock_info

    def in_stock_push(self):
        print("**********\nStock Information: {}  \nPlatform: {} \nOptin: {} \nGFC: {} \nStart Date: {} \nEnd Date: {} "
              "\nLanguage: {} \nPush Type: {}".format(self.stock_update(), self.platform, self.optin,
                                                      self.global_frequency_capping, self.start_date, self.end_date,
                                                      self.language, self.push_type))


WebPush1 = TriggerPush("PDP", "Desktop", True, "Bir", "01/03/22", "01/03/23", "All Language", "Trigger Push")
WebPush1.send_push()
WebPush1.trigger_push()

WebPush2 = BulkPush(5, "MOBILE", True, "İki", "01/03/22", "01/03/23", "All Language", "Bulk Push")
WebPush2.send_push()
WebPush2.bulk_push()

WebPush3 = SegmentPush("Purchase History", "TABLET", True, "Bir", "01/03/22", "01/03/23", "Turkish", "Segment Push")
WebPush3.send_push()
WebPush3.segment_push()

WebPush4 = PriceAlertPush(1000, 0.15, "DESKTOP", True, "Üç", "01/03/22", "01/03/23", "Spanish", "Price Alert Push")
WebPush4.send_push()
WebPush4.price_alert_push()

WebPush5 = InStockPush(True, "MOBILE", True, "Beş", "01/03/22", "01/03/23", "Arabic", "In Stock Push")
WebPush5.send_push()
WebPush5.in_stock_push()
