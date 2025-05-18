from pia_hibp.analyze.pd_analysis import df_create


def analyze_by_answer(df, col):
    # Verificar que las columnas necesarias existen
    required_cols = [col, 'breached']
    
    for required_col in required_cols:
        if required_col not in df.columns:
            raise ValueError(f"La columna '{required_col}' no existe en el DataFrame")
    
    # Filtrar sólo las filas donde breached es True
    breached_df = df[df['breached'] == True]
    
    # Contar ocurrencias de cada respuesta única en la columna especificada
    results = breached_df[col].value_counts().to_dict()
    
    return results
