import requests

def get_exchange_rate(start_date, end_date, valcode="usd"):
    url = f"https://bank.gov.ua/NBU_Exchange/exchange_site?start={start_date}&end={end_date}&valcode={valcode}&sort=exchangedate&order=desc&json" 
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    elif response.status_code == 404:
        print("Дані з технично причини не отримані")
        return None
    else:
        print("Помилка отримання даних")
        return None


start_date = "20240401"
end_date = "20240405"
currency = "usd"  
data = get_exchange_rate(start_date, end_date, currency)

if data:
    for item in data:
        print(f"{item['exchangedate']}: {item['rate']} UAH за {item['units']} {item['cc']}")


# 📌 200 — це HTTP-код успішної відповіді (OK).

# 404 — не знайдено

# 500 — внутрішня помилка сервера

# 403 — заборонено