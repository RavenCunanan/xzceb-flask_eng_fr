
"""
French English translator for Coursera Final Project
by Raven Cunanan
"""

import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']


authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def english_to_french(englishText):

    fr_trans = language_translator.translate(
    text=englishText, model_id='en-fr' ).get_result()
    french_text = fr_trans.get("translations")[0].get("translation")

    return french_text

def french_to_english(french_text):
    en_trans = language_translator.translate(
    text=french_text, model_id='fr-en').get_result()
    english_text = en_trans("translations")[0].get("translation")
    return english_text
