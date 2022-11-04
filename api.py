def api():
    import requests
    # from pprint import pprint as print

    API_KEY = 'API_KEY here'

    currency = "USD"
    url = f'https://v6.exchangerate-api.com/v6/{API_KEY}/pair/{currency}/UZS'

    response = requests.get(url)
    jsondata = response.json()
    return jsondata['conversion_rate']

# print(api())