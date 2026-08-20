def verify_card_number(card_number):
    card_number = card_number.replace('-', '').replace(' ', '')
    card_number = card_number[::-1]
    double_every_other = [int(x) * 2 - 9 if int(x) * 2 > 9 else int(x) * 2 for x in card_number[1::2]]
    not_doubled = [int(x) for x in card_number[0::2]]
    
    if sum(double_every_other + not_doubled) % 10 == 0:
        return 'VALID!'
    else:
        return 'INVALID!'