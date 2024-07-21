def info(airplane):
    if airplane == 'B737':
        capacity = '189'
        price = '300'
    elif airplane == 'B757':
        capacity = '289'
        price = '450'
    elif airplane == 'B747':
        capacity = '550'
        price = '700'
    elif airplane == 'A310':
        capacity = '220'
        price = '350'
    elif airplane == 'A320':
        capacity = '150'
        price = '270'
    elif airplane == 'A350':
        capacity = '440'
        price = '610'
    elif airplane == 'A380':
        capacity = '835'
        price = '950'
    elif airplane == 'MD80':
        capacity = '172'
        price = '290'
    elif airplane == 'F100':
        capacity = '122'
        price = '250'
    elif airplane == 'BA146':
        capacity = '112'
        price = '230'
    elif airplane == 'ATR172':
        capacity = '75'
        price = '150'
    else:
        capacity = '143'
        price = '260'
    return capacity, price
