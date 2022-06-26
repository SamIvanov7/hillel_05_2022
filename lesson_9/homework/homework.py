import requests

#
# - Create a class `Price`
#     ```python
#         class Price:
#             def __init__(self, amount: int, currency: str) -> None:
#                 self.amount: int = amount
#                 self.currency: str = currency
#     ```
# - Acceptance criterias:
#     - If I create 2 instances of a `Price` class I want to do operations between them:
#         - add prices with same currency
#         - do a subtricttion of prices with same currency
# - *Additional: operations between prices with different currencies:
#     - If price instances currencies are different I want to do a convertion
#         - USD is a middle currency
#         - If any prices currency is USD convertion is not happening
#         - Result currency after the operation is a currency of the price that is on the left or USD (for your decision)

date = input("Enter the date in format YYYYMMDD:")


class Exchange_NBU:
    currency_name = ""
    nbu_link = ""

    def __init__(self, name: str):
        if not isinstance(name, str):
            raise Exception
        self.nbu_link = (
            f"https://bank.gov.ua/NBUStatService/v1/statdirectory/exchangenew?json / "
            f"?valcode=CAD&date={date}"
        )
        self.currency_name = name

    def check_status(self):
        res = requests.get(self.nbu_link)
        res.raise_for_status()
        print(f"statuscode: {res.status_code}")
        print(f"HEADERS: {res.headers}")

    def request_send(self):
        res = requests.get(self.nbu_link)
        j_res = res.json()
        return j_res

    def list_processing(self, lst: dict):
        my_list_4_key = []
        my_list_4_value = []
        for i in lst:
            for key, value in i.items():
                if key == "txt":
                    my_list_4_key.append(value)
                if key == "rate":
                    my_list_4_value.append(value)
        return dict(zip(my_list_4_key, my_list_4_value))

    def __str__(self):
        date_Of_request = self.request_send()[0]["exchangedate"]
        my_dict = self.list_processing(self.request_send())
        for name in my_dict:
            if name == self.currency_name:
                my_dict.get(self.currency_name)
        return f"{date_Of_request} Курс {self.currency_name} к UAH: {my_dict.get(self.currency_name)}"

    def get_our_curency(self, list_processing):
        my_dict = self.list_processing(self.request_send())
        for name in my_dict:
            if name == self.currency_name:
                fin_result = my_dict.get(self.currency_name)
        return fin_result


cur1 = Exchange_NBU("Долар США")
print(cur1)
usd_to_uah_rate = cur1.get_our_curency(cur1.request_send())


class Price:
    amount = 0.0
    currency = ""

    def __init__(self, amount: int, currency: str) -> None:
        self.amount = amount
        self.currency = currency

    def __add__(self: "Price", other: "Price"):
        instance = Price(amount=(self.amount + other.amount), currency=self.currency)
        return instance

    def __sub__(self, other: "Price") -> "Price":
        instance = Price(amount=(self.amount - other.amount), currency=self.currency)
        return instance

    def __mul__(self, other: "Price") -> "Price":
        instance = Price(amount=(self.amount * other.amount), currency=self.currency)
        return instance

    def __str__(self) -> str:
        return f"Price({self.amount}, {self.currency}, ex_rate: {usd_to_uah_rate})"

    @property
    def converted(self):
        return Price(self.amount * usd_to_uah_rate, "UAH")


if __name__ == "__main__":
    print("------------------------------")
    price_1 = Price(18000, "UAH")
    price_2 = Price(15000, "UAH")
    print(price_1)
    print(price_2)
    total_sub = price_1 - price_2
    print("------------------------------")
    print(f"Sub of prices : {total_sub}")
    print("------------------------------")

    price_3 = Price(1600, "USD")
    price_4 = Price(10000, "UAH")

    print(price_3)
    print(price_3.converted)
    print(price_4)
    print("------------------------------")
    total = price_3.converted + price_4
    print(f"Sum of prices: {total}")
