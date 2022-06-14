#입출금을 같이 하는 스레드 클래스 작성

from Account import *


class WithDrawThread1(threading.Thread):
    def __init__(self):
        super().__init__()

    def setAccount(self, account):
        self.account = account
        self.setName('어머니')

    def run(self):
        self.account.setBalance(1000)
        self.account.withDraw(500)
        self.account.withDraw(300)
