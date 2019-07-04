from sys import argv


def format_price(price):
    price_num = float(price)
    str_price = '{:,.0f}'.format(price_num).replace(',', ' ')
    return str_price


if __name__ == '__main__':
    str_price = argv[1]
