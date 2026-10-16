# Sunday titles by (liturgical_cycle, week).
SUNDAY_TITLES = {
    ('advent', 0): 'Last Sunday after Pentecost',
    ('advent', 1): 'First Sunday of Advent',
    ('advent', 2): 'Second Sunday of Advent',
    ('advent', 3): 'Third Sunday of Advent',
    ('advent', 4): 'Fourth Sunday of Advent',

    ('christmas', 0): 'Christmas',
    ('christmas', 1): 'First Sunday after Christmas Day',
    ('christmas', 2): 'Second Sunday after Christmas Day',

    ('epiphany', 0): 'Epiphany',
    ('epiphany', 1): 'First Sunday after the Epiphany',
    ('epiphany', 2): 'Second Sunday after the Epiphany',
    ('epiphany', 3): 'Third Sunday after the Epiphany',
    ('epiphany', 4): 'Fourth Sunday after the Epiphany',
    ('epiphany', 5): 'Fifth Sunday after the Epiphany',
    ('epiphany', 6): 'Sixth Sunday after the Epiphany',
    ('epiphany', 7): 'Seventh Sunday after the Epiphany',
    ('epiphany', 8): 'Eighth Sunday after the Epiphany',

    # Since Lent is defined by its distance from Easter,
    # start counting Easter cycle from last Sunday after the Epiphany
    ('easter', 0): 'Last Sunday after the Epiphany',
    ('easter', 1): 'First Sunday in Lent',
    ('easter', 2): 'Second Sunday in Lent',
    ('easter', 3): 'Third Sunday in Lent',
    ('easter', 4): 'Fourth Sunday in Lent',
    ('easter', 5): 'Fifth Sunday in Lent',
    ('easter', 6): 'Palm Sunday',
    ('easter', 7): 'Easter Day',
    ('easter', 8): 'Second Sunday of Easter',
    ('easter', 9): 'Third Sunday of Easter',
    ('easter', 10): 'Fourth Sunday of Easter',
    ('easter', 11): 'Fifth Sunday of Easter',
    ('easter', 12): 'Sixth Sunday of Easter',
    ('easter', 13): 'Seventh Sunday of Easter',
    ('easter', 14): 'Pentecost',
    ('easter', 15): 'Trinity Sunday',

    ('easter', 16): 'Second Sunday after Pentecost',
    ('easter', 17): 'Third Sunday after Pentecost',
    ('easter', 18): 'Fourth Sunday after Pentecost',
    ('easter', 19): 'Fifth Sunday after Pentecost',
    ('easter', 20): 'Sixth Sunday after Pentecost',
    ('easter', 21): 'Seventh Sunday after Pentecost',
    ('easter', 22): 'Eighth Sunday after Pentecost',
    ('easter', 23): 'Ninth Sunday after Pentecost',
    ('easter', 24): 'Tenth Sunday after Pentecost',
    ('easter', 25): 'Eleventh Sunday after Pentecost',
    ('easter', 26): 'Twelfth Sunday after Pentecost',
    ('easter', 27): 'Thirteenth Sunday after Pentecost',
    ('easter', 28): 'Fourteenth Sunday after Pentecost',
    ('easter', 29): 'Fifteenth Sunday after Pentecost',
    ('easter', 30): 'Sixteenth Sunday after Pentecost',
    ('easter', 31): 'Seventeenth Sunday after Pentecost',
    ('easter', 32): 'Eighteenth Sunday after Pentecost',
    ('easter', 33): 'Nineteenth Sunday after Pentecost',
    ('easter', 34): 'Twentieth Sunday after Pentecost',
    ('easter', 35): 'Twenty-First Sunday after Pentecost',
    ('easter', 36): 'Twenty-Second Sunday after Pentecost',
    ('easter', 37): 'Twenty-Third Sunday after Pentecost',
    ('easter', 38): 'Twenty-Fourth Sunday after Pentecost',
    ('easter', 39): 'Twenty-Fifth Sunday after Pentecost',
    ('easter', 40): 'Twenty-Sixth Sunday after Pentecost',
    ('easter', 41): 'Twenty-Seventh Sunday after Pentecost',
}

WEEKDAY_NAMES = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

# Weeks whose Sunday title takes no article in weekday titles (e.g. "Friday
# after Christmas", "Wednesday after Pentecost")
OMIT_ARTICLE = {
    ('christmas', 0), ('easter', 6), ('easter', 7), ('easter', 14), ('easter', 15)}

WEEKDAY_TITLES = {
    ('easter', 6): {
        'Monday': 'Monday in Holy Week',
        'Tuesday': 'Tuesday in Holy Week',
        'Wednesday': 'Wednesday in Holy Week',
        'Thursday': 'Maundy Thursday',
        'Friday': 'Good Friday',
        'Saturday': 'Holy Saturday'
    },
    ('easter', 7): {
        'Monday': 'Monday in Easter Week',
        'Tuesday': 'Tuesday in Easter Week',
        'Wednesday': 'Wednesday in Easter Week',
        'Thursday': 'Thursday in Easter Week',
        'Friday': 'Friday in Easter Week',
        'Saturday': 'Saturday in Easter Week'
    },
    ('easter', 12): {
        'Monday': 'Monday after the Sixth Sunday of Easter: Rogation Day',
        'Tuesday': 'Tuesday after the Sixth Sunday of Easter: Rogation Day',
        'Wednesday': 'Wednesday after the Sixth Sunday of Easter: Rogation Day'
    },
    ('easter', 0): {
        'Thursday': 'Thursday after Ash Wednesday',
        'Friday': 'Friday after Ash Wednesday',
        'Saturday': 'Saturday after Ash Wednesday'
    },
}

# The named Holy Days which fall on weekdays, by (month, day).
HOLY_DAY_TITLES = {
    (1, 1): 'The Holy Name of Our Lord Jesus Christ',
    (1, 18): 'The Confession of Saint Peter the Apostle',
    (1, 25): 'The Conversion of Saint Paul the Apostle',
    (2, 2): 'The Presentation of Our Lord Jesus Christ in the Temple',
    (2, 24): 'Saint Matthias the Apostle',
    (3, 19): 'Saint Joseph',
    (3, 25): 'The Annunciation of Our Lord Jesus Christ to the Blessed Virgin Mary',
    (4, 25): 'Saint Mark the Evangelist',
    (5, 1): 'Saint Philip and Saint James, Apostles',
    (5, 31): 'The Visitation of the Blessed Virgin Mary',
    (6, 11): 'Saint Barnabas the Apostle',
    (6, 24): 'The Nativity of Saint John the Baptist',
    (6, 29): 'Saint Peter and Saint Paul, Apostles',
    (7, 4): 'Independence Day',
    (7, 22): 'Saint Mary Magdalene',
    (7, 25): 'Saint James the Apostle',
    (8, 6): 'The Transfiguration of Our Lord Jesus Christ',
    (8, 15): 'Saint Mary the Virgin, Mother of Our Lord Jesus Christ',
    (8, 24): 'Saint Bartholomew the Apostle',
    (9, 14): 'Holy Cross Day',
    (9, 21): 'Saint Matthew, Apostle and Evangelist',
    (9, 29): 'Saint Michael and All Angels',
    (10, 18): 'Saint Luke the Evangelist',
    (10, 23): 'Saint James of Jerusalem, Brother of Our Lord Jesus Christ, and Martyr',
    (10, 28): 'Saint Simon and Saint Jude, Apostles',
    (11, 1): "All Saints' Day",
    (11, 30): 'Saint Andrew the Apostle',
    (12, 21): 'Saint Thomas the Apostle',
    (12, 26): 'Feast of St. Stephen',
    (12, 27): 'Feast of St. John',
    (12, 28): 'Holy Innocents',
    (12, 25): 'The Nativity of Our Lord Jesus Christ',
    (1, 6): 'The Epiphany',
}