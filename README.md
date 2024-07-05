# The "Rock - Paper - Scissors" Game 
лесна и проста игра за развлечение
играта е създадена на език за програмиране - Python. Проектът е създаден при следване на следните стъпки: 1.Инициализация на променливи и въвеждане на данни - задаване на възможните опции за игра(камък, ножица, хартия) и получаване на избор от играча чрез вход от клавиатурата. 2.Генериране на случайно число за избор на компютъра между камък, ножица и хартия. 3.Определяне на резултата на играта чрез сравнение на изборите на играча и компютъра за определяне на победител 4.Извеждане на резултата като се изведе избора на компютъра и се извежда съобщение за загуба, равенство или победа. След това може да се избере повторна игра
Включени са библиотека random, използвана за генериране на случайна възможност, алгоритъм за сравнение, условни оператори (if-elif-else), цикъл while, променливи, вход и изход от конзолата, функции като input() и print(), break, continue.
[Source Code](PythonApplication2.py)
![image](https://github.com/swx8gg0/RockPaperScissorsbyIvaylo/assets/174589239/5df93894-3185-4ab4-814c-73a1438e42b3)
live demo: https://replit.com/@stefanovivaylo9/PythonApplication2py

from itertools import product
import uuid
import datetime
from typing import List


class Product:
    def __init__(self,Name,Category,Price,StockQuantity,Description):
        self.ProductId = str(uuid.uuid4())
        self.Name = Name
        self.Category = Category
        self.Price = Price
        self.StockQuantity = StockQuantity
        self.Description = Description
        self.IsAvailable = StockQuantity > 0

    def __str__(self):
        return (f'Product Id: {self.ProductId}\n'f'Name: {self.Name}\n'f'Category: {self.Category}\n'f'Price: {self.Price:.2f}\n'f'StockQuantity: {self.StockQuantity}\n'f'Description: {self.Description}\n'f'IsAvailable: {"Yes" if self.IsAvalailable else "No"}')
        
class Customer:
    def __init__(self, FullName, Email,PhoneNumber, ShippingAddress):
        self.CustomerId = str(uuid.uuid4())
        self.FullName = FullName
        self.Email = Email
        self.PhoneNumber = PhoneNumber
        self.ShippingAddress = ShippingAddress

    def __str__(self):
        return(f'Customer ID: {self.CustomerId}\n'f'Full Name: {self.FullName}\n'f'Email: {self.Email}\n'f'Phone Number: {self.PhoneNumber}\n'f'Shipping Address: {self.ShippingAddress}')

class Order:
    def __init__(self, CustomerId, OrderItems: List[Product], status ="waiting"):
        self.OrderId= str(uuid.uuid4())
        self.CusotmerId = CustomerId
        self.OrderDate = datetime.now()
        self.OrderItems = OrderItems
        self.TotalAmount = self.TotalAmount()
        self.status = status
    
    def totalamount(self):
        return sum(item.Price for item in self.OrderItems)

    def __str__(self):
        item_str = "\n".join([f' - {item.Name}: {item.Price}' for item in self.OrderItems])
        return (f'Order Id: {self.OrderId}\n'f'Customer Id: {self.CustomerId}\n'f'Order Date: {self.OrderDate}\n'f'Total Amount: {self.TotalAmount:.2f}\n'f'Status: {self.status}\n'f'Order Items:\n{item_str}')

class Category:
    def __init__(self, Name, Description, Products: List[Product]):
        self.CategoryId = str(uuid.uuid4())
        self.Name = Name
        self.Description = Description
        self.Products = Products

class Payment:
    def __init__(self, OrderId, PaymentDate, Amount, PaymentMethod):
        self.PaymentId = str(uuid.uuid4())
        self.OrderId = OrderId
        self.PaymentDate = PaymentDate
        self.Amount = Amount
        self.PaymentMethod = PaymentMethod
    def __str__(self):
        return(f)
