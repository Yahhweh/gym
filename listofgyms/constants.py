

SPECIALIZATIONS = [
    (0, 'Strength Training'),
    (1, 'Yoga & Flexibility'),
    (2, 'Cardio & Endurance'),
    (3, 'CrossFit'),
    (4, 'Bodybuilding'),
    (5, 'Rehabilitation & Injury Recovery'),
    (6, 'Personal Nutrition Coaching'),
]

PRODUCT_CHOICES = [
    ('client', 'Client'),
    ('trainer', 'Trainer'),
    ('gym', 'Gym'),
]

SPECIALIZATION_RATE = [
    25,
    20,
    22,
    30,
    28,
    35,
    27,
]

LOCATIONS = [
    ( 0, 'River Mall', '50.405128399999995', '30.612249700000003'),
    ( 1, 'ТРЦ Gulliver', '50.438727899999996', '30.523172600000002'),
    ( 2, 'Retroville', '50.5035509', '30.416455499999994'),
    ( 3, 'Ocean Plaza', '50.412413199999996', '30.522305499999998'),
    ( 4, 'SkyMall', '50.493613200000006', '30.560226699999994'),
    ( 5, 'Blockbuster Mall', '50.487306499999995', '30.521151699999997'),
    ( 6, 'Prospekt Mall', '50.454733999999995', '30.635592000000003'),
    ( 7, 'Cosmo Multimall', '50.449761099999996', '30.441360099999997'),
    ( 8, 'Karavan', '50.5050676', '30.471980100000003'),
    ( 9, 'Epicenter', '50.3769753', '30.444863'),
    ( 10, 'ЕПІЦЕНТР', '50.5201796', '30.479722499999998'),
    ( 11, 'Epitsentr K', '50.489839499999995', '30.4868905'),
    ( 12, 'DREAM berry', '50.5166513', '30.498698299999997'),
    ( 13, 'Gorodok Shopping Mall', '50.489934000000005', '30.4951873'),
    ( 14, 'Silver Breeze', '50.428699699999996', '30.593380399999997'),
    ( 15, 'Darynok', '50.4614376', '30.642801899999995'),
    ( 16, 'DREAM yellow', '50.507352499999996', '30.4984281'),
    ( 17, 'Ukraina Shopping Mall', '50.4463352', '30.491924999999995'),
    ( 18, 'ТРЦ “РайON”', '50.5165176', '30.602009599999995'),
    ( 19, 'Epitsentr', '50.4200464', '30.5945101'),
]

CENTER_LONG = 30.5234
CENTER_LAT = 50.4501

MAX_PRICE = 3000
MIN_PRICE = 500
MAX_RADIUS = 10

STATUS_CHOICES = [
    ('pending', 'Pending'),
    ('paid', 'Paid'),
    ('active', 'Active'),
    ('completed', 'Completed'),
    ('canceled', 'Canceled'),
]