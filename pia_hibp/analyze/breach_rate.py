import pandas as pd

def by_group(df, col):
    # Verificar columnas necesarias
    required_cols = [col, 'breached']
    for required_col in required_cols:
        if required_col not in df.columns:
            raise ValueError(f"La columna '{required_col}' no existe en el DataFrame")
    
    # Obtener el total de personas por grupo
    total_by_group = df[col].value_counts().to_dict()
    
    # Obtener el número de personas comprometidas por grupo
    breached_by_group = df[df['breached'] == True][col].value_counts().to_dict()
    
    # Calcular la tasa de compromiso para cada grupo
    breach_rates = []
    for group in total_by_group:
        breached = breached_by_group.get(group, 0)
        total = total_by_group[group]
        rate = (breached / total) * 100
        breach_rates.append({'Group': group, 'Breach Rate (%)': rate})
    
    # Convertir a DataFrame
    breach_rates_df = pd.DataFrame(breach_rates)
    
    # Ordenar de mayor a menor tasa
    breach_rates_df = breach_rates_df.sort_values('Breach Rate (%)', ascending=False)
    
    return breach_rates_df
