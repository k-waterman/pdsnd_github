import time
import pandas as pd
import numpy as np
import calendar 

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    cities=['chicago', 'new york city', 'washington']
    while True:
        city=input('Please specify which city you would like to see data for: chicago, new york city, or washington.').lower()
        if city.lower() in cities:
            break
        else:
            print('Please enter a valid city name.')
 
    # TO DO: get user input for month (all, january, february, ... , june)
    months=['january','february','march','april','may','june']

    while True:
        month=input('Please specify a month you would like to see data for, between the months of january and june. Enter "all" to see data for all available months').lower()
        if month.lower() in months:
            break
        else:
            print('Please enter a valid month.')


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days=['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
    while True:
            day=input('Please specify which day of the week you would like to see data for. Enter "all" to see data for all days of the week.').lower()
            if day.lower() in days:
                break
            elif day not in days and day!='all':
                print('Please enter a valid day of the week.')

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
    
     # referenced Practice Problem 3 for the following code...  
     # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
 


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
 

    # TO DO: display the most common month
    
    #convert Start_Time column to month
    df['month'] = df['Start Time'].dt.month  
    #find the most common month of travel
    common_month = df['month'].mode()[0]
    print('Travel is most frequent in the month of:', common_month)

    
 


    # TO DO: display the most common day of week. I have referenced Practice Problem 1 for the following code...
    
    #convert Start_Time column to weekday_name
    df['weekday'] = df['Start Time'].dt.weekday_name
    #find the most common day of travel 
    common_day_week = df['weekday'].mode()[0]
    print('The most frequent day of the week for travel is:', common_day_week)

 

    # TO DO: display the most common start hour
    
    # convert the Start_Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour
    # find the most common hour of travel
    common_start_hour = df['hour'].mode()[0]
    print('The most frequent hour for travel is:', common_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start=df['Start Station'].mode()[0]
    print('The most frequently used start station:', common_start)


    # TO DO: display most commonly used end station
    common_end=df['End Station'].mode()[0]
    print('The most frequently used end station:', common_end)


    # TO DO: display most frequent combination of start station and end station trip
    common_combo=(df['Start Station'] + ' - ' + df['End Station']).mode()[0]
    print("The most common combination of start and end stations is: ", common_combo)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_duration=df['Trip Duration'].sum()
    print('The total travel time is:', total_duration, 'seconds')


    # TO DO: display mean travel time
    average_duration=df['Trip Duration'].mean()
    print('The average trip duration is:', average_duration, 'seconds')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    
    user_types = df['User Type'].value_counts()
    print(user_types)
    
    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        gender_counts=df['Gender'].value_counts()
        print('Gender counts:', gender_counts)
    else:
        print('Gender data not available in this dataset.')


    # TO DO: Display earliest, most recent, and most common year of birth
    
    if 'Birth Year' in df.columns:
        oldest_user=df['Birth Year'].min()
        youngest_user=df['Birth Year'].max()
        common_age=df['Birth Year'].mode()
        print('The oldest user age is:', oldest_user)
        print('The youngest user age is:', youngest_user)
        print('The most common user age is:', common_age)
    else:
        print('Birth year data not avaiable in this dataset.')
        
    


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
        
def raw_data(df):
    #displays first 5 lines of data 
    i = 0
    while True:
        view_raw_data = input('\n Would you like to view raw data? Please input yes or no to view the first 5 lines of data.\n')
        
        if view_raw_data.lower() != 'yes':
            break
            
        else:
            i= i+ 5
            print(df.iloc[i:i+5])

        

       


if __name__ == "__main__":
        main()
