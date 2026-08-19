import pandas as pd

def employee_bonus(employee: pd.DataFrame, bonus: pd.DataFrame) -> pd.DataFrame:
    df_merged = employee.merge(bonus, how = "left", on = "empId")
    return df_merged[(df_merged["bonus"].isna()) | (df_merged["bonus"] < 1000)][["name","bonus"]]