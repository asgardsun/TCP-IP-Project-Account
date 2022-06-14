#실행 파일

from WithDrawThread1 import *
from WithDrawThread2 import *
if __name__ == "__main__":
    # 공유 객체 생성
    account = Account()

    #스레드 클래스의 생성자에서는 account를 None 초기화를 한다.
    thread1 = WithDrawThread1()
    thread2 = WithDrawThread2()

    #스레드 클래스의 setAccount()에서는 account를 실제 인스턴스의 주소로 치환된다.
    #아래 2개의 스레드는 account 인스턴스를 공유하게 된다.
    thread1.setAccount(account)
    thread2.setAccount(account)

    #스레드 실행
    thread1.start()
    thread2.start()