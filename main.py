import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }


MONTH = {
    1: 'January',
    2: 'February',
    3: 'March',
    4: 'April',
    5: 'May',
    6: 'June',
    7: 'July',
    8: 'August',
    9: 'September',
    10: 'October',
    11: 'November',
    12: 'December'
}

DAY = {
    1: 'Sunday',
    2: 'Monday',
    3: 'Tuesday',
    4: 'Wenesday',
    5: 'Thursday',
    6: 'Friday',
    7: 'Saturday'
    
}


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    city = '' 
    month = ''
    day = ''
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True: 
        city = input('Enter Us city chicago , new york city or washington \n').lower()
        if city.lower() in ['chicago' , 'new york city' , 'washington']:
            break 
        

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        try:
            month = int(input('Enter the desired month: 0 for all, 1 for January, 2 for February, ... 6 for June\n'))
            if 0 <= month <= 6:
                break
            else:
                print("Invalid month number. Please enter a number between 0 and 12.")
        except ValueError:
            print("Invalid input. Please enter a valid number for the month.")

    # TO DO: get user input for day of the week (all, sunday , monday, tuesday, ... sunday)
    while True:
        try:
            day = int(input('Enter the desired day: 0 for all, 1 for Sunday, 2 for Monday, ... 7 for Saturday\n'))
            if 0 <= day <= 7:
                break
            else:
                print("Invalid day number. Please enter a number between 0 and 7.")
        except ValueError:
            print("Invalid input. Please enter a valid number for the day.")

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    df = pd.read_csv(CITY_DATA[city])
    
    # Convert 'Start Time' to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Extract month and day of week
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.dayofweek + 1  # 1=Sunday, ..., 7=Saturday
    df['hour'] = df['Start Time'].dt.hour
    
    # Filter by month and day
    df = df[((df['month'] == month) | (month == 0)) & ((df['day_of_week'] == day) | (day == 0))]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    
    # TO DO: display the most common month
    start_time = time.time()
    modeMonth = df['month'].mode()[0]
    countMonth = df['month'].value_counts()[modeMonth]
    
    print(f'The most common month is "{MONTH[modeMonth]}" with {countMonth} occurrences')

    # TO DO: display the most common day of week
    modeDay = df['day_of_week'].mode()[0]
    countDay = df['day_of_week'].value_counts()[modeDay]
    
    print(f'The most common Day is "{DAY[modeDay]}" with {countDay} occurrences')

    # TO DO: display the most common start hour
    modeHour = df['hour'].mode()[0]
    countHour = df['hour'].value_counts()[modeHour]
    print(f'The most common Hour is "{modeHour}" with {countHour} occurrences')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    
    # TO DO: display most commonly used start station
    modeStart = df['Start Station'].mode()[0]
    countStart = df['Start Station'].value_counts()[modeStart]
    print(f'The most common start station is "{modeStart}" with {countStart} trips')

    # TO DO: display most commonly used end station
    modeEnd = df['End Station'].mode()[0]
    countEnd = df['End Station'].value_counts()[modeEnd]
    print(f'The most common end station is "{modeEnd}" with {countEnd} trips')


    # TO DO: display most frequent combination of start station and end station trip
    # Find the most frequent combination of start and end station
    modeComp = df[['Start Station', 'End Station']].mode().iloc[0]

    # Extract the values for start and end station
    start_station = modeComp['Start Station']
    end_station = modeComp['End Station']

    # Filter the DataFrame for rows with the same combination
    most_common_combination = df[(df['Start Station'] == start_station) & (df['End Station'] == end_station)]

    # Get the count of the most frequent combination
    countComp = most_common_combination.shape[0]

    # Print the result
    print(f'The most common combination of start and end station is "{start_station}" -> "{end_station}" with {countComp} times')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)




def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    Total_Time = df['Trip Duration'].sum()
    print(f'Total Time travel is "{Total_Time}"')
    
    # TO DO: display mean travel time
    avg_time = df['Trip Duration'].mean()
    print(f'Average Time Travle is "{avg_time}"')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    userCount = df['User Type'].value_counts()
    print(f'The number of Users Type is "{userCount}"')

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        genderCount = df['Gender'].value_counts()
        print(f'The number of Gender is "{genderCount}"')
    else :
        # washington.csv does not have Birth Year or gender columns 
        return 

    # TO DO: Display earliest, most recent, and most common year of birth
    years = df['Birth Year'].dropna().astype(int)
    
    # Display the earliest year
    earliest_year = years.min()

    # Display the most recent year
    most_recent_year = years.max()

    # Display the most common year
    most_common_year = years.mode()[0]

    # Display the results
    print(f'Earliest Year of Birth: {earliest_year}')
    print(f'Most Recent Year of Birth: {most_recent_year}')
    print(f'Most Common Year of Birth: {most_common_year}')
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def generator(start, df, chunk_size):
    for i in range(start, len(df), chunk_size):
        yield df[i:i + chunk_size]

def display_data(df):
    for chunk in generator(0, df, 5):
        user_input = input("Show 5 rows of data? Write Yes or No as an answer: ").lower()
        if user_input == 'yes':
            print(chunk)
        else:
            print("Exiting display.")
            break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
