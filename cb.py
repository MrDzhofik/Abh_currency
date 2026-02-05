import cbrapi as cbr
from datetime import datetime

TODAY = datetime.today().strftime("%Y-%m-%d")
print(TODAY)

currencies = cbr.get_currencies_list()
metals = cbr.get_metals_prices(TODAY)

print(currencies["Vcurs"])
print(metals)
