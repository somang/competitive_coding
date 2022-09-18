"""
Isyana is given the number of visitors at her local theme park on 
N consecutive days. The number of visitors on the i-th day is Vi.
A day is record breaking if it satisfies both of the following conditions:

Either it is the first day, or the number of visitors on the day is strictly larger than the number of visitors on each of the previous days.
Either it is the last day, or the number of visitors on the day is strictly larger than the number of visitors on the following day.
Note that the very first day could be a record breaking day!
Please help Isyana find out the number of record breaking days.

Input
The first line of the input gives the number of test cases, T. 
T test cases follow. 
Each test case begins with a line containing the integer N. 
The second line contains N integers. 
The i-th integer is Vi and represents the number of visitors on the i-th day.

Sample input
4
8
1 2 0 7 2 0 2 0
6
4 8 15 16 23 42
9
3 1 4 1 5 9 2 6 5
6
9 9 9 9 9 9

"""

def number_of_record_breaking_days(number_of_days, visitors):
    record_breaking_days = 0
    prev_record = 0
    for i in range(number_of_days):
        greater_than_prev_days = (i == 0) or (visitors[i] > prev_record)
        greater_than_following_day = (i == number_of_days-1) or (visitors[i] > visitors[i+1])
        if greater_than_prev_days and greater_than_following_day:
            record_breaking_days += 1
        prev_record = max(prev_record, visitors[i])

    return record_breaking_days

def main():
    test_cases = int(input())
    for test_case in range(1, test_cases + 1, 1):
        number_of_days = int(input())
        vistors = list(map(int, input().split()))
        ans = number_of_record_breaking_days(number_of_days, vistors)
        print("Case #{}: {}".format(test_case, ans))

if __name__ == "__main__":
    main()
