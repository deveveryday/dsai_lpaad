test = [
    #0 month, 1 income, 2 variable costs, 3 costs, 4 imo
    ["jan", 85000, 46000, 18000, 0],
    ["fev", 92000, 51000, 19000, 0],
    ["mar", 78000, 48000, 20000, 0],
    ["apr", 105000, 54000, 21000, 0],
    ["may", 88000, 52000, 22000, 0]
]

first_month_name = test[0][0]
first_month_result = test[0][1] - test[0][2] - test[0][3]
first_month_imo = (first_month_result / test[0][1]) * 100

second_month_name = test[1][0]
second_month_result = test[1][1] - test[1][2] - test[1][3]
second_month_imo = (second_month_result / test[1][1]) * 100

third_month_name = test[2][0]
third_month_result = test[2][1] - test[2][2] - test[2][3]
third_month_imo = (third_month_result / test[2][1]) * 100

forth_month_name = test[3][0]
forth_month_result = test[3][1] - test[3][2] - test[3][3]
forth_month_imo = (forth_month_result / test[3][1]) * 100

fifth_month_name = test[3][0]
fifth_month_result = test[3][1] - test[3][2] - test[3][3]
fifth_month_imo = (fifth_month_result / test[3][1]) * 100

test[0][4] = first_month_imo
test[1][4] = second_month_imo
test[2][4] = third_month_imo
test[3][4] = forth_month_imo
test[4][4] = fifth_month_imo

print(test)

max_imo = max()
