import pandas as pd

data = {
    'Fecha': ['2025-05-13', '2025-05-13', '2025-05-16'],
    'Paneles total': [2, 1, 4],
    'Paneles correctos': [2, 1, 4],
    'Paneles erroneos': [0, 0, 0],
    'Tiempo medio': [10.0, 7.0, 12.0]
}

# Crear un DataFrame de Pandas
df = pd.DataFrame(data)

# Guardar el DataFrame como un archivo CSV
df.to_csv('datos_operarios.csv', index=False)

print("CSV generado con éxito: 'datos_operarios.csv'")
