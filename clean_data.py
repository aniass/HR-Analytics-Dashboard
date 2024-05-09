import pandas as pd

URL = r'C:\Python Scripts\Datasets\HR_employee\HR-Employee-Attrition.csv'


def read_data(path):
    df = pd.read_csv(path)
    return df


def age_ranges(row):
    if row <= 25:
        return '18-25'
    elif (row >= 26) and (row <= 35):
        return '26-35'
    elif (row >= 36) and (row <= 45):
        return '36-45'
    elif (row >= 46) and (row <= 54):
        return '46-54'
    else:
        return '55+'


def salary(row):
    if row <= 5000:
        return 'up to 5k'
    elif (row > 5000) and (row <= 10000):
        return '5k-10k'
    elif (row > 10000) and (row <= 15000):
        return '10k-15k'
    else:
        return '15+'


def prepare_data(df):
    # Convert Attrition variable into numeric:
    df['Attrition_num'] = df['Attrition'].map({'No' : 0, 'Yes' : 1})
    # Create Age ranges:
    df['Age_num'] = df['Age'].apply(age_ranges)
    # Create Salary ranges:
    df['Salary'] = df['MonthlyIncome'].apply(salary)
    return df


def get_summary(data):
    df = prepare_data(data)
    print(df.head())
    print(f'Shape of data:', df.shape)
    print(df.info())


if __name__ == '__main__':
    df = read_data(URL)
    get_summary(df)
    #df.to_csv('data\HR_employee.csv')
    
