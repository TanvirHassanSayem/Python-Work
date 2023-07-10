import re



txt = "The rain@in.Spain ai me ai "

# x2=txt.split('@')
# print(x2)
x = re.findall('^The .*@([^ ]*)', txt)


print(x)


# y1= x[2]

# print(y1)

