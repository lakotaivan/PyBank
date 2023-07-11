def euro_u_kune(x):
  return lambda a : a * x

def kune_u_euro(x):
  return lambda a : a / x

eurkn = euro_u_kune(7.5345)
kneur = kune_u_euro(7.5345)

def usd_u_kune(x):
  return lambda a : a * x

def kune_u_usd(x):
  return lambda a : a / x

usdkn = usd_u_kune(7.03)
knusd = kune_u_usd(7.03)

def usd_u_euro(x):
  return lambda a : a * x

def euro_u_usd(x):
  return lambda a : a / x

usdeur = usd_u_euro(1.07)
eurusd = euro_u_usd(1.07)


# valuta1 = str(input("Odaberite valutu koju imate (EUR, KN, USD): "))
# valuta2 = str(input("Odaberite valutu u koju želite konvertirati (EUR, KN, USD): "))

# if valuta1.upper() == "EUR" and valuta2.upper() == "KN" :
#   e = float(input("Iznos u eurima: "))
#   print("Iznos u kunama: " + str(eurkn(e)) + " Kn")

# elif valuta1.upper() == "KN" and valuta2.upper() == "EUR" :
#   k = float(input("Iznos u kunama: "))
#   print("Iznos u eurima: " + str(kneur(k)) + " EUR")


# elif valuta1.upper() == "USD" and valuta2.upper() == "KN" :
#   usd = float(input("Iznos u dolarima: "))
#   print("Iznos u kunama: " + str(usdkn(usd)) + " KN")

# elif valuta1.upper() == "KN" and valuta2.upper() == "USD" :
#   k = float(input("Iznos u kunama: "))
#   print("Iznos u dolarima: " + str(knusd(k)) + " USD")


# elif valuta1.upper() == "USD" and valuta2.upper() == "EUR" :
#   usd = float(input("Iznos u dolarima: "))
#   print("Iznos u eurima: " + str(usdeur(usd)) + " EUR")

# elif valuta1.upper() == "EUR" and valuta2.upper() == "USD" :
#   e = float(input("Iznos u eurima: "))
#   print("Iznos u dolarima: " + str(eurusd(e)) + " USD")

# else :
#   print("Pogreška pri unosu!")