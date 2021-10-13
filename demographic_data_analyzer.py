import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    races = df['race']
    race_count = None
    race_dict = {}
    for e in races:
      if e not in race_dict:
        race_dict[e] = 1
      else:
        race_dict[e] += 1
    race_count = pd.Series(race_dict)

    # What is the average age of men?
    df_men = df[df.sex == 'Male']
    average_age_men = round(df_men['age'].mean(),1)
    

    # What is the percentage of people who have a Bachelor's degree?
    educ = df[df.education == 'Bachelors']
    percentage_bachelors = round(len(educ)/len(df),3)*100

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?
    adv_edu = ['Bachelors', 'Masters', 'Doctorate']
    df_advedu = df[df.education.isin(adv_edu)]
    df_lowedu = df[~df.education.isin(adv_edu)]
    edu_paid = 0
    nedu_paid = 0
    for e in df_advedu['salary']:
      if e == ">50K":
        edu_paid += 1
    for e in df_lowedu['salary']:
      if e == ">50K":
        nedu_paid += 1

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = len(df_advedu)
    lower_education = len(df_lowedu)

    # percentage with salary >50K
    higher_education_rich = round(edu_paid/higher_education,3)*100
    lower_education_rich = round(nedu_paid/lower_education,3)*100

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()
    df_min_hours = df[df['hours-per-week'] == min_work_hours]
    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = 0
    for e in df['hours-per-week']:
      if e == min_work_hours:
        num_min_workers += 1
    
    min_rich = 0
    for e in df_min_hours['salary']:
      if e == '>50K':
        min_rich += 1
    rich_percentage = round(min_rich/num_min_workers,3)*100

    # What country has the highest percentage of people that earn >50K?
    country_count = {}
    country_rich = {}
    for e in df['native-country']:
      if e not in country_count:
        country_count[e] = 1
      else:
        country_count[e] += 1

    country_series = df['native-country']
    salary_series = df['salary']

    for e in range(len(df)):
      c = country_series[e] 
      s = salary_series[e]
      if c not in country_rich:
        if s == ">50K":
          country_rich[c] = 1
        else:
          country_rich[c] = 0
      else:
        if s == ">50K":
          country_rich[c] += 1

    country_perc = {}

    for c in country_count:
      country_perc[c] = round(country_rich[c]/country_count[c],3)
      

    highest_earning_country = max(country_perc, key=country_perc.get)
    highest_earning_country_percentage = country_perc[highest_earning_country]*100

    # Identify the most popular occupation for those who earn >50K in India.
    india_df = df[df['native-country'] == 'India']
    df_rich_india = india_df[india_df['salary'] == '>50K']

    top_ocu = {}

    for e in df_rich_india['occupation']:
      if e not in top_ocu:
        top_ocu[e] = 1
      else:
        top_ocu[e] += 1

    top_IN_occupation = max(top_ocu, key = top_ocu.get)
    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
