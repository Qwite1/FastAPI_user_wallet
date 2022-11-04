import datetime
import config
import pydantic_models
import bit
from db import *

wallet = bit.Key()
print(f"Баланс: {wallet.get_balance()}")
print(f"Адрес: {wallet.address}")
print(f"Приватный ключ: {wallet.to_wif()}")

wallet.send()