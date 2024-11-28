import pandas as pd # type: ignore

def get_contest_data(contest_code: str):
    all_contest_data = pd.read_excel('contest_data.xlsx')
    contest_data = all_contest_data[all_contest_data['contest_code'] == contest_code]
    
    return contest_data

def update_contest_data(contest_data: pd.Series):
    with pd.ExcelWriter('contest_data.xlsx', mode='a', engine='openpyxl', if_sheet_exists='overlay') as writer:
        contest_data.to_excel(writer, sheet_name='data', header=False, index=False, startrow=contest_data.index[0]+1)

def get_entry_data(contest_code: str):
    filename = f'{contest_code}_data.xlsx'
    entry_data = pd.read_excel(filename)

    return entry_data

def update_entry_data(entry_data: pd.Series, contest_code: str):
    filename = f'{contest_code}_data.xlsx'
    with pd.ExcelWriter(filename, mode='a', engine='openpyxl', if_sheet_exists='overlay') as writer:
            entry_data.to_excel(writer, sheet_name=contest_code, header=False, index=False, startrow=entry_data.index[0]+1)

def get_contest_name(contest_data: pd.Series) -> str:
    name_column = contest_data['contest_name']
    contest_name = name_column[0]

    return contest_name

def get_countries(entry_data: pd.DataFrame) -> list:
    countries = entry_data['country'].unique()
    countries = list(countries)
    countries.sort()

    return countries

def get_country_codes() -> pd.DataFrame:
    country_codes = pd.read_excel('country_codes.xlsx')

    return country_codes