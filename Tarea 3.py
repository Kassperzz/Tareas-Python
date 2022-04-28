print('LOGIN:')

user1 = 'raul_1'
pw1 = 's1d3'
user2 = 'xXdD'
pw2 = 'mmaa'
user3 = 'duoc'
pw3 = 'aea'
user4 = 'Lucy'
pw4 = 'mugi'

connection = False

while connection == False :
    user = input('User: ')
    pw = input('Password: ')
    if user == user1:
        if pw == pw1:
            connection = True
    if user == user2:
        if pw == pw2:
            connection = True
    if user == user3:
        if pw == pw3:
            connection = True
    if user == user4:
        if pw == pw4:
            connection = True
    if connection == False:
        print('login error')
           
print('login success!')