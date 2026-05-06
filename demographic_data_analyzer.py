import pandas as pd

def calculate_demographic_data(print_data=True):
    # Read dataset
    df = pd.read_csv("adult.data.csv")

    # 1. Number of each race
    race_count = df['race'].value_counts()

    # 2. Average age of men
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # 3. Percentage with Bachelor's degree
    total = len(df)
    bachelors = len(df[df['education'] == 'Bachelors'])
    percentage_bachelors = round((bachelors / total) * 100, 1)

    # 4. Higher education (Bachelors, Masters, Doctorate)
    higher_edu = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    lower_edu = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]

    # 5. Percentage with higher education earning >50K
    higher_edu_rich = round(
        (len(higher_edu[higher_edu['salary'] == '>50K']) / len(higher_edu)) * 100, 1
    )

    # 6. Percentage without higher education earning >50K
    lower_edu_rich = round(
        (len(lower_edu[lower_edu['salary'] == '>50K']) / len(lower_edu)) * 100, 1
    )

    # 7. Minimum work hours
    min_work_hours = df['hours-per-week'].min()

    # 8. Percentage earning >50K among those who work minimum hours
    min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = round(
        (len(min_workers[min_workers['salary'] == '>50K']) / len(min_workers)) * 100, 1
    )

    # 9. Country with highest percentage earning >50K
    country_counts = df['native-country'].value_counts()
    rich_country = df[df['salary'] == '>50K']['native-country'].value_counts()

    country_percentage = (rich_country / country_counts * 100).dropna()
    highest_earning_country = country_percentage.idxmax()
    highest_earning_country_percentage = round(country_percentage.max(), 1)

    # 10. Most popular occupation in India for >50K earners
    india_rich = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
    top_IN_occupation = india_rich['occupation'].value_counts().idxmax()

    # Print results
    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print("Percentage with Bachelors degrees:", percentage_bachelors)
        print("Higher education rich %:", higher_edu_rich)
        print("Lower education rich %:", lower_edu_rich)
        print("Min work time:", min_work_hours)
        print("Rich percentage among min workers:", rich_percentage)
        print("Country with highest % of rich:", highest_earning_country)
        print("Highest % of rich people in country:", highest_earning_country_percentage)
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_edu_rich,
        'lower_education_rich': lower_edu_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }