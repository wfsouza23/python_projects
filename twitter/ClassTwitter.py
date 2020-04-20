import oauth2
import requests
import json
import urllib

class Twitter:
    def __init__(self, consumer_key, consumer_key_secret, access_token, access_token_secret):
        self.conexao(consumer_key, consumer_key_secret, access_token, access_token_secret)

    def conexao(self, consumer_key, consumer_key_secret, access_token, access_token_secret):
        self.consumer = oauth2.Consumer(consumer_key, consumer_key_secret)
        self.token = oauth2.Token(access_token, access_token_secret)
        self.cliente = oauth2.Client(self.consumer, self.token)
    
    def tweet(self, novo_tweet):
        try:
            query_codificada = urllib.parse.quote(novo_tweet, safe='')
            requisicao = self.cliente.request('https://api.twitter.com/1.1/statuses/update.json?status=' + query_codificada, method='POST')

            decodificar = requisicao[1].decode()

            objeto = json.loads(decodificar)
            
            return objeto
        except Exception as err:
            if err == 'Request-started':
                self.tweet('Using the exception error to tweet')
            else:
                print('O erro identificado: ', err)