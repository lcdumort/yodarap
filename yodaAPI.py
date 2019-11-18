from bs4 import BeatifulSoup as bs
import requests

class Yoda:
    def __init__(self):
        '''
        A yoda speaker. How cool is that
        '''
        
    def translate_to_yoda(sentence):
        '''
        Give a good English sentence as input.
        Returns a Yoda-sentence back.
        '''
        url = 'https://www.yodaspeak.co.uk/'
        r = requests.post(url,data = {'YodaMe':sentence})
        soup = bs(r.content)
        soup.find('textarea',{'name':'YodaSpeak'}).text
        print(text)

if __name__=='__main__':
    yo = Yoda()
    Yoda('Nynke has lost a planet.')

