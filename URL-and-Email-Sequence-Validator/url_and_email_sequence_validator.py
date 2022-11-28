import re

with open('input.txt') as t:

        text = t.read().split()

print("\nEmail and URL Validator: \n")

for i in range(len(text)):

    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

    url_pattern1 = "((http|https)://)[-a-zA-Z0-9:%._\\+~#?&//=]{2,256}\\.[a-z]{2,6}\\b([-a-zA-Z0-9:%._\\+~#?&//=]*)$"

    url_pattern2 = "[-a-zA-Z0-9:%._\\+~#?&//=]{2,256}\\.[a-z]{2,6}\\b([-a-zA-Z0-9:%._\\+~#?&//=]*)$"

    if re.match(email_pattern,text[i]):

        print(text[i]+" is a Valid Email \n")

    elif re.match(url_pattern1,text[i]):

        print(text[i]+" is a Valid URL \n")

    elif re.match(url_pattern2,text[i]):

        print(text[i]+" is a Valid URL \n")
        
    else:

        print(text[i]+" is neither a Valid URL nor a Valid EMAIL \n")
