USER_NAMES = \
    [('Vasya', 'Pupkin'),
     ('Вася', 'Пупкин'),
     ('Вася-Dfcz', 'Пупкин-Gegrby'),
     ('Вася Dfcz', 'Пупкин Gegrby'),
     ('vasya1', 'pupkin1'),
     ('1Vasya', '1Pupkin')
     ]

USER_NAMES_SYM = \
    [('vaSya1"№№%', 'puPkin1"%:.;'),
     ('%Vasya', '&Pupkin')]


CARD_NUMBERS = \
    ['1234 5678 9101 1213',
     '1234567891011213']

# тестовые данные для негативных тестов на поле ввода номера карты (не реализовано, поскольку нет проверки на
# корректность данных)
INCORRECT_CARD_NUMBERS = \
    ['#@$%1234567891011213',
     '1234 5678 9101 12131',
     '1234 5678 9101 1213a'
     'qweerttyy',
     '1-2-3']

# payment system
PS_NAMES = \
    ['Visa',
     'MasterCard',
     'Apple Card']

PAYMENT_DATA = \
    [('1234 5678 9101 1213', 'Visa', '1'),
     ('1234567891011213', 'MasterCard', '2'),
     ('1234 5678', 'Apple Card', '3')]
