import random




when = ['A few years ago', 'Yesterday', 'Last night', 'A long time ago','On 20th Jan']

who = ['a rabbit', 'an elephant', 'a mouse', 'a turtle','a cat']

name = ['Ali', 'Miriam','daniel', 'Hoouk', 'Starwalker']

residence = ['Barcelona','India', 'Germany', 'Venice', 'England']

went = ['cinema', 'university','seminar', 'school', 'laundry']

happened = ['made a lot of friends','Eats a burger', 'found a secret key', 'solved a mistery', 'wrote a book']

print(random.choice(when) + ', ' 
      + random.choice(who) + 
      ' that lived in ' 
      + random.choice(residence) + 
      ', went to the ' 
      + random.choice(went) + ' and ' 
      + random.choice(happened))


#OUTPUT
'''
 python teller.py
On 20th Jan, a mouse that lived in India, went to the laundry and made a lot of friends

A long time ago, a rabbit that lived in England, went to the cinema and Eats a burger

A long time ago, a rabbit that lived in England, went to the cinema and wrote a book

Last night, an elephant that lived in Germany, went to the cinema and Eats a burger

A long time ago, a mouse that lived in Venice, went to the laundry and made a lot of friends
'''
