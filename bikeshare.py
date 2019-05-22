#Project Submission for Matthew Trigger - Enjoy!
import time as t
import numpy as np
import pandas as pd

CITY_DATA = { 'chicago': 'chicago.csv',
              'nyc': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters(city, month, day):
    """ Asks user to specify a city, month, and day.
   Returns:
       (str) city - name of the city
       (str) month - name of the month
       (str) day - name of the day of week"""
    print ('Howdy! How about we explore some major US bikeshare data!')
    print ('')
    #Get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    while True:
        print ("Which city should we look at?\n")
        city = input("Chicago, NYC or Washington?\n").lower()
        if city not in ("chicago", "nyc", "washington"):
            print("\n Nice try... That's an Invalid answer! :(\n")
            continue
        else:
            break

    print("\nHow should we filter your data?\n")

    #Get user input for month (all, january, february, ... , june)
    data_filter = input("Month, day or both?\n").lower()

    while True:
        if data_filter not in ("month", "day", "both", "none"):
            print("\n Nice try... That's an Invalid answer!\n")
            data_filter = input("Month, day, both, or none?\n")
        elif data_filter == "month":
            print("Which month should we explore?\n")
            month = input("January, february, march, april, may, june or all?\n").lower()
            day = 'all'
            while True:
                if month not in ['january', 'february', 'march', 'april', 'may', 'june', 'all']:
                    print("\n Nice try... That's an Invalid answer!\n")
                    month = input("January, february, march, april, may, june or all?\n").lower()
                else:
                    break
            break
        elif data_filter == "day":
            print("Which day should we explore?\n")
            day = input("Monday, tuesday, wednesday, thursday, friday, saturday, sunday or all?\n").lower()
            month = 'all'
            while True:
                if day not in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']:
                    print("\n Nice try... That's an Invalid answer!\n")
                    day = input("Monday, tuesday, wednesday, thursday, friday, saturday, sunday or all?\n").lower()
                else:
                    break
            break
        elif data_filter == "both":
            print("Which month should we explore?\n")
            month = input("January, february, march, april, may, june or all?\n").lower()
            while True:
                if month not in ['january', 'february', 'march', 'april', 'may', 'june', 'all']:
                    print("\nNice try... That's an Invalid answer!\n")
                    month = input("January, february, march, april, may, june or all?\n").lower()
                else:
                    break

            print("Which day should we explore?\n")
            day = input("Monday, tuesday, wednesday, thursday, friday, saturday, sunday or all?\n").lower()
            while True:
                if day not in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']:
                    print("\nNice try... That's an Invalid answer!\n")
                    day = input("Monday, tuesday, wednesday, thursday, friday, saturday, sunday or all?\n").lower()
                else:
                    break
            break

    print('Thank you for your patience :)')

    print("You Chose  ", city)
    print("You Chose  ", month)
    print("You Chose  ", day)
    return city, month, day

def load_data(city, month, day):
    """Loads data that the user specified under the filters they selected.
   Arguments:
       (str) city - name of the chosen city
       (str) month - name of the chosen month
       (str) day - name of chosen day
   Returns:
       df - Pandas DataFrame the filtered city data"""

    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        #filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on peak travel times."""

    start_time = t.time()

    print('\nCalculating Peak Travel Times...\n')
    print('')

    #display the most common month
    df['month'] = df['Start Time'].dt.month
    common_month = df['month'].mode()[0]

    print('Most Common Month:', common_month)
    print('')

    #display the most common day of week
    df['week'] = df['Start Time'].dt.week
    common_week = df['week'].mode()[0]

    print('Most Common day of week:', common_week)
    print('')

    #display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]

    print('Most Common Start Hour:', common_hour)
    print('')

def station_stats(df):
    """Displays statistics on the most used stations and common trips."""

    print('\nCalculating That City\'s Favorite Stations and Trips...\n')
    print('')
    start_time = t.time()

    #display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]

    print('Favorite Start Station:', common_start_station)
    print('')

    #display most commonly used end station
    common_end_station = df['End Station'].mode()[0]

    print('Favorite End Station:', common_end_station)
    print('')

    #display most frequent combination of start station and end station trip
    df['combo'] = df['Start Station'] + ' to ' + df['End Station']
    common_station_combo = df['combo'].mode()[0]

    print('Most Common Combination:', common_station_combo)
    print('')

def trip_duration_stats(df):
    """Displays statistics for total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = t.time()

    #display total travel time
    total_travel_time = df['Trip Duration'].sum()

    print('Total Travel Time:', total_travel_time)
    print('')

    #display mean travel time
    average = df['Trip Duration'].mean()

    print('Mean/Average Travel Time:', average)
    print('')

def user_stats(df):
    """Displays statistics on those who use bikeshare."""

    print('\nCreating a picture of our Users...\n')
    start_time = t.time()

    #Display counts of user types
    user_types = df['User Type'].value_counts()
    print('Counts of user types:', user_types)
    print('')

    #Display counts of gender
    if 'Gender' in df:
        gender = df['Gender'].value_counts()
        print('Counts of gender:', gender)
        print('')
    else:
        print("Sorry, if you would like to see gender data please filter by Chicago or New York City.")

    #Display earliest, most recent, and most common year of birth
    if 'Birth_Year' in df:
        earliest_birth_year = df['Birth_Year'].min()
        print('Earliest Birth Year:', earliest_birth_year)
        print('')
        recent_birth_year = df['Birth Year'].max()

        print('Recent Birth Year:', recent_birth_year)
        print('')

        common_birth_year = df['Birth Year'].mode()[0]
        print('Most Popular Birth Year:', common_birth_year)
        print('')
    else:
        print("Sorry, if you would like to see gender data please filter by Chicago or New York City.")

def data(df):
    """ Shows the user 5 rows of raw data."""
    line_number = 0
    print("\nDo you want to see some juicy raw data?\n")
    answer = input("Yes or no?\n").lower()
    if answer not in ['yes', 'no']:
        print("\n Nice try... That's an Invalid answer! \n")
        answer = input("Yes or no?\n").lower()
    elif answer == 'yes':
        while True:
            line_number += 5
            print(df.iloc[line_number : line_number + 5])
            print("\nDo you want to see EVEN MORE juicy raw data?\n")
            continues = input("Yes or no?\n").strip().lower()
            if continues == 'no':
                break
    elif answer == 'no':
        return

def main():
    city = ""
    month = 0
    day = 0

    while True:
        city, month, day = get_filters(city, month, day)
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        data(df)

        restart = input('\nThat was fun! Would you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
    main()
