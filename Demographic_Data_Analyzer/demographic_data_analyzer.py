import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult_data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    age = df.loc[df['sex']=='Male']
    avr = age['age']
    average_age_men = float('{:.3}'.format(avr.mean()))

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = float('{:.3}'.format((df['education'].value_counts()['Bachelors'] / df['education'].count()) * 100))

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    sum_bachelors = df.loc[df['education']=='Bachelors'].loc[df['salary'] == '>50K']['education'].value_counts()['Bachelors']
    sum_masters = df.loc[df['education']=='Masters'].loc[df['salary'] == '>50K']['education'].value_counts()['Masters']
    sum_doctorate = df.loc[df['education']=='Doctorate'].loc[df['salary'] == '>50K']['education'].value_counts()['Doctorate']

    total_bachelors = df.loc[df['education']=='Bachelors']['education'].value_counts()['Bachelors']
    total_masters = df.loc[df['education']=='Masters']['education'].value_counts()['Masters']
    total_doctorate = df.loc[df['education']=='Doctorate']['education'].value_counts()['Doctorate']

    higher_education_rich = float('{:.3}'.format((sum_bachelors + sum_masters + sum_doctorate) / (total_bachelors + total_masters + total_doctorate) * 100))

    # What percentage of people without advanced education make more than 50K?
    sum_hsgrade = df.loc[df['education']=='HS-grad'].loc[df['salary'] == '>50K']['education'].value_counts()['HS-grad']
    sum_some_college = df.loc[df['education']=='Some-college'].loc[df['salary'] == '>50K']['education'].value_counts()['Some-college']

    total_education = df['education'].loc[df['salary']=='>50K'].value_counts().sum()

    lower_education_rich = float('{:.3}'.format((((sum_hsgrade + sum_some_college + sum_bachelors + sum_masters + sum_doctorate) / total_education) * -100) + 100))

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    hours_per_week = df['hours-per-week']
    min_work_hours = hours_per_week.min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    rich_percentage = float('{:.2}'.format((df.loc[df['salary']=='>50K'].loc[df['hours-per-week'] < 40]['salary'].value_counts()['>50K'] / df.loc[df['salary']=='>50K']['salary'].value_counts()['>50K']) * 100))

    # What country has the highest percentage of people that earn >50K?
    count_country = df['native-country'].value_counts()
    rich_country_count = df[df['salary'] =='>50K']['native-country'].value_counts()
    highest_earning_country = (rich_country_count / count_country * 100).idxmax()
    highest_earning_country_percentage = round((rich_country_count / count_country * 100).max(), 1)

    # Identify the most popular occupation for those who earn >50K in India.
    rich_indians = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
    top_IN_occupation = rich_indians['occupation'].value_counts().idxmax()

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print(f"Number of each race:\n{race_count}")
        print(f"Average age of men: {average_age_men}")
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print(f"Country with highest percentage of rich: {highest_earning_country}")
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print(f"Top occupations in India: {top_IN_occupation}")

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }