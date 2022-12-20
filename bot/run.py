from booking.bookings import Booking
import time

with Booking() as bot:
    bot.land_first_page()
    bot.change_currency(currency='USD')
    bot.select_place_to_go("New York")
    bot.select_dates(check_in='2022-12-24', check_out='2023-01-05')
    bot.select_adults(10)
    print('exiting...')
time.sleep(45)