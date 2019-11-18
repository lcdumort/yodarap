from bs4 import BeautifulSoup as bs
import requests

class Yoda:
    def __init__(self):
        '''
        A yoda speaker. How cool is that
        '''
        self.yoda_drawing = ''' 
      ::\`--._,'.::.`._.--'/::     
      ::::.  ` __::__ '  .::::    
      ::::::-:.`'..`'.:-::::::
      ::::::::\ `--' /::::::::
      '''

    def translate(self,sentence):
        '''
        Give a good English sentence as input.
        Returns a Yoda-sentence back.
        '''
        url = 'https://www.yodaspeak.co.uk/'
        r = requests.post(url,data = {'YodaMe':sentence})
        soup = bs(r.content,'html.parser')
        translation=soup.find('textarea',{'name':'YodaSpeak'}).text
        return translation
       

    def speak(self,sentence):
        translation = self.translate(sentence)
        translength = len(translation)
        box = '-'*(translength+4)
        return (box + '\n% ' + translation + ' %\n' + box + '\n\n'+ self.yoda_drawing)

        

        

if __name__=='__main__':
    yo = Yoda()
    while True:
        sentence = input('SPEAK PADAWAN: ')
        print(yo.speak(sentence) )
    
