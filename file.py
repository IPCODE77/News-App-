# Get All Updated news using python request module
import requests
import time

message = 'Hey, Readers welcome to THE INDEPENDENT BHARAT \n You can read all type of news here \n Press 1 -- Business \n Press 2 -- Entertainment \n Press 3 -- General \n Press 4 -- Health \n Press 5 -- science \n Press 6 -- Sports \n Press 7-- Techonology \n'

for i in range(len(message)):
    time.sleep(0.02)
    print(message[i], end="")

user_input = int(input('Enter Your Choice: '))


def shownews(country='in'):
    response = requests.get(
        f'https://newsapi.org/v2/top-headlines/sources?country={country}&apiKey=d9fa043f7f074395bcbf48cfacb704ff').json()
    desc = response['sources']
    print('******Top Headlines On Today******')
    for index, item in enumerate(desc):
        time.sleep(0.01)
        print(f'{index+1} ' + item['description'])
        print('\n')
shownews()


try:
    def showall_type_news(category):
        response_json = requests.get(
            f'https://newsapi.org/v2/top-headlines/sources?category={category}&apiKey=d9fa043f7f074395bcbf48cfacb704ff').json()
        articles = response_json['sources']
        print(f"***** Top Headlines On {category} *****")
        for arr in articles:
            print(arr['description'])
            print('\n')

except:
    print('Something Went Wrong ! Please try After Some Time')

if user_input == 1:
    showall_type_news('business')
elif user_input == 2:
    showall_type_news('entertainment')
elif user_input == 3:
    showall_type_news('general')
elif user_input == 4:
    showall_type_news('health')
elif user_input == 5:
    showall_type_news('science')
elif user_input == 6:
    showall_type_news('sports')
elif user_input == 7:
    showall_type_news('technology')
else:
    print('Invalid Input')
