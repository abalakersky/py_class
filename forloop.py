emails=['me@gmail.com', 'you@hotmail.com', 'they@yahoo.com']

# print(emails[1])

for email in emails:
    if 'gmail' in email:
        print(email)
    else:
        print('email is wrong')
