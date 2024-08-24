import numpy as np
import numpy_financial as npf
import matplotlib.pyplot as plt

# zalozenia

current_price = 1200000
growth_rate = 0.05
years = 5
yearly_rate = 0.12
monthly_rate = yearly_rate / 12
nper = years * 12

future_price = current_price * (1 + growth_rate) ** years 
# Cena za 5lat to 153 153.79PLN


monthly_payment = npf.pmt(monthly_rate, nper, 0, -future_price) # wplata miesieczna
# miesieczna wplata 1 875.28PLN






months = np.arange(1, nper + 1)
price_over_time = current_price * (1 + growth_rate / 12) ** months
savings_over_time = npf.fv(monthly_rate, months, -monthly_payment, 0)




plt.plot(months, price_over_time, label='Cena mieszkania')
plt.plot(months, savings_over_time, label='Wartość lokaty')
plt.legend()
plt.xlabel('Miesiące')
plt.ylabel('Złote')
plt.title('Zmiana ceny mieszkania i wartości lokaty w czasie')
plt.show()