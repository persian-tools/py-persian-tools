def parsian_account_number_calculator(sheba: str) -> dict:
    sheba = sheba[14:]
    formatted = '0' + sheba[:2] + '-0' + sheba[2:9] + '-' + sheba[9:]

    return {
        'normal': sheba,
        'formatted': formatted
    }


def pasargad_account_number_calculator(sheba: str) -> dict:
    sheba = sheba[7:]
    while sheba[0] == '0':
        sheba = sheba[1:]
    sheba = sheba[:len(sheba) - 2]
    formatted = '-'.join([sheba[:3], sheba[3:6], sheba[6:14], sheba[14:]])

    return {
        'normal': sheba,
        'formatted': formatted
    }


def shahr_account_number_calculator(sheba: str) -> dict:
    sheba = sheba[7:]
    while sheba[0] == '0':
        sheba = sheba[1:]

    return {
        'normal': sheba,
        'formatted': sheba
    }


data = [
    {
        'nickname': 'central-bank',
        'name': 'Central Bank of Iran',
        'persian_name': 'بانک مرکزی ایران',
        'card_prefix': ['636797'],
        'sheba_code': ['010'],
    },
    {
        'nickname': 'sanat-o-madan',
        'name': 'Sanat O Madan Bank',
        'persian_name': 'بانک صنعت و معدن',
        'card_prefix': ['627961'],
        'sheba_code': ['011'],
    },
    {
        'nickname': 'mellat',
        'name': 'Mellat Bank',
        'persian_name': 'بانک ملت',
        'card_prefix': ['610433', '991975'],
        'sheba_code': ['012'],
    },
    {
        'nickname': 'refah',
        'name': 'Refah Bank',
        'persian_name': 'بانک رفاه کارگران',
        'card_prefix': ['589463'],
        'sheba_code': ['013'],
    },
    {
        'nickname': 'maskan',
        'name': 'Maskan Bank',
        'persian_name': 'بانک مسکن',
        'card_prefix': ['628023'],
        'sheba_code': ['014'],
    },
    {
        'nickname': 'sepah',
        'name': 'Sepah Bank',
        'persian_name': 'بانک سپه',
        'card_prefix': ['589210'],
        'sheba_code': ['015'],
    },
    {
        'nickname': 'keshavarzi',
        'name': 'Keshavarzi',
        'persian_name': 'بانک کشاورزی',
        'card_prefix': ['603770', '639217'],
        'sheba_code': ['016'],
    },
    {
        'nickname': 'melli',
        'name': 'Melli',
        'persian_name': 'بانک ملی ایران',
        'card_prefix': ['170019', '603799'],
        'sheba_code': ['017'],
    },
    {
        'nickname': 'tejarat',
        'name': 'Tejarat Bank',
        'persian_name': 'بانک تجارت',
        'card_prefix': ['585983', '627353'],
        'sheba_code': ['018'],
    },
    {
        'nickname': 'saderat',
        'name': 'Saderat Bank',
        'persian_name': 'بانک صادرات ایران',
        'card_prefix': ['603769', '903769'],
        'sheba_code': ['019'],
    },
    {
        'nickname': 'tosee-saderat',
        'name': 'Tose Saderat Bank',
        'persian_name': 'بانک توسعه صادرات',
        'card_prefix': ['207177', '627648'],
        'sheba_code': ['020'],
    },
    {
        'nickname': 'post',
        'name': 'Post Bank',
        'persian_name': 'پست بانک ایران',
        'card_prefix': ['627760'],
        'sheba_code': ['021'],
    },
    {
        'nickname': 'toose-taavon',
        'name': 'Tosee Taavon Bank',
        'persian_name': 'بانک توسعه تعاون',
        'card_prefix': ['502908'],
        'sheba_code': ['022'],
    },
    {
        'nickname': 'tosee',
        'name': 'Tosee Bank',
        'persian_name': 'موسسه اعتباری توسعه',
        'card_prefix': ['628157'],
        'sheba_code': '051',
    },
    {
        'nickname': 'ghavamin',
        'name': 'Ghavamin Bank',
        'persian_name': 'بانک قوامین',
        'card_prefix': ['639599'],
        'sheba_code': ['052'],
    },
    {
        'nickname': 'karafarin',
        'name': 'Karafarin Bank',
        'persian_name': 'بانک کارآفرین',
        'card_prefix': ['627488'],
        'sheba_code': ['053'],
    },
    {
        'nickname': 'parsian',
        'name': 'Parsian Bank',
        'persian_name': 'بانک پارسیان',
        'card_prefix': ['622106', '627884'],
        'sheba_code': ['054'],
        'account_number_calculator': parsian_account_number_calculator
    },
    {
        'nickname': 'eghtesad-novin',
        'name': 'Eghtesad Novin Bank',
        'persian_name': 'بانک اقتصاد نوین',
        'card_prefix': ['627412'],
        'sheba_code': ['055'],
    },
    {
        'nickname': 'saman',
        'name': 'Saman Bank',
        'persian_name': 'بانک سامان',
        'card_prefix': ['621986'],
        'sheba_code': ['056'],
    },
    {
        'nickname': 'pasargad',
        'name': 'Pasargad Bank',
        'persian_name': 'بانک پاسارگاد',
        'card_prefix': ['502229', '639347'],
        'sheba_code': ['057'],
        'account_number_calculator': pasargad_account_number_calculator
    },
    {
        'nickname': 'sarmayeh',
        'name': 'Sarmayeh Bank',
        'persian_name': 'بانک سرمایه',
        'card_prefix': ['639607'],
        'sheba_code': ['058'],
    },
    {
        'nickname': 'sina',
        'name': 'Sina Bank',
        'persian_name': 'بانک سینا',
        'card_prefix': ['639346'],
        'sheba_code': ['059'],
    },
    {
        'nickname': 'mehr-iran',
        'name': 'Mehr Iran Bank',
        'persian_name': 'بانک مهر ایران',
        'card_prefix': ['606373'],
        'sheba_code': ['090', '060'],
    },
    {
        'nickname': 'shahr',
        'name': 'City Bank',
        'persian_name': 'بانک شهر',
        'card_prefix': ['502806', '504706'],
        'sheba_code': ['061'],
        'account_number_calculator': shahr_account_number_calculator
    },
    {
        'nickname': 'ayandeh',
        'name': 'Ayandeh Bank',
        'persian_name': 'بانک آینده',
        'card_prefix': ['636214'],
        'sheba_code': ['062'],
    },
    {
        'nickname': 'ansar',
        'name': 'Ansar Bank',
        'persian_name': 'بانک انصار',
        'card_prefix': ['627381'],
        'sheba_code': ['063'],
    },
    {
        'nickname': 'gardeshgari',
        'name': 'Gardeshgari Bank',
        'persian_name': 'بانک گردشگری',
        'card_prefix': ['505416', '505426'],
        'sheba_code': ['064'],
    },
    {
        'nickname': 'hekmat-iranian',
        'name': 'Hekmat Iranian Bank',
        'persian_name': 'بانک حکمت ایرانیان',
        'card_prefix': ['636949'],
        'sheba_code': ['065'],
    },
    {
        'nickname': 'dey',
        'name': 'Dey Bank',
        'persian_name': 'بانک دی',
        'card_prefix': ['502938'],
        'sheba_code': ['066'],
    },
    {
        'nickname': 'iran-zamin',
        'name': 'Iran Zamin Bank',
        'persian_name': 'بانک ایران زمین',
        'card_prefix': ['505785'],
        'sheba_code': ['069'],
    },
    {
        'nickname': 'resalat',
        'name': 'Resalat Bank',
        'persian_name': 'بانک رسالت',
        'card_prefix': ['504172'],
        'sheba_code': ['070'],
    },
    {
        'nickname': 'kosar',
        'name': 'Kosar Credit Institute',
        'persian_name': 'موسسه کوثر',
        'card_prefix': ['505801'],
        'sheba_code': ['073'],
    },
    {
        'nickname': 'melal',
        'name': 'Melal Credit Institute',
        'persian_name': 'موسسه اعتباری ملل',
        'card_prefix': ['606256'],
        'sheba_code': ['075'],
    },
    {
        'nickname': 'middle-east-bank',
        'name': 'Middle East Bank',
        'persian_name': 'بانک خاورمیانه',
        'card_prefix': ['585949'],
        'sheba_code': ['078'],
    },
    {
        'nickname': 'mehr-eqtesad',
        'name': 'Mehr Eqtesad Bank',
        'persian_name': 'بانک قرض الحسنه مهر',
        'card_prefix': ['639370'],
        'sheba_code': ['079'],
    },
    {
        'nickname': 'noor-bank',
        'name': 'Noor Credit Institution',
        'persian_name': 'موسسه اعتباری نور',
        'sheba_code': ['080'],
    },
    {
        'nickname': 'iran-venezuela',
        'name': 'Iran and Venezuela Bank',
        'persian_name': 'بانک ایران و ونزوئلا',
        'sheba_code': ['095'],
    },
]
