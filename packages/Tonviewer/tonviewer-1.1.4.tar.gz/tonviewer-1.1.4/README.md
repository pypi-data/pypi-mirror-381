<p align="center">
  <img align="center" width="350" src="https://github.com/user-attachments/assets/779356f9-84af-4247-83f0-32be2229c569" />

  <h1 align="center">TonViewer</h1>
  <h3 align="center"></h3>
</p>


<p align="center">

<a href="https://pypi.org/project/Tonviewer/">
    <img src="https://img.shields.io/pypi/v/Tonviewer?color=red&logo=pypi&logoColor=red">
  </a>

  <a href="https://t.me/Pycodz">
    <img src="https://img.shields.io/badge/Telegram-Channel-blue.svg?logo=telegram">
  </a>
  
  <a href="https://t.me/DevZ44d" target="_blank">
    <img alt="Telegram Owner" src="https://img.shields.io/badge/Telegram-Owner-red.svg?logo=telegram" />
  </a>
</p>

#### 🚀 Quick Start
```python
## Prints TON , transactions and balance of wallet
from Tonviewer import Wallet , Coin , HashTx
wallet = Wallet("")    #wallet_address_here
#Example : UQBAZ3qWaaoIC8Pq5ELnz2ofYoGN_E3mhzxhE-8EWTpMYgyc
wallet.balance()
wallet.transactions(limit=3)    #limit : int , get transactions of Wallet default = 1

# Prints live price
coin = Coin("")   #ex: "toncoin" , "bitcoin" , ...
coin.price()
# Hash
# Option A: Pass a transaction hash
parser = HashTx(hashtx="b4566294bb20e0c22c57109f1128b903d4446d12710b3926b48c42cfc60dd097")
parser.get()  # prints & returns dict

```

### Installation and Development 🚀

### Via PyPi ⚡️
```shell
# via PyPi
pip install Tonviewer -U
```

### 💎 TON Crypto Info Scraper

- TON Crypto Info Scraper is a Python library that allows you to fetch real-time data from the TON blockchain and CoinGecko without needing any APIs.

- It enables users to view wallet **balances** and **live coin information** and get **transactions** of Wallet with ease, making it perfect for TON developers, analysts, and bot creators.


### Using in Terminal 🚀
```shell
Tonviewer -[OPTIONS] "[Wallet]"
```

### Usage 📚
```text
Tonviewer -[OPTIONS] "[FOR-OPTION]"

Options
    -b, --balance                   Prints balance of wallet .
    -p, --price                     Prints live price #ex: toncoin , bitcoin , ... .
    -t, --transactions              Get transactions of Wallet . 
    -l, --limit                     Number of times to get transactions .
    -h, --help                      Display help message .
    -v, --version                   Show Version Of Libarary and info .
```

### 📦 Example For Usage .
```shell
#Example Wallet : "UQAh_cfG…-9h50k1D
Tonviewer -b "UQAh_cfG…-9h50k1D"
          -p "bitcoin"
          -t "UQAh_cfG…-9h50k1D" -l 4
          -h
          -v
```

### 📦 Example format response of `transactions` Method ,
```json
{
  "Time": "12 Aug 08:03",
  "Action": "Sent TON",
  "From": "UQBAZ3qWaaoIC8Pq5ELnz2ofYoGN_E3mhzxhE-8EWTpMYgyc",
  "To": "Fragment",
  "Paid For": "890 Telegram Stars",
  "Price": "−3.908 TON ≈ 12.23204 $",
  "Limit": "1"
  }
```

### 📦 Example Output of `HashTx` Method

### ✅ Successful Transaction:
```json
{
  "Time": "12.08.2025, 11:03:55",
  "Action": "SUCCESSFUL TRANSFER",
  "From": "UQBAZ3qWaaoIC8Pq5ELnz2ofYoGN_E3mhzxhE-8EWTpMYgyc",
  "To": "Fragment",
  "Paid For": "890 Telegram Stars",
  "Price": "−3.908 TON ≈ 12.23204 $"
}
```

### ❌ Failed Transaction:
```json
{
  "Time": "08.08.2025, 16:52:43",
  "Action": "FAILED TRANSFER",
  "From": "pointcreator.ton",
  "To": "Telegram"
}
```

### ⚠️ Invalid Hash:
```json
{
  "Error": "This doesn't look like a valid transaction address. Where'd you get that?"
}
```


### ✨ Features

- 🧾  **Real-time** TON wallet balance fetching.
- 💬 **Live** cryptocurrency price lookup.
- 🔎 **Transaction by Hash** → Simply pass a transaction hash, it grabs the page via Selenium.
- 📄 **Parse Raw HTML** → Already have the page source? Pass it directly.
- 🟢 **Successful TX** → Extracts `Time`, `Action`, `From`, `To`, `Paid For`, `Price`.
- 🔴 **Failed TX** → Extracts only the essentials (`Time`, `Action`, `From`, `To`).
- ⚠️ **Invalid Hash** → Clean error message when the transaction address is not valid.
- 🧾 **Auto JSON Print** → Prints a formatted JSON result **and** returns it as a Python `dict`.


## 💬 Help & Support .
- Follow updates via the **[Telegram Channel](https://t.me/Pycodz)**.
- For general questions and help, join our **[Telegram chat](https://t.me/PyChTz)**.


