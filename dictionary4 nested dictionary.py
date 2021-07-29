# WAPP to demonstrate Nested Dictionary

social_media = {
    'Facebook': {
        'username': 'Jack123',
        'password': '123'
    },
    'Twitter': {
           'username': 'Jack456',
           'password': '456'
    }
}

for  u, v in social_media.items():
       print(u + " Account:")
       print("\t Username is "+v['username'])
       print("\t Password is "+v['password'])
