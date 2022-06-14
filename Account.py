#Account 클래스 정의

import threading, time
lock = threading.Lock()
#공유 객체

class Account():
    def __int__(self,balance):
        super().__init__()
        self.balance = balance #계좌금액 초기화

    #현재 잔액을 리턴해주는 getter()
    def getBalance(self):
        time.sleep(1)
        return self.balance

    #입금 처리해주는 setter()
    def setBalance(self,balance):
        lock.acquire() #잠금 시작
        self.balance = balance #입금액으로 잔액을 바꿈

        #2초간 일시정지
        time.sleep(2)
        #현재 실행중인 스레드 이름과 balance 값을 출력하는 코드
        print(threading.current_thread().name,'이/가 입금 : ',self.balance,"원")
        lock.release() #잠금 해제

    #출금하는 메소드
    def withDraw(self,money):
        lock.acquire()
        #잔액이 출금 금액보다 더 많다면
        if self.balance >= money:
            time.sleep(1)
            self.balance -= money
            print(threading.current_thread().name, "이/가 출금",money,'원')
            print('통장 잔액 : ',self.getBalance(),'원')
        else: #출금 금액이 잔액보다 많을 때
            try:
                print(threading.current_thread().name,'이/가 출금',money,'원 출금 시도 하였습니다.')
                raise Exception() #강제로 예외 발생 시키기
            except Exception:
                print('잔액이 부족합니다.')
        lock.release()


