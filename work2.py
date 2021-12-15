import pandas as pd

def readfile():
    try:
        data = pd.read_csv("deadline.csv")
    except FileNotFoundError:
        data = pd.DataFrame(columns=["Date", "Priority", "Task", "State"], data=[[None, None, None, None]])
        data.to_csv("deadline.csv", encoding='utf-8', index=False)
    return data

def check_done(table):
    def check_done(df):
    print("What deadline would you like to remove? Or type 'None'")
    inputt = input()
    if inputt == None:
        return
    elif inputt != None:
        what_to_del = inputt
        if what_to_del not in df["Date"]:
            print("Please enter an existing date")
            # check_done(df)
        else:
            df = df[df != what_to_del]
    return df

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
            break
        new_datum  = new_datum.split(" ")
        newdata_ls.append(new_datum)
    newdata_ls.sort(key=lambda x: ''.join(x[0].split(':'))[::-1])
    return pd.DataFrame(data = newdata_ls, columns=table.columns)


def check_input():
    pass
