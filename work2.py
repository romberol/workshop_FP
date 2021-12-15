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
    pass
def check_input():
    pass
