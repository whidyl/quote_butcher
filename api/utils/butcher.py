import translators as ts
from requests import get
import json
import random

languages = ['en','zh','ar','ru', 'fr', 'de', 'es', 'pt', 'it', 'ja', 'ko', 'el', 'nl', 'hi', 'tr', 'ms', 'th', 'vi', 'id', 'pl', 'mn', 'cs', 'hu', 'et', 'bg', 'da', 'fi', 'ro', 'sv', 'sl', 'fa', 'bs', 'sr', 'tl', 'ht', 'ca', 'hr', 'lv', 'lt', 'ur', 'uk', 'cy', 'sw', 'sm', 'sk', 'af', 'no', 'bn', 'mg', 'mt', 'gu', 'ta', 'te', 'pa', 'am', 'az', 'be', 'ceb', 'eo', 'eu', 'ga']
good_stacks = [['mg', 'el', 'fa', 'no', 'cy', 'da', 'fa'], ['be', 'it', 'sk', 'ht', 'sr', 'be', 'mn'], ['sl', 'te', 'da', 'pa', 'ja', 'sm', 'ur']]

def generate_butchered_quote():
    """
    Uses forismatic API to get a random quote and "butcher" it by translating it through several languages.
    """
    response = json.loads(get('http://api.forismatic.com/api/1.0/?method=getQuote&format=json&lang=en').text.replace("\\", ""))
    json_response = dict()
    json_response['quote'], json_response['author'] = response['quoteText'], response['quoteAuthor']

    text = json_response['quote']
    language_stack = random.choice(good_stacks)
    print(language_stack)
    text = multi_translate(text, language_stack)
    json_response['butchered'] = text
    return json_response

def butcher_quote(quote):
    language_stack = [random.choice(languages) for i in range(7)]
    return multi_translate(quote, language_stack)

def multi_translate(text, language_stack):
    prev_lang = 'en'
    for lang in language_stack:
        text = ts.google(text, from_language=prev_lang, to_language=lang)
        prev_lang = lang
    text = ts.google(text, from_language=prev_lang, to_language='en')
    return text

print(generate_butchered_quote())


# randomized language stack
#print(quote)
#languages = ['en','zh','ar','ru', 'fr', 'de', 'es', 'pt', 'it', 'ja', 'ko', 'el', 'nl', 'hi', 'tr', 'ms', 'th', 'vi', 'id', 'pl', 'mn', 'cs', 'hu', 'et', 'bg', 'da', 'fi', 'ro', 'sv', 'sl', 'fa', 'bs', 'sr', 'tl', 'ht', 'ca', 'hr', 'lv', 'lt', 'ur', 'uk', 'cy', 'sw', 'sm', 'sk', 'af', 'no', 'bn', 'mg', 'mt', 'gu', 'ta', 'te', 'pa', 'am', 'az', 'be', 'ceb', 'eo', 'eu', 'ga']
#language_stack = ['it', 'ar', 'zh', 'pa', 'ja', 'es', 'gu', 'en']
#language_stack = [random.choice(languages) for i in range(7)]
# ['mg', 'el', 'fa', 'no', 'cy', 'da', 'fa'] perfect
# ['be', 'it', 'sk', 'ht', 'sr', 'be', 'mn']
# ['sl', 'te', 'da', 'pa', 'ja', 'sm', 'ur']
