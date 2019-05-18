import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_city():
    """
    Asks user to specify a city to analyze.
    Returns:
        (str) city - name of the city to analyze
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    print('Please follow the prompts to retrieve the bikeshare data. Data is organized by city, month, and day of the week')
    city=input('What city would you like to see data for; Chicago, New York City, or Washington?: ')
    while True:
        if city == 'Chicago':
            return 'chicago'
        elif city == 'New York City':
            return 'new york city'
        elif city == 'Washington':
            return 'washington'
        elif city == 'new york city':
            return 'new york city'
        elif city == 'washington':
            return 'washington'
        elif city == 'chicago':
            return 'chicago'
        else:
            print('You did not input an eligible city, try again')
            city=input('What city would you like to see data for; Chicago, Ney York City, or Washington?: ')
            city = city.lower()
    return city

def time_view():
    """
    Asks user to specify the time frame in which to view the data
    """
    period= input("\nHow would you like to filter the city's bikeshare data? month, day of the week, or no time filter? \nPlease input month, day, or none ")
    period = period.lower()

    while True:
        if period == 'month':
            while True:
                print('\n Filtering by month')
                return 'month'

        if period == "day":
            print('\n Filtering by the day of the week')
            return 'day'
        elif period == "none":
            print('\n No time filter')
            return 'none'
        period = input("\n Please choose a filter option between 'month', 'day' of the week, or none \n")
def get_month(m):
    """
    Asks user to specify a city to analyze.
        Returns:
            (str) month - name of the month to filter by, or "all" to apply no month filter
    """
    if m == 'month':
        month = input('\nWhich month would you like to see data for; January, February, March, April, May, or June?\n')
        while month.lower() not in ['january', 'february', 'march', 'april', 'may', 'june',  'January' , 'February' , 'March' , 'April', 'May' ,'June']:
            month = input('\nPlease choose between January, February, March, April, May, or June? Please type the full month name.\n')
        return month.lower()
    else:
        return 'none'
def day_stats(d):
    """
    Asks user to specify a city to analyze.
    Returns:
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    if d == 'day':
        day = input('\nWhich day? Please type a day M, Tu, W, Th, F, Sa, Su. \n')
        while day.lower() not in ['m', 'tu', 'w', 'th', 'f', 'sa', 'su', 'M', 'Tu', 'W', 'Th', 'F', 'Sa', 'Su']:
            day = input('\nWhich day would you like to see data for; M, Tu, W, Th, F, Sa, Su?')
        return day.lower()
    else:
        return 'none'

def load_data(city):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    print('\nLoading the data\n')
    df = pd.read_csv(CITY_DATA[city])

    #extracting from Start Time
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['month'] = df['Start Time'].dt.month
    df["day_of_month"] = df["Start Time"].dt.day
    return df

def time_stats(df, time, month, week_day):
    """Displays statistics on the most frequent times of travel."""
    if time == 'month':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]


    if time == 'day_of_week':
        days = ['Monday', 'Tuesday',
        'Wednesday', 'Thursday',
        'Friday', 'Saturday', 'Sunday']
        for d in days:
            if week_day.capitalize() in d:
                day_of_week = d
        df = df[df['day_of_week'] == day_of_week]

    return df

def month_freq(df):
    """most common month"""
    print('\n * 1. Part a: What is the most popular month to use the bike share program with the current city filter?')
    m = df.month.mode()[0]
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    popular_month = months[m - 1].capitalize()
    return popular_month

def day_freq(df):
    """most common day of the week"""
    print('\n * 1. Part b: What is the most popular day of the week to use the bike share program with the current city filter?')
    return df['day_of_week'].value_counts().reset_index()['index'][0]

def hour_freq(df):
    """most common hour"""
    print('\n * 1. Part c: What is the most popular hour of the day for bike rides with the current city filter?')
    df['hour'] = df['Start Time'].dt.hour
    return df.hour.mode()[0]

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    print('\n * 2. Part a: What was the total traveling done for 2017 through June, and what was the average time spent on each trip?')
    df['End Time'] = pd.to_datetime(df['End Time'])
    df['Travel Time'] = df['End Time'] - df['Start Time']
    total_ride_time = np.sum(df['Travel Time'])
    total_days = str(total_ride_time).split()[0]

    print ("\nThe total travel time on 2017 through June was " + total_days + " days \n")
    avg_ride_time = np.mean(df['Travel Time'])
    avg_days = str(avg_ride_time).split()[0]
    print("The average travel time on 2017 through June was " + avg_days + " days \n")

    return total_ride_time, avg_ride_time

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    print("\n* 2. Part b What is the most popular start station with the current filter?\n")
    start_station = df['Start Station'].value_counts().reset_index()['index'][0]
    print (start_station)
    print("\n* Q6. What is the most popular end station?\n")
    end_station = df['End Station'].value_counts().reset_index()['index'][0]
    print(end_station)
    return start_station, end_station

def popular_trip(df):
    """most common trip from start to end
    """
    result = df[['Start Station', 'End Station']].groupby(['Start Station', 'End Station']).size().nlargest(1)
    print('\n* 2. Part c What was the most popular trip from start to end?')
    return result

def gender_data(df):
    """What are the counts of gender?"""
    try:
        print('\n* 4. Part b What is the breakdown of gender among users?\n')
        return df['Gender'].value_counts()
    except:
        print('There is no gender data for this city.')

def bike_users(df):
    """What are the counts of each user type?
    """
    print('\n* 4. Part a Types of users: subscribers, customers, others\n')
    return df['User Type'].value_counts()

def birth_years(df):
    """earliest, most recent, most common year of birth
    """
    try:
        print('\n* 4. Part c What is the earliest, latest, and most  popular year of birth?')
        earliest = np.min(df['Birth Year'])
        print ("\nThe earliest birth year " + str(earliest) + "\n")
        latest = np.max(df['Birth Year'])
        print ("The latest birth year " + str(latest) + "\n")
        most_popular= df['Birth Year'].mode()[0]
        print ("The most  popular birth year " + str(most_popular) + "\n")
        return earliest, latest, most_popular
    except:
        print('There is no birth year data for Washington.')

def process(f, df):
    """Calculates the time it takes to compute a statistic"""
    start_time = time.time()
    statToCompute = f(df)
    print(statToCompute)
    print("Computing this stat took %s seconds." % (time.time() - start_time))

def raw_stats(df):
    df = df.drop(['month', 'day_of_month'], axis = 1)
    row_index = 0

    see_data = input("\nWould you like to see 5 rows of the raw data used to compute the data? Please write 'yes' or 'no' \n").lower()
    while True:
        if see_data == 'no':
            return
        if see_data == 'yes':
            print(df[row_index: row_index + 5])
            row_index = row_index + 5
        see_data = input("\n Would you like to see the next 5 rows of the data? Please write 'yes' or 'no' \n").lower()

def main():

    city = get_city()
    df = load_data(city)
    period = time_view()
    month = get_month(period)
    day = day_stats(period)

    df = time_stats(df, period, month, day )
    raw_stats(df)

    stats_funcs_list = [month_freq,
     day_freq, hour_freq,
     trip_duration_stats, popular_trip,
     station_stats, bike_users, birth_years, gender_data]

    for x in stats_funcs_list:
        process(x, df)

    restart = input("\n * Would you like to restart? Type yes or no\n")
    if restart.upper() == 'YES':
        main()

if __name__ == '__main__':
    main()
