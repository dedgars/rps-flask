from random import choice
from termcolor import cprint
import pyinputplus as pyip
from colorama import init
init()

hangman = ['''
 +---+
     |
     |
     | 
    === ''', '''
 +---+
 O   |
     |
     | 
    === ''', '''
 +---+
 O   |
 |   |
     | 
    === ''', '''
 +---+
 O   |
/|   |
     | 
    === ''', '''
 +---+
 O   |
/|\  |
     | 
    === ''', '''
 +---+
 O   |
/|\  |
/    | 
    === ''', '''
 +---+
 O   |
/|\  |
/ \  | 
    === ''']
wordbase = ['Aruba', 'Afghanistan', 'Angola', 'Anguilla', 'Aland Islands', 'Albania', 'Andorra', 'United Arab Emirates', 'Argentina', 'Armenia', 'American Samoa', 'Antarctica', 'French Southern Territories', 'Antigua and Barbuda', 'Australia', 'Austria', 'Azerbaijan', 'Burundi', 'Belgium', 'Benin', 'Burkina Faso', 'Bangladesh', 'Bulgaria', 'Bahrain', 'Bahamas', 'Bosnia and Herzegovina', 'Belarus', 'Belize', 'Bermuda', 'Bolivia', 'Brazil', 'Barbados', 'Brunei', 'Bhutan', 'Botswana', 'Central African Republic', 'Canada', 'Cocos Islands', 'Switzerland', 'Chile', 'China', 'Cameroon', 'The Democratic Republic of the Congo', 'Congo', 'Cook Islands', 'Colombia', 'Comoros', 'Cabo Verde', 'Costa Rica', 'Cuba', 'Cayman Islands', 'Cyprus', 'Czechia', 'Germany', 'Djibouti', 'Dominica', 'Denmark', 'Dominican Republic', 'Algeria', 'Ecuador', 'Egypt', 'Eritrea', 'Western Sahara', 'Spain', 'Estonia', 'Ethiopia', 'Finland', 'Fiji', 'Falkland Islands', 'France', 'Faroe Islands', 'Micronesia', 'Gabon', 'United Kingdom', 'Georgia', 'Guernsey', 'Ghana', 'Gibraltar', 'Guinea', 'Guadeloupe', 'Gambia', 'Guinea Bissau', 'Equatorial Guinea', 'Greece', 'Grenada', 'Greenland', 'Guatemala', 'French Guiana', 'Guam', 'Guyana', 'Hong Kong', 'Honduras', 'Croatia', 'Haiti', 'Hungary', 'Indonesia', 'Isle of Man', 'India', 'Ireland', 'Iran', 'Iraq', 'Iceland', 'Israel', 'Italy', 'Jamaica', 'Jersey', 'Jordan', 'Japan', 'Kazakhstan', 'Kenya', 'Kyrgyzstan', 'Cambodia', 'Kiribati', 'Saint Kitts and Nevis', 'South Korea', 'Kuwait', 'Laos', 'Lebanon', 'Liberia', 'Libya', 'Liechtenstein', 'Sri Lanka', 'Lesotho', 'Lithuania', 'Luxembourg', 'Latvia', 'Macao', 'Morocco', 'Monaco', 'Moldova', 'Madagascar', 'Maldives', 'Mexico', 'Marshall Islands', 'North Macedonia', 'Mali', 'Malta', 'Myanmar', 'Montenegro', 'Mongolia', 'Mozambique', 'Mauritania', 'Martinique', 'Mauritius', 'Malawi', 'Malaysia', 'Mayotte', 'Namibia', 'New Caledonia', 'Niger', 'Nigeria', 'Nicaragua', 'Netherlands', 'Norway', 'Nepal', 'Nauru', 'New Zealand', 'Oman', 'Pakistan', 'Panama', 'Pitcairn', 'Peru', 'Philippines', 'Palau', 'Papua New Guinea', 'Poland', 'Puerto Rico', 'North Korea', 'Portugal', 'Paraguay', 'Palestine', 'French Polynesia', 'Qatar', 'Romania', 'Russian Federation', 'Rwanda', 'Saudi Arabia', 'Sudan', 'Senegal', 'Singapore', 'South Georgia and the South Sandwich Islands', 'Sierra Leone', 'El Salvador', 'San Marino', 'Somalia', 'Serbia', 'South Sudan', 'Sao Tome and Principe', 'Suriname', 'Slovakia', 'Slovenia', 'Sweden', 'Eswatini', 'Sint Maarten', 'Seychelles', 'Syria', 'Chad', 'Togo', 'Thailand', 'Tajikistan', 'Tokelau', 'Turkmenistan', 'Timor', 'Tonga', 'Trinidad and Tobago', 'Tunisia', 'Turkey', 'Tuvalu', 'Taiwan', 'Tanzania', 'Uganda', 'Ukraine', 'United States Minor Outlying Islands', 'Uruguay', 'United States of America', 'Uzbekistan', 'Vatican', 'Venezuela', 'Viet Nam', 'Vanuatu', 'Samoa', 'Yemen', 'South Africa', 'Zambia', 'Zimbabwe']
abc = 'abcdefghijklmnopqrstuvwxyz '


def get_letter(guesses, abc):
    while True:
        letter = input('Your guess: ').lower()
        if len(letter) != 1:
            print('Please enter a single letter! ')
        elif letter in guesses:
            print('You already tried this letter, choose another! ')
        elif letter not in abc:
            print('This character is not allowed, choose another! ')
        else:
            return letter


def another_game():
    answer = pyip.inputYesNo('Do you want to play another game? y/n: ')
    if answer == 'yes':
        game()
    else:
        quit()


def game():
    errors = 0
    guesses = []
    country = choice(wordbase)
    word = country.lower()
    cprint('H A N G M A N', 'red')
    cprint('Countries and territories', 'red')
    print('You can use following characters (space included): ', abc)
    print(len(word) * '_')

    while True:
        letter = get_letter(guesses, abc)
        guesses.append(letter)
        if letter not in word:
            errors += 1

        word_list = []

        for letter in word:
            if letter in guesses:
                word_list.append(letter)
            else:
                word_list.append('_')

        cprint(hangman[errors], 'red', attrs=['bold'])

        print('Letters used so far:', ' '.join(guesses))
        print(''.join(word_list))
        if errors == 6:
            print('You are hanging, game over.')
            cprint(f'You where unable to guess {country} :(', 'red')
            another_game()
        elif ''.join(word_list) == word:
            cprint(f'You have guessed {country} and survived! :)', 'red')
            another_game()


game()


