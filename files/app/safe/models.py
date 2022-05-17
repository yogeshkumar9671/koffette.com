from email.policy import default
from itertools import product
from msilib.schema import Media
from multiprocessing.sharedctypes import Value
from pydoc import describe
from sre_parse import CATEGORIES
from statistics import mode
from tkinter import Widget
from unicodedata import category, name
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxLengthValidator, MinLengthValidator

# Create your models here.



countries = (('AF', 'AFGHANISTAN'),('AL', 'ALBANIA'),('DZ', 'ALGERIA'),('AS', 'AMERICAN SAMOA'),('AD', 'ANDORRA'),('AO', 'ANGOLA'),('AI', 'ANGUILLA'),('AQ', 'ANTARCTICA'),('AG', 'ANTIGUA AND BARBUDA'),('AR', 'ARGENTINA'),('AM', 'ARMENIA'),('AW', 'ARUBA'),('AU', 'AUSTRALIA'),('AT', 'AUSTRIA'),('AZ', 'AZERBAIJAN'),('BS', 'BAHAMAS'),('BH', 'BAHRAIN'),('BD', 'BANGLADESH'),('BB', 'BARBADOS'),('BY', 'BELARUS'),('BE', 'BELGIUM'),('BZ', 'BELIZE'),('BJ', 'BENIN'),('BM', 'BERMUDA'),('BT', 'BHUTAN'),('BO', 'BOLIVIA'),('BA', 'BOSNIA AND HERZEGOVINA'),('BW', 'BOTSWANA'),('BV', 'BOUVET ISLAND'),('BR', 'BRAZIL'),('IO', 'BRITISH INDIAN OCEAN TERRITORY'),('BN', 'BRUNEI DARUSSALAM'),('BG', 'BULGARIA'),('BF', 'BURKINA FASO'),('BI', 'BURUNDI'),('KH', 'CAMBODIA'),('CM', 'CAMEROON'),('CA', 'CANADA'),('CV', 'CAPE VERDE'),('KY', 'CAYMAN ISLANDS'),('CF', 'CENTRAL AFRICAN REPUBLIC'),('TD', 'CHAD'),('CL', 'CHILE'),('CN', 'CHINA'),('CX', 'CHRISTMAS ISLAND'),('CC', 'COCOS (KEELING) ISLANDS'),('CO', 'COLOMBIA'),('KM', 'COMOROS'),('CG', 'CONGO'),('CD', 'CONGO, THE DEMOCRATIC REPUBLIC OF'),('CK', 'COOK ISLANDS'),('CR', 'COSTA RICA'),('CI', "CÃ”TE D'IVOIRE"),('HR', 'CROATIA'),('CU', 'CUBA'),('CY', 'CYPRUS'),('CZ', 'CZECH REPUBLIC'),('DK', 'DENMARK'),('DJ', 'DJIBOUTI'),('DM', 'DOMINICA'),('DO', 'DOMINICAN REPUBLIC'),('EC', 'ECUADOR'),('EG', 'EGYPT'),('SV', 'EL SALVADOR'),('GQ', 'EQUATORIAL GUINEA'),('ER', 'ERITREA'),('EE', 'ESTONIA'),('ET', 'ETHIOPIA'),('FK', 'FALKLAND ISLANDS (MALVINAS)'),('FO', 'FAROE ISLANDS'),('FJ', 'FIJI'),('FI', 'FINLAND'),('FR', 'FRANCE'),('GF', 'FRENCH GUIANA'),('PF', 'FRENCH POLYNESIA'),('TF', 'FRENCH SOUTHERN TERRITORIES'),('GA', 'GABON'),('GM', 'GAMBIA'),('GE', 'GEORGIA'),('DE', 'GERMANY'),('GH', 'GHANA'),('GI', 'GIBRALTAR'),('GR', 'GREECE'),('GL', 'GREENLAND'),('GD', 'GRENADA'),('GP', 'GUADELOUPE'),('GU', 'GUAM'),('GT', 'GUATEMALA'),('GN', 'GUINEA'),('GW', 'GUINEA'),('GY', 'GUYANA'),('HT', 'HAITI'),('HM', 'HEARD ISLAND AND MCDONALD ISLANDS'),('HN', 'HONDURAS'),('HK', 'HONG KONG'),('HU', 'HUNGARY'),('IS', 'ICELAND'),('IN', 'INDIA'),('ID', 'INDONESIA'),('IR', 'IRAN, ISLAMIC REPUBLIC OF'),('IQ', 'IRAQ'),('IE', 'IRELAND'),('IL', 'ISRAEL'),('IT', 'ITALY'),('JM', 'JAMAICA'),('JP', 'JAPAN'),('JO', 'JORDAN'),('KZ', 'KAZAKHSTAN'),('KE', 'KENYA'),('KI', 'KIRIBATI'),('KP', "KOREA, DEMOCRATIC PEOPLE'S REPUBLIC OF"),('KR', 'KOREA, REPUBLIC OF'),('KW', 'KUWAIT'),('KG', 'KYRGYZSTAN'),('LA', "LAO PEOPLE'S DEMOCRATIC REPUBLIC"),('LV', 'LATVIA'),('LB', 'LEBANON'),('LS', 'LESOTHO'),('LR', 'LIBERIA'),('LY', 'LIBYAN ARAB JAMAHIRIYA'),('LI', 'LIECHTENSTEIN'),('LT', 'LITHUANIA'),('LU', 'LUXEMBOURG'),('MO', 'MACAO'),('MK', 'MACEDONIA, THE FORMER YUGOSLAV REPUBLIC OF'),('MG', 'MADAGASCAR'),('MW', 'MALAWI'),('MY', 'MALAYSIA'),('MV', 'MALDIVES'),('ML', 'MALI'),('MT', 'MALTA'),('MH', 'MARSHALL ISLANDS'),('MQ', 'MARTINIQUE'),('MR', 'MAURITANIA'),('MU', 'MAURITIUS'),('YT', 'MAYOTTE'),('MX', 'MEXICO'),('FM', 'MICRONESIA, FEDERATED STATES OF'),('MD', 'MOLDOVA, REPUBLIC OF'),('MC', 'MONACO'),('MN', 'MONGOLIA'),('MS', 'MONTSERRAT'),('MA', 'MOROCCO'),('MZ', 'MOZAMBIQUE'),('MM', 'MYANMAR'),('NA', 'NAMIBIA'),('NR', 'NAURU'),('NP', 'NEPAL'),('NL', 'NETHERLANDS'),('AN', 'NETHERLANDS ANTILLES'),('NC', 'NEW CALEDONIA'),('NZ', 'NEW ZEALAND'),('NI', 'NICARAGUA'),('NE', 'NIGER'),('NG', 'NIGERIA'),('NU', 'NIUE'),('NF', 'NORFOLK ISLAND'),('MP', 'NORTHERN MARIANA ISLANDS'),('NO', 'NORWAY'),('OM', 'OMAN'),('PK', 'PAKISTAN'),('PW', 'PALAU'),('PS', 'PALESTINIAN TERRITORY, OCCUPIED'),('PA', 'PANAMA'),('PG', 'PAPUA NEW GUINEA'),('PY', 'PARAGUAY'),('PE', 'PERU'),('PH', 'PHILIPPINES'),('PN', 'PITCAIRN'),('PL', 'POLAND'),('PT', 'PORTUGAL'),('PR', 'PUERTO RICO'),('QA', 'QATAR'),('RE', 'RÃ‰UNION'),('RO', 'ROMANIA'),('RU', 'RUSSIAN FEDERATION'),('RW', 'RWANDA'),('SH', 'SAINT HELENA'),('KN', 'SAINT KITTS AND NEVIS'),('LC', 'SAINT LUCIA'),('PM', 'SAINT PIERRE AND MIQUELON'),('VC', 'SAINT VINCENT AND THE GRENADINES'),('WS', 'SAMOA'),('SM', 'SAN MARINO'),('ST', 'SAO TOME AND PRINCIPE'),('SA', 'SAUDI ARABIA'),('SN', 'SENEGAL'),('CS', 'SERBIA AND MONTENEGRO'),('SC', 'SEYCHELLES'),('SL', 'SIERRA LEONE'),('SG', 'SINGAPORE'),('SK', 'SLOVAKIA'),('SI', 'SLOVENIA'),('SB', 'SOLOMON ISLANDS'),('SO', 'SOMALIA'),('ZA', 'SOUTH AFRICA'),('GS', 'SOUTH GEORGIA AND SOUTH SANDWICH ISLANDS'),('ES', 'SPAIN'),('LK', 'SRI LANKA'),('SD', 'SUDAN'),('SR', 'SURINAME'),('SJ', 'SVALBARD AND JAN MAYEN'),('SZ', 'SWAZILAND'),('SE', 'SWEDEN'),('CH', 'SWITZERLAND'),('SY', 'SYRIAN ARAB REPUBLIC'),('TW', 'TAIWAN, PROVINCE OF CHINA'),('TJ', 'TAJIKISTAN'),('TZ', 'TANZANIA, UNITED REPUBLIC OF'),('TH', 'THAILAND'),('TL', 'TIMOR'),('TG', 'TOGO'),('TK', 'TOKELAU'),('TO', 'TONGA'),('TT', 'TRINIDAD AND TOBAGO'),('TN', 'TUNISIA'),('TR', 'TURKEY'),('TM', 'TURKMENISTAN'),('TC', 'TURKS AND CAICOS ISLANDS'),('TV', 'TUVALU'),('UG', 'UGANDA'),('UA', 'UKRAINE'),('AE', 'UNITED ARAB EMIRATES'),('GB', 'UNITED KINGDOM'),('US', 'UNITED STATES'),('UM', 'UNITED STATES MINOR OUTLYING ISLANDS'),('UY', 'URUGUAY'),('UZ', 'UZBEKISTAN'),('VU', 'VANUATU'),('VN', 'VIET NAM'),('VG', 'VIRGIN ISLANDS, BRITISH'),('VI', 'VIRGIN ISLANDS, U.S.'),('WF', 'WALLIS AND FUTUNA'),('EH', 'WESTERN SAHARA'),('YE', 'YEMEN'),('ZW', 'ZIMBABWE')
)

state = (("AN","Andaman and Nicobar Islands"),("AP","Andhra Pradesh"),("AR","Arunachal Pradesh"),("AS","Assam"),("BR","Bihar"),("CG","Chhattisgarh"),("CH","Chandigarh"),("DN","Dadra and Nagar Haveli"),("DD","Daman and Diu"),("DL","Delhi"),("GA","Goa"),("GJ","Gujarat"),("HR","Haryana"),("HP","Himachal Pradesh"),("JK","Jammu and Kashmir"),("JH","Jharkhand"),("KA","Karnataka"),("KL","Kerala"),("LA","Ladakh"),("LD","Lakshadweep"),("MP","Madhya Pradesh"),("MH","Maharashtra"),("MN","Manipur"),("ML","Meghalaya"),("MZ","Mizoram"),("NL","Nagaland"),("OD","Odisha"),("PB","Punjab"),("PY","Pondicherry"),("RJ","Rajasthan"),("SK","Sikkim"),("TN","Tamil Nadu"),("TS","Telangana"),("TR","Tripura"),("UP","Uttar Pradesh"),("UK","Uttarakhand"),("WB","West Bengal")
) 



class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    state = models.CharField(choices=state, max_length=50)
    pincode = models.IntegerField()

    def __str__(self):
        return str(self.id)

category = (
    ('TW',"Top Wear"),
    ('BW',"Bottom Wear"),
    ('S',"Shoes"),
    ('BEA',"Beauty Product"),
    ('CO',"Coffee"),
    ('GRO',"Grocery"),
    ('Acce',"Accessories"),
) 


# Fcategory = (
#     ('S',"Shoes"),
#     ('clo', "Clothes"),
#     ('BEA',"Beauty Product"),
#     ('CO',"Coffee"),
#     ('GRO',"Grocery"),
#     ('Acce',"Accessories"),
# )


# Tsub_category = (
#     ('wat',"Watch"),
#     ('shir',"Shirt"),
#     ('tshir',"T-Shirt"),
#     ('jack',"Jacket"),
# )
# Bsub_category = (
#     ('sh',"Shoes"),
#     ('jean',"Jeans"),
#     ('trou',"Trouser"),
#     ('belt ',"Belts "),
# )


class Product(models.Model):
    category = models.CharField(choices=category, max_length=5)
    brand_name = models.CharField(max_length=100)
    product_title = models.CharField(max_length=100)
    product_discription = models.TextField()
    selling_price = models.FloatField()
    actual_price = models.FloatField()
    img = models.ImageField(upload_to="productImg", null=True, editable=True,)
    img2 = models.ImageField(upload_to="productImg", blank=True, null=True, editable=True,)
    img3 = models.ImageField(upload_to="productImg", blank=True, null=True)
    img4 = models.ImageField(upload_to="productImg", blank=True, null=True)

    def Calculate_Offer(self):
        off = (self.actual_price-self.selling_price)/self.actual_price
        offer = int(off*100)
        return offer

    def __str__(self):
        return str(self.brand_name)


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    
    def __str__(self):
        return str(self.product)
    

STATUS_CHOICES = (
    ('Accepted', 'Accepted'),
    ('Packed', 'Packed'),
    ('On The Way', 'On The Way'),
    ('Deliverd', 'Deliverd'),
    ('Cancel', 'Cancel'),
)

class OrderPlaced(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=STATUS_CHOICES,max_length=50, default="Pending")