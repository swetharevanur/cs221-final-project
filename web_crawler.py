# web_crawler.py
# Web crawler that recursively searches the entire Backpage website
# Retrieves post text, date, title, location, ID, and phone number.
# Authors: Swetha Revanur and Keanu Spies

import nltk
import urllib
from bs4 import BeautifulSoup
import re
import string
import pandas as pd
from util import stripPunctuation
from backpage_parser import * 

URLS = [ "http://losangeles.backpage.com/WomenSeekMen/323-750-8882-asian-anywhere-out-to-you-asian-sandy-hot/119134783",
		"http://losangeles.backpage.com/SportsEquipForSale/1-400-ruger-precision-in-308-win-and-6-5-creedmoor/140762717",
		"http://losangeles.backpage.com/SportsEquipForSale/home-protection-nij-level-3a-and-3-venture-ballistic-shields/96659002",
		"http://losangeles.backpage.com/TherapeuticMassage/south-american-therapist-to-your-door/92268987",
		"http://losangeles.backpage.com/AppliancesForSale/over-15-years-refrigerator-fixer-24-hrs-emergency-store-3106972751-same-day-nights-also/99071977",
		"http://losangeles.backpage.com/TherapeuticMassage/40-intoxicating-colombian-and-asian-chicks-will-oil-you-til-your-toes-curl-310-849-4388/121253938"]

tabulate(URLS)