# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi():
    # Use a breakpoint in the code line below to debug your script.
    value = int(input())

    leftOver = value % 100
    plusValue = 99 - leftOver
    if leftOver < 49:
        value -= leftOver+1
    else:
        value += plusValue

    if value == 0:
        value = 99

    print(value)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
