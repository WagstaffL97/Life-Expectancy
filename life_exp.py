
ages = []
new_ages = []
places = []
years = []

min_age = 100
max_age = 10
min_place = ""
max_place = ""
min_time = ""
max_time = ""
maximum_place = ""
maximum_year = ""
minimum_place = ""
minimum_year = ""

year = (input("What year would you like to learn about? "))

print()

with open("life-expectancy.csv") as life_expect:
    for info in life_expect:
        clean = info.strip()
        split = clean.split(",")

        old = float(split[3])
        dest = split[0]
        calender = split[2]

        ages.append(old)
        places.append(dest)
        years.append(calender)

        if calender == year:

            new_ages.append(old)
            year_sum = sum(new_ages)
            year_average = year_sum/len(new_ages)

            if old > max_age:
                max_age = old
                max_place = dest
                max_time = calender
            
            if old < min_age:
                    min_age = old
                    min_place = dest
                    min_time = calender

        maximum_age = max(ages)
        minimum_age = min(ages) 

        if old == maximum_age:
            maximum_age = old
            maximum_place = dest
            maximum_year = calender
        if old == minimum_age:
            minimum_age = old
            minimum_place = dest
            minimum_year = calender   

    average_sum = sum(ages)
    overall_average = average_sum/len(ages)

    print(f"Overall MAXIMUM life expectancy is {maximum_age} from {maximum_place} at {maximum_year}.")
    print(f"Overall MINIMUM life expectancy is {minimum_age} from {minimum_place} at {minimum_year}.")
    print(f"Overall AVERAGE life expectancy for the entire list is {overall_average:.2f}")   
    print()
    print(f"For the year {year}:")
    print(f"The average life expectancy across all countries this year is {year_average:.2f} year(s)")
    print(f"The maximum life expectancy was in {max_place} at {max_age}")
    print(f"The minimum life expectancy was in {min_place} at {min_age}")


    







        
