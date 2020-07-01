def output_years():
    years_list = []
    years1 = input('start year：')
    years2 = input('end year：')
    int_years1 = int(years1)
    int_years2 = int(years2)

    if years2 < years1:
        print('error, end year should bigger than start year')
        return
    for years in range(int_years1,int_years2+1):
        if years % 100 == 0:
            if years % 400 == 0:
                years_list.append(years)
        elif years % 4 == 0:
            years_list.append(years)
    print(years_list)
    return
output_years()