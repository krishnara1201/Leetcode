import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    col = f"getNthHighestSalary({N})"
    salaries = (
        employee["salary"]
        .dropna()
        .drop_duplicates()
        .sort_values(ascending=False)
    )
    if N <= 0 or N > len(salaries):
        return pd.DataFrame({col:[None]})


    return pd.DataFrame({col:[salaries.iloc[N-1]]})