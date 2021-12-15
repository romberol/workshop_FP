import pandas as pd

def readfile():
    try:
        data = pd.read_csv("deadline.csv")
    except FileNotFoundError:
        data = pd.DataFrame(columns=["Date", "Priority", "Task", "State"], data=[[None, None, None, None]])
        data.to_csv("deadline.csv", encoding='utf-8', index=False)
    print("Your deadline table:")
    if data.dropna().shape==(0, 4):
        print("Your tabel is empty!")
    else:
        print(data)
    return data

def check_done(table):
    pass
def add_deadlines(table):
    newdata_ls = []
    question = input('Do you want to add something? (type anything if so, type 0 if no)')
    if question == '0':
        print('No changes are made')
        return False
    print('What exactly do you want to add?\
Please, enter datum in format of: date priority task status;\
press enter to enter next datum;\
press enter twice, if that is all')
    while True:
        new_datum = input()
        if new_datum == '':
            print('The data entered was:', newdata_ls)
            break
        new_datum  = new_datum.split()
        newdata_ls.append(new_datum)
    newdata_ls.sort(key=lambda x: ''.join(x[0].split(':'))[::-1])
    print('list sorted by data', newdata_ls)
    return newdata_ls
def check_input():
    pass
