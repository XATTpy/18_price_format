from sys import argv


def format_price(price):
    try:
        price_num = round(float(price), 2)
    except ValueError:
        return None
    if price_num.is_integer():
        str_price = '{:,.0f}'.format(price_num).replace(',', ' ')
    else:
        str_price = '{:,}'.format(price_num).replace(',', ' ')
    return str_price


if __name__ == '__main__':
    try:
        price = argv[1]
    except IndexError:
        quit('At the input data is expected to format.')
        
    str_price = format_price(price)
    print(str_price)
