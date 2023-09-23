import random
print("Guess the capital of the country!")
Cont_Capital = {'Kosovo':'Prishtina','France':'Paris','England':'London','Italy':'Rome','Greece':'Athens','Germany':'Berlin','Albania':'Tirana','Egypt':'Cario',
                'Finland':'Helsinki','Hungary':'Budapest','India':'New Delhi','Ireland':'Dublin','Japan':'Tokyo','Malta':'Valleta','Netherlands':'Amsterdam'}

random_countries = random.choice(list(Cont_Capital.keys()))
print('Guess the capital')
while True:
    user_input = input(f'The country is {random_countries} write down the capital of it:\n')
    user_input = user_input.title()
    if user_input in Cont_Capital.values():
        print('You are correct!')
        break
    else:
        print('You are wrong. Try again.')