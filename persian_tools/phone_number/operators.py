OPERATORS = {
    'ShatelMobile': 'شاتل موبایل',
    'MCI': 'همراه اول',
    'Irancell': 'ایرانسل',
    'Taliya': 'تالیا',
    'RightTel': 'رایتل',
    'TeleKish': 'تله کیش',
    'ApTel': 'آپتل',
    'SamanTel': 'سامانتل',
}

IRANCELL_SAMPLE = {
    'province': [],
    'base': 'کشوری',
    'type': ['permanent', 'credit'],
    'operator': OPERATORS['Irancell'],
}

data = {
    # MCI
    '910': {
        'base': 'کشوری',
        'province': [],
        'type': ['permanent', 'credit'],
        'operator': OPERATORS['MCI'],
    },
    '911': {
        'province': ['گلستان', 'گیلان'],
        'base': 'مازندران',
        'type': ['permanent', 'credit'],
        'operator': OPERATORS['MCI'],
    },
    '912': {
        'province': ['البرز', 'زنجان', 'سمنان', 'قزوین', 'قم', 'برخی از شهرستان های استان مرکزی'],
        'base': 'تهران',
        'type': ['permanent'],
        'operator': OPERATORS['MCI'],
    },
    '913': {
        'province': ['یزد', 'چهارمحال و بختیاری', 'کرمان'],
        'base': 'اصفهان',
        'type': ['permanent', 'credit'],
        'operator': OPERATORS['MCI'],
    },
    '914': {
        'province': ['آذربایجان شرقی', 'اردبیل', 'اصفهان'],
        'base': 'آذربایجان غربی',
        'type': ['permanent', 'credit'],
        'operator': OPERATORS['MCI'],
    },
    '915': {
        'province': ['خراسان شمالی', 'خراسان جنوبی', 'سیستان و بلوچستان'],
        'base': 'خراسان رضوی',
        'type': ['permanent', 'credit'],
        'operator': OPERATORS['MCI'],
    },
    '916': {
        'province': ['لرستان', 'فارس', 'اصفهان'],
        'base': 'خوزستان',
        'type': ['permanent', 'credit'],
        'operator': OPERATORS['MCI'],
    },
    '917': {
        'province': ['بوشهر', 'کهگیلویه و بویر احمد', 'هرمزگان'],
        'base': 'فارس',
        'type': ['permanent', 'credit'],
        'operator': OPERATORS['MCI'],
    },
    '918': {
        'province': ['کردستان', 'ایلام', 'همدان'],
        'base': 'کرمانشاه',
        'type': ['permanent', 'credit'],
        'operator': OPERATORS['MCI'],
    },
    '919': {
        'province': ['البرز', 'سمنان', 'قم', 'قزوین', 'زنجان'],
        'base': 'تهران',
        'type': ['credit'],
        'operator': OPERATORS['MCI'],
    },
    '990': {
        'province': [],
        'base': 'کشوری',
        'type': ['credit'],
        'operator': OPERATORS['MCI'],
    },
    '991': {
        'province': [],
        'base': 'کشوری',
        'type': ['permanent', 'credit'],
        'operator': OPERATORS['MCI'],
    },
    '992': {
        'province': [],
        'base': 'کشوری',
        'type': ['credit'],
        'operator': OPERATORS['MCI'],
    },
    '993': {
        'province': [],
        'base': 'کشوری',
        'type': ['credit'],
        'operator': OPERATORS['MCI'],
    },
    '994': {
        'province': [],
        'base': 'کشوری',
        'type': ['credit'],
        'operator': OPERATORS['MCI'],
    },
    '995': {
        'province': [],
        'base': 'کشوری',
        'type': ['credit', 'permanent'],
        'operator': OPERATORS['MCI'],
    },
    '996': {
        'province': [],
        'base': 'کشوری',
        'type': ['credit', 'permanent'],
        'operator': OPERATORS['MCI'],
    },

    # Taliya
    '932': {
        'province': [],
        'base': 'کشوری',
        'type': ['credit'],
        'operator': OPERATORS['Taliya'],
    },

    # RightTel
    '920': {
        'province': [],
        'base': 'کشوری',
        'type': ['permanent'],
        'operator': OPERATORS['RightTel'],
    },
    '921': {
        'province': [],
        'base': 'کشوری',
        'type': ['credit'],
        'operator': OPERATORS['RightTel'],
    },
    '922': {
        'province': [],
        'base': 'کشوری',
        'type': ['credit'],
        'operator': OPERATORS['RightTel'],
    },
    '923': {
        'province': [],
        'base': 'کشوری',
        'type': ['credit'],
        'operator': OPERATORS['RightTel'],
    },

    # Irancell
    '930': IRANCELL_SAMPLE,
    '933': IRANCELL_SAMPLE,
    '935': IRANCELL_SAMPLE,
    '936': IRANCELL_SAMPLE,
    '937': IRANCELL_SAMPLE,
    '938': IRANCELL_SAMPLE,
    '939': IRANCELL_SAMPLE,
    '900': IRANCELL_SAMPLE,
    '901': IRANCELL_SAMPLE,
    '902': IRANCELL_SAMPLE,
    '903': IRANCELL_SAMPLE,
    '905': IRANCELL_SAMPLE,
    '904': {
        'province': [],
        'base': 'کشوری',
        'model': 'سیم‌کارت کودک',
        'type': ['credit'],
        'operator': OPERATORS['Irancell'],
    },
    '941': {
        'province': [],
        'base': 'کشوری',
        'model': 'TD-LTE',
        'type': ['credit'],
        'operator': OPERATORS['Irancell'],
    },

    # ShatelMobile
    '99810': {
        'province': [],
        'base': 'کشوری',
        'type': ['credit'],
        'operator': OPERATORS['ShatelMobile'],
    },
    '99811': {
        'province': [],
        'base': 'کشوری',
        'type': ['credit'],
        'operator': OPERATORS['ShatelMobile'],
    },
    '99812': {
        'province': [],
        'base': 'کشوری',
        'type': ['credit'],
        'operator': OPERATORS['ShatelMobile'],
    },
    '99813': {
        'province': [],
        'base': 'کشوری',
        'type': ['credit'],
        'operator': OPERATORS['ShatelMobile'],
    },
    '99814': {
        'province': [],
        'base': 'کشوری',
        'type': ['credit'],
        'operator': OPERATORS['ShatelMobile'],
    },
    '99815': {
        'province': [],
        'base': 'کشوری',
        'type': ['credit'],
        'operator': OPERATORS['ShatelMobile'],
    },
    '99816': {
        'province': [],
        'base': 'کشوری',
        'type': ['credit'],
        'operator': OPERATORS['ShatelMobile'],
    },
    '99817': {
        'province': [],
        'base': 'کشوری',
        'type': ['credit'],
        'operator': OPERATORS['ShatelMobile'],
    },

    # TeleKish
    '934': {
        'province': [],
        'base': 'کشوری',
        'type': ['permanent'],
        'operator': OPERATORS['TeleKish'],
    },

    # ApTel
    '99910': {
        'province': [],
        'base': 'کشوری',
        'type': ['permanent'],
        'operator': OPERATORS['ApTel'],
    },
    '99911': {
        'province': [],
        'base': 'کشوری',
        'type': ['permanent'],
        'operator': OPERATORS['ApTel'],
    },
    '99913': {
        'province': [],
        'base': 'کشوری',
        'type': ['permanent'],
        'operator': OPERATORS['ApTel'],
    },
    '99914': {
        'province': [],
        'base': 'کشوری',
        'type': ['credit'],
        'operator': OPERATORS['ApTel'],
    },

    # SamanTel
    '9999': {
        'province': [],
        'base': 'کشوری',
        'type': ['credit', 'permanent'],
        'operator': OPERATORS['SamanTel'],
    },
    '99999': {
        'province': [],
        'base': 'کشوری',
        'type': ['permanent'],
        'operator': OPERATORS['SamanTel'],
    },
}
