import pandas as pd # type: ignore

def get_contest_data(contest_code: str):
    all_contest_data = pd.read_excel('contest_data.xlsx')
    contest_data = all_contest_data[all_contest_data['contest_code'] == contest_code]
    return contest_data

def update_contest_data(contest_data: pd.Series):
    with pd.ExcelWriter('contest_data.xlsx', mode='a', engine='openpyxl', if_sheet_exists='overlay') as writer:
        contest_data.to_excel(writer, sheet_name='data', header=False, index=False, startrow=contest_data.index[0]+1)