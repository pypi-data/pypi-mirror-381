import cloudscraper
from bs4 import BeautifulSoup
import json
import re

class Scraping:
    def __init__(self):
        self.scraper = cloudscraper.create_scraper()

    def get_tonviewer(self, wallet: str):
        url = f"https://tonviewer.com/{wallet}"

        response = self.scraper.get(url)
        details = []
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            ton = soup.find("div", {"class": "bdtytpm b1249k0b"})
            usdt = soup.find("div", class_="bdtytpm b1ai646e")
            if ton and usdt:
                details.append({
                    "Balance": ton.text.strip() + " " + usdt.text.strip()
                })
                return details
        return None

    def get_coingecko_price(self, coin: str):
        response = self.scraper.get(f"https://www.coingecko.com/en/coins/{coin}")
        soup = BeautifulSoup(response.text, "html.parser")
        if response.status_code == 200:
            try:
                price_div = soup.find("div",
                                      class_="tw-font-bold tw-text-gray-900 dark:tw-text-moon-50 tw-text-3xl md:tw-text-4xl tw-leading-10")
                if price_div:
                    span = price_div.find("span", attrs={"data-converter-target": "price"})
                    if span:
                        return span.text.strip()
            except Exception as e:
                return " Error fetching price:", e
            return None


    def get_transactions(self , wallet : str , limit: int):
        global usdt , doller
        url = f"https://tonviewer.com/{wallet}"
        response = self.scraper.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        transactions = soup.find_all("a", class_="eyh3sfr")
        data = []

        for i, tx in enumerate(transactions[:limit], start=1):

            time_tag = tx.select_one("div.bdtytpm")
            time = time_tag.get_text(strip=True) if time_tag else ""

            action_tag = tx.select_one("div.text")
            action = action_tag.get_text(strip=True) if action_tag else ""


            address_tag = tx.select_one("div.action-address")
            to = address_tag.get_text(" ", strip=True) if address_tag else ""

            payload_tag = tx.select_one("div[class*=payload]")
            if payload_tag:
                text_full = payload_tag.get_text(" ", strip=True)
                text_clean = text_full.split("#")[0].strip()
                match = re.match(r"^\d+\s+\w+(?:\s+\w+)?", text_clean)
                for_what = match.group(0) if match else text_clean
            else:
                for_what = ""
            ton_tag = tx.select_one("div[class*=transfer]")
            ton = ton_tag.get_text(strip=True) if ton_tag else ""
            abss = re.search(r"[+-]?\d+(\.\d+)?" , ton)
            if abss:
                usdt = abs(float(abss.group()))
                doller =usdt * float(self.get_coingecko_price('toncoin').split("$")[1])


            data.append({
                "Time": time,
                "Action": action,
                "From" : wallet,
                "To": to,
                "Paid For": for_what,
                "Price": f"{ton} ≈ {doller} $",
                "Limit": str(i)
            })

        return json.dumps(data, indent=2, ensure_ascii=False)







