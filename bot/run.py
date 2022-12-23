from booking.bookings import Booking
import time

#running bot from the CLI may bring some errors
#if your selenium drivers path is not set correctly
#to fix that we catch the error first then provide solution
try:
    with Booking() as bot:
        bot.land_first_page()
        bot.change_currency(currency='USD')
        bot.select_place_to_go("New York")
        bot.select_dates(check_in='2022-12-24', check_out='2023-01-05')
        bot.select_adults(10)
        bot.click_search()
        bot.filtration()
        print('exiting...')
except Exception as e:
    if 'in PATH' in str(e):
        print(
            'You are trying to run the bot from command line \n'
            'Please add to PATH your Selenium Drivers \n'
            'Windows: \n'
            '    set PATH=%PATH%;C:path-to-your-folder \n \n'
            'Linux: \n'
            '    PATH=$PATH:/path/toyour/folder/ \n'
        )
    #its not always a path problem code maybe broken
    else:
        raise
time.sleep(45)