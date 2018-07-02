class Account(object):
    def __init__(self, rate):
        """帐号类，amount 是美元金额"""
        self.__amt = 0
        self.rate = rate

    @property
    def amount(self):
        """账户余额(美元)"""
        return self.__amt

    @property
    def cny(self):
        """账户余额(人民币)"""
        return self.__amt * self.rate

    @amount.setter
    def amount(self, value):
        if value < 0:
            print("sorry,no negative amount in the account.")
            return
        self.__amt = value


if __name__ == '__main__':
    # 汇率
    acc = Account(rate=6.63)
    acc.amount = 20
    print("Dollar amount:", acc.amount)
    print("In CNY:", acc.cny)
    acc.amount = -200
    print("Dollar amount:", acc.amount)
