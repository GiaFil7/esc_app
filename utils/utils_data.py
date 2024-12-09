import pandas as pd

def get_contest_data(contest_code: str) -> pd.Series:
    """
    Gets the data for the specified contest. They include a row for every year held and the columns:
        * **contest_code** *str*: The contest code
        * **year** *int*: The years held
        * **submitted** *bool*: If a ranking has been submitted for a particular year
        * **contest_name** *str*: The full contest name
    
    :param contest_code: The contest code
    :type contest_code: str
    :returns: The contest data
    :rtype: Series
    """

    all_contest_data = pd.read_excel('files\\contest_data.xlsx')
    contest_data = all_contest_data[all_contest_data['contest_code'] == contest_code]
    
    return contest_data

def update_contest_data(contest_data: pd.Series):
    """
    Updates the data of a contest. The data must have a row for every year and the following columns:
        * **contest_code** *str*: The contest code
        * **year** *int*: The years held
        * **submitted** *bool*: If a ranking has been submitted for a particular year
        * **contest_name** *str*: The full contest name
    
    :param contest_data: The new data to save to file
    :type contest_data: Series
    """

    with pd.ExcelWriter('files\\contest_data.xlsx', mode = 'a', engine = 'openpyxl', if_sheet_exists = 'overlay') as writer:
        contest_data.to_excel(writer, sheet_name = 'data', header = False, index = False, startrow = contest_data.index[0] + 1)

def get_entry_data(contest_code: str) -> pd.DataFrame:
    """
    Gets the data of entries of the specified contest. They include a row for every entry and the columns:
        * **contest** *str*: The contest code and year (e.g. ESC 1956)
        * **country** *str*: The name of the country
        * **country_code** *str*: The country code
        * **artist** *str*: The name of the artist
        * **song** *str*: The song title
        * **placing** *str*: The placing of the entry in the contest
        * **show** *str*: The semi-final the entry participated in (SF1/SF2). Or the Grand Final (GF) if automatically qualified.
        * **accepted_answers** *str*: The accepted answers for this entry in quizzes

        :param contest_code: The contest code
        :type contest_code: str
        :returns: The entry data
        :rtype: DataFrame
    """

    filename = f'files\\{contest_code}_data.xlsx'
    entry_data = pd.read_excel(filename)

    return entry_data

def update_entry_data(entry_data: pd.Series, contest_code: str):
    """
    Updates the data of entries of the specified contest. The data must have a row for every entry and the columns:
        * **contest** *str*: The contest code and year (e.g. ESC 1956)
        * **country** *str*: The name of the country
        * **country_code** *str*: The country code
        * **artist** *str*: The name of the artist
        * **song** *str*: The song title
        * **placing** *str*: The placing of the entry in the contest
        * **show** *str*: The semi-final the entry participated in (SF1/SF2). Or the Grand Final (GF) if automatically qualified.
        * **accepted_answers** *str*: The accepted answers for this entry in quizzes

        :param entry_data: The entry data
        :type entry_data: Series
        :param contest_code: The contest code
        :type contest_code: str
    """

    filename = f'files\\{contest_code}_data.xlsx'
    with pd.ExcelWriter(filename, mode = 'a', engine = 'openpyxl', if_sheet_exists = 'overlay') as writer:
            entry_data.to_excel(writer, sheet_name = contest_code, header = False, index = False, startrow = entry_data.index[0] + 1)

def get_contest_name(contest_data: pd.Series) -> str:
    name_column = contest_data['contest_name']
    contest_name = name_column[0]

    return contest_name

def get_countries(entry_data: pd.DataFrame) -> list:
    """
    Returns all participating countries in the contest.

    :param entry_data: The entry data of the contest
    :type entry_data: DataFrame
    :returns: A list of all participating countries
    :rtype: list
    """

    countries = entry_data['country'].unique()
    countries = list(countries)
    countries.sort()

    return countries

def get_country_codes(special_case="") -> pd.DataFrame:
    """
    Returns the country codes of all participating countries. If the contest is ESC 1956
    it returns the country codes for that year specifically. It contains one row per country
    and the following columns:
    * **country** *str*: The name of the country
    * **code** *str*: The country code

    In the case of ESC 1956, there is one row per entry and the following columns:
    * **country** *str*: The name of the country
    * **song** *str*: The song title
    * **code** *str*: The country code

    :param special_case: The type of special case (optional)
    :type special_case: str
    :returns: A DataFrame containing the country code data
    :rtype: DataFrame
    """

    if special_case == "":
        country_codes = pd.read_excel('files\\country_codes.xlsx', sheet_name = 'all_codes')
    elif special_case == "ESC 1956":
        country_codes = pd.read_excel('files\\country_codes.xlsx', sheet_name = '1956_codes')
    else:
        print("Invalid special case")
        country_codes = pd.DataFrame()

    return country_codes

def get_country_code(country: str) -> str:
    """
    Returns the country code of the specified country.

    :param country: The name of the country
    :type country: str
    :returns: The country code
    :rtype: str
    """

    country_codes = get_country_codes()
    country_code = country_codes[country_codes['country'] == country]
    country_code = country_code['code'].to_string(index = False, header = False)

    return country_code

def read_html_file(file_path: str) -> str:
    """
    Reads the specified html file and returns it as a string.

    :param file_path: The path to the file
    :type file_path: str
    :returns: The contents of the file as a string
    :rtype: str
    """

    with open(file_path, 'r') as file:
        html_as_string = file.read()

    return html_as_string

def get_quiz_data(contest_code: str) -> pd.DataFrame:
    """
    Gets the quiz data of the specified contest. They include a row for every quiz and the columns:
    * **quiz** *str*: The quiz code (e.g. year, country code)
    * **best_score** *int*: The user's best score for that quiz
    * **max_score** *int*: The maximum score for that quiz
    * **best_time** *int*: The user's best time (in seconds) for that quiz

    :param contest_code: The contest code
    :type contest_code: str
    :returns: The quiz data
    :rtype: DataFrame
    """

    filename = f'files\\quiz_data.xlsx'
    quiz_data = pd.read_excel(filename, sheet_name = contest_code)

    return quiz_data

def update_quiz_data(quiz_data: pd.Series, contest_code: str):
    """
    Updates the quiz data of a contest. The data must have a row for every quiz and the following columns:
    * **quiz** *str*: The quiz code (e.g. year, country code)
    * **best_score** *int*: The user's best score for that quiz
    * **max_score** *int*: The maximum score for that quiz
    * **best_time** *int*: The user's best time (in seconds) for that quiz
    
    :param quiz_data: The new quiz data to save to file
    :type quiz_data: Series
    :param contest_code: The contest code
    :type contest_code: str
    """

    with pd.ExcelWriter('files\\quiz_data.xlsx', mode = 'a', engine = 'openpyxl', if_sheet_exists = 'overlay') as writer:
        quiz_data.to_excel(writer, sheet_name = contest_code, header = False, index = False, startrow = 1)