import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os

# Obtener la lista de archivos CSV
# CAMBIAR EL NOMBRE ENTRE " " CON LA RUTA DE LA CARPETA DONDE ESTÉN LOS DATOS
csv_folder = "D:\\almud\\Documents\\04 Unity projects\\VR-Based_Product-Evaluation-System\\VR-Based_Product-Evaluation-System\\Assets\\StreamingAssets"
csv_files = [file for file in os.listdir(csv_folder) if file.endswith("_Position.csv")]

# Procesar cada archivo CSV por separado
for csv_filename in csv_files:
    # Cargar los datos desde el archivo CSV
    data = pd.read_csv(os.path.join(csv_folder, csv_filename), delimiter=";")

    # Convertir las coordenadas a números decimales
    data["X"] = data["X"].str.replace(",", ".").astype(float)
    data["Y"] = data["Y"].str.replace(",", ".").astype(float)

    # Escalar las coordenadas para aumentar la distancia visual entre los puntos
    scale_factor = 4  # Aumenta este factor para expandir la visualización
    data["X"] = data["X"] * scale_factor
    data["Y"] = data["Y"] * scale_factor

    # Crear la gráfica de dispersión con un tamaño personalizado
    fig, ax = plt.subplots(figsize=(30, 24))  # Ajusta el tamaño de la figura en pulgadas

    # Leer la imagen del entorno
    # CAMBIAR EL NOMBRE ENTRE " " CON LA RUTA DE LA CARPETA DONDE ESTÉN LOS DATOS
    environment_img = mpimg.imread("D:\\almud\\Documents\\04 Unity projects\\VR-Based_Product-Evaluation-System\\VR-Based_Product-Evaluation-System\\Assets\\StreamingAssets\\SceneSnapshot.png")

    # Ajustar el extent para centrar la imagen en el gráfico
    xmin, xmax, ymin, ymax = -20, 20, -20, 20  # Ajusta según tus coordenadas transformadas
    ax.imshow(environment_img, extent=[-15, 15, -8.5, 21.5], aspect='auto') #Modifica el tamaño de la imagen aquí

    # Generar la gráfica de dispersión encima de la imagen del entorno
    ax.scatter(data["X"], data["Y"], color='white', alpha=0.5, s=20, label='Player trajectory')  # Ajusta el tamaño de los puntos
    ax.set_title("Player movement")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.axis("equal")  # Ajustar el tamaño de los ejes X e Y para que tengan la misma escala
    ax.grid(False)  # Ocultar la cuadrícula

    # Ajustar los límites de los ejes si es necesario
    ax.set_xlim(xmin, xmax)  # Ajusta estos límites según tus datos transformados
    ax.set_ylim(ymin, ymax)

    # Configurar el fondo de la gráfica y de la figura como transparente
    ax.patch.set_facecolor('none')  # Fondo del área del gráfico
    fig.patch.set_facecolor('none')  # Fondo de la figura

    # Guardar la figura con el mismo nombre que el archivo CSV y calidad alta
    output_filename = os.path.splitext(csv_filename)[0] + "_martes" + ".png"
    plt.savefig(output_filename, dpi=300, bbox_inches='tight', transparent=True)  # Ajusta el DPI y usa transparencia

# Mostrar las gráficas una vez que se han guardado todas
plt.show()