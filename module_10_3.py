import threading
import random
from threading import Thread
from time import sleep


class Bank(Thread):
    def __init__(self):
        super().__init__()
        self.balance = 0
        self.change = 0
        self.lock = threading.Lock()

    def deposit(self):
        for _ in range(100):
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            self.change = random.randint(50,500)
            self.balance += self.change
            print(f"Пополнение: {self.change}. Баланс: {self.balance}")
            sleep(0.001)

    def take(self):
        for _ in range(100):
            self.change = random.randint(50, 500)
            print(f"Запрос на {self.change}")
            if self.change <= self.balance:
                self.balance -= self.change
                print(f"Снятие: {self.change}. Баланс: {self.balance}")
            else:
                print(f"Запрос отклонён, недостаточно средств")
                self.lock.acquire()
            sleep(0.001)


bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')