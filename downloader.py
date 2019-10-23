import requests
import validators
from instagram.client import InstagramAPI

def auth():
    auth_url = 'https://api.instagram.com/oauth/authorize/?client_id={}&redirect_uri={}&response_type=token'
    client_id = 'ce682a1184e840f191eb72ef1646ecc1'
    redirect_url = 'http://localhost'
    url = auth_url.format(client_id, redirect_url)
    
    print('Visit the following url in your browser and authorize access: \n\n' + url + '\n')
    token = input('Enter the redirected url after login: ').strip()

    while not validators.url(token):
        token = input('Enter valid url: ').strip()

    return token.split('token=')[1]
   
def main():
    token = auth()
    api = InstagramAPI(access_token=token)

    recent_media, next = api.user_recent_media()
    photos = []
    
    recent = api.

    for media in recent_media:
        # photos.append(media.images.url)
        print(media.values)


if __name__ == "__main__":
    main()
    








