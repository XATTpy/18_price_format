from sys import argv


def format_price(price):
    if not isinstance(price, (int, float, str)):
        return None
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
        quit('A number is expected on the input.')

    str_price = format_price(price)
    print(str_price)
