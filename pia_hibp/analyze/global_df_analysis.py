def breach_percentage(df):
    if 'breached' not in df.columns:
        raise ValueError("El dataframe no contiene columna breached")
    total_participants = len(df) #Total de filas
    affected_participants = df['breached'].sum() #Suma num filas donde breached es True
    if total_participants > 0:
        percentage = (affected_participants / total_participants) * 100
    else:
        percentage = 0
    return percentage

def breach_average(df):
    if 'breached' not in df.columns:
        raise ValueError("El dataframe no contiene la columna 'breach_num'")
    return df['breach_num'].mean()

def breach_median(df):
    if 'breach_num' not in df.columns:
        raise ValueError("El dataframe no contiene la columna 'breach_num'")
    return df['breach_num'].median()
