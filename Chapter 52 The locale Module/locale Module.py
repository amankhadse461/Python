import locale
locale.setlocale(locale.LC_ALL, '')

print(locale.currency(762559748.49))

print(locale.currency(762559748.49, grouping=True))


