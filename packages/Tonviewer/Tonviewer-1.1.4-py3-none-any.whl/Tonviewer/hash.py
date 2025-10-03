from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import re
import json
import time
from typing import Optional


class HashTx:
    def __init__(self, hashtx: Optional[str] = None, html: Optional[str] = None, headless: bool = True, wait: float = 1.0):
        self.soup = None
        self.htmlcode = None

        if html:
            self.htmlcode = html
            self.soup = BeautifulSoup(html, "html.parser")

        elif hashtx:
            url = f"https://tonscan.org/tx/{hashtx}"
            opts = Options()
            if headless:
                opts.add_argument("--headless=new")
            opts.add_argument("--no-sandbox")
            opts.add_argument("--disable-dev-shm-usage")
            driver = webdriver.Chrome(options=opts)
            try:
                driver.get(url)
                time.sleep(wait)  # ندي فرصة للجافاسكربت
                self.htmlcode = driver.page_source
                self.soup = BeautifulSoup(self.htmlcode, "html.parser")
            finally:
                try:
                    driver.quit()
                except Exception:
                    pass
        else:
            raise ValueError("يجب تمرير hashtx أو html إلى HashParser")

    def text_after_label(self, soup, label: str):
        table = soup.find("table", class_="tx-details-table")
        if table:
            for tr in table.find_all("tr"):
                tds = tr.find_all(["td", "th"])
                if not tds or len(tds) < 2:
                    continue
                left = tds[0].get_text(strip=True).lower()
                if left == label.lower():
                    right = tds[1]
                    a = right.find("a")
                    if a:
                        for attr in ("data-loopa", "data-address", "data-wallet"):
                            val = a.get(attr)
                            if val:
                                return val.strip()
                        return a.get_text(strip=True)
                    return right.get_text(strip=True)
        return None

    def is_failed(self):
        if not self.soup:
            return False
        failed_el = self.soup.select_one(".tx-mobile-status__failed, .tx-mobile-overview-icon--failed")
        if failed_el:
            return True
        txt = self.soup.get_text(" ", strip=True).lower()
        if "failed transfer" in txt:
            return True
        return False

    def get(self):
        invalid_msg = "This doesn't look like a valid transaction address. Where'd you get that?"
        if self.htmlcode and invalid_msg in self.htmlcode:
            result = {"Action": invalid_msg}
            print(json.dumps(result, indent=2, ensure_ascii=False))
            return result

        if not self.soup:
            return {}

        soup = self.soup
        action_el = soup.select_one(".tx-mobile-status, .tx-mobile-status__success, .tx-mobile-status__failed, .mobile-tx-status, .tx-status")
        action = action_el.get_text(" ", strip=True) if action_el else None
        action_norm = action.strip().upper() if action else None

        from_val = self.text_after_label(soup, "from")
        to_val = self.text_after_label(soup, "to")
        if to_val and "·" in to_val:
            to_val = to_val.split("·")[0].strip()

        date_val = (
            self.text_after_label(soup, "Date")
            or self.text_after_label(soup, "Start Time")
            or self.text_after_label(soup, "Time")
        )


        if self.is_failed():
            result = {
                "Time": date_val,
                "Action": action_norm or "FAILED TRANSFER",
                "From": from_val,
                "To": to_val,
            }

            print(json.dumps(result, indent=2, ensure_ascii=False))
            return result


        paid_for_el = soup.select_one(".mobile-tx-value--message, .tx-table-payload-text, .tx-mobile-desc, .tx-payload")
        paid_for = None
        if paid_for_el:
            paid_for = paid_for_el.get_text(" ", strip=True)
            paid_for = re.split(r"Ref#|Ref\s?#", paid_for, maxsplit=1)[0].strip()

        amount = None
        for sel in (".mobile-tx-value", ".tx-amount", ".tx-value", ".mobile-tx-amount", ".tx-row-tx-event-action-badge"):
            el = soup.select_one(sel)
            if el and "TON" in el.get_text():
                amount = el.get_text(strip=True)
                break
        if not amount:
            m = re.search(r"([+-−\u2212]?\s*[\d\.,]+)\s*TON", str(soup), re.IGNORECASE)
            if m:
                amount = m.group(0).strip()

        price_str = None
        if amount:
            cleaned = amount.replace("\u2212", "-").replace("−", "-").strip()
            mnum = re.search(r"([+-]?\s*[\d\.,]+)", cleaned)
            if mnum:
                num = mnum.group(1).replace(",", "")
                price_str = f"−{num} TON" if not num.startswith("-") else f"{num} TON"
            else:
                price_str = cleaned

        result= {
            "Time": date_val,
            "Action": action_norm or "SUCCESSFUL TRANSFER",
            "From": from_val,
            "To": to_val,
            "Paid For": paid_for,
            "Price": price_str
        }



        print(json.dumps(result, indent=2, ensure_ascii=False))
        return result

