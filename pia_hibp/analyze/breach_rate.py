import pandas as pd

def by_group(df, col):
    # Verifies required columns
    required_cols = [col, 'breached']
    for required_col in required_cols:
        if required_col not in df.columns:
            raise ValueError(f"La columna '{required_col}' no existe en el DataFrame")
    
    # Total per group
    total_by_group = df[col].value_counts().to_dict()
    
    # Total breached per group
    breached_by_group = df[df['breached'] == True][col].value_counts().to_dict()
    
    # Breached rate per group
    breach_rates = []
    for group in total_by_group:
        breached = breached_by_group.get(group, 0)
        total = total_by_group[group]
        rate = (breached / total) * 100
        breach_rates.append({'Group': group, 'Breach Rate (%)': rate})
    
    # Creates DataFrame
    breach_rates_df = pd.DataFrame(breach_rates)
    
    # Orders breach rates
    breach_rates_df = breach_rates_df.sort_values('Breach Rate (%)', ascending=False)
    
    return breach_rates_df
