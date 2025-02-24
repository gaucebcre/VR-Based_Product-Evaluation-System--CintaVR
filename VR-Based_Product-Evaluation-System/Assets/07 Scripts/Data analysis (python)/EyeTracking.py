import os
import pandas as pd

# Obtener la lista de archivos CSV
# CAMBIAR RUTA SEGÚN SE NECESITE
csv_folder = r"D:\almud\Documents\04 Unity projects\VR-Based_Product-Evaluation-System\VR-Based_Product-Evaluation-System\Assets\StreamingAssets"
csv_files = [file for file in os.listdir(csv_folder) if file.endswith("Eye-tracking.csv")]

# Frecuencia (Hz) que puedes modificar
hz = 5.0
time_per_sample = 1 / hz  # Calcular el tiempo entre muestras en segundos

# Crear un diccionario para almacenar los datos de cada archivo
data_dict = {}

# Asegurarnos de que tenemos archivos CSV en la carpeta
if not csv_files:
    print(f"No se encontraron archivos CSV en {csv_folder}.")
else:
    print(f"Se encontraron los siguientes archivos CSV en {csv_folder}:")
    print(csv_files)

# Iterar a través de cada archivo CSV
for file in csv_files:
    # Crear la ruta completa al archivo CSV
    file_path = os.path.join(csv_folder, file)
    print(f"Procesando archivo: {file_path}")
    
    # Leer el archivo CSV
    df = pd.read_csv(file_path)
    
    # Verificar si la columna "Volume" existe
    if 'Volume' in df.columns:
        # Empezamos desde la segunda fila (índice 1) y reemplazamos los valores "Blink"
        for i in range(1, len(df)):
            if df.at[i, 'Volume'] == 'Blink':
                df.at[i, 'Volume'] = df.at[i - 1, 'Volume']  # Reemplazar "Blink" con el valor anterior
                # Continuar reemplazando los "Blink" consecutivos
                j = i + 1
                while j < len(df) and df.at[j, 'Volume'] == 'Blink':
                    df.at[j, 'Volume'] = df.at[i - 1, 'Volume']  # Reemplazar el siguiente "Blink"
                    j += 1
        
        # Crear la ruta para guardar el archivo procesado
        output_file_path = os.path.join(csv_folder, file.replace('.csv', '-PP.csv'))
        
        # Guardar el archivo CSV procesado con el sufijo "-PP" en la misma carpeta
        df.to_csv(output_file_path, index=False)
        print(f"Archivo procesado y guardado: {output_file_path}")

        # Ahora, procesamos el archivo -PP.csv para calcular el tiempo de visualización
        last_value = None
        current_time = 0  # Inicializamos el tiempo total en 0 segundos
        time_data = {}  # Diccionario para almacenar los tiempos de visualización por elemento

        # Iterar a través de las filas del DataFrame
        for index, row in df.iterrows():
            volume = row['Volume']  # Leer el valor de 'Volume'
            
            # Si el valor no es 'Blink', acumulamos el tiempo para ese 'Volume'
            if volume != 'Blink':
                if volume != last_value:
                    # Si es un nuevo elemento, asignamos el tiempo correspondiente
                    if last_value is not None:
                        time_data[last_value] = time_data.get(last_value, 0) + current_time * time_per_sample
                    current_time = 0  # Reiniciar el contador de tiempo para el nuevo valor
                
                # Acumular el tiempo para el valor actual
                current_time += 1
                last_value = volume
        
        # Al final del procesamiento, añadimos el tiempo acumulado para el último valor
        if last_value is not None:
            time_data[last_value] = time_data.get(last_value, 0) + current_time * time_per_sample

        # Agregar los datos al diccionario principal
        data_dict[file] = time_data

# Crear un DataFrame de pandas con la estructura que mencionas
final_data = {}

# La primera columna es el nombre de cada archivo
final_data["Archivo"] = list(data_dict.keys())

# Crear columnas para cada elemento, y para cada archivo, guardar el tiempo correspondiente
# Primero, obtenemos todos los elementos únicos que aparecen en todos los archivos
all_elements = set()
for time_data in data_dict.values():
    all_elements.update(time_data.keys())

# Asegurarnos de que las columnas estén en el mismo orden
all_elements = sorted(all_elements)

# Crear una columna para cada elemento
for element in all_elements:
    final_data[element] = [
        data_dict[file].get(element, 0)  # Si el elemento no está, asignamos 0
        for file in data_dict
    ]

# Crear el DataFrame final
final_df = pd.DataFrame(final_data)

# Guardar el DataFrame como un archivo CSV llamado Final-Data.csv, con separación por ";"
final_output_path = os.path.join(csv_folder, "Final-ET-Data.csv")
final_df.to_csv(final_output_path, index=False, sep=";")

print(f"Archivo 'Final-ET-Data.csv' guardado en {final_output_path}")



    