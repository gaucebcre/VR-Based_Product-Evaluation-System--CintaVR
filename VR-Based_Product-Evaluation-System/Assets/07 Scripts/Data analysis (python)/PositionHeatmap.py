import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os
import seaborn as sns

# Obtener la lista de archivos CSV en la carpeta actual
csv_folder = "."  # Carpeta actual
csv_files = [file for file in os.listdir(csv_folder) if file.endswith(".csv")]

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

    # Crear la gráfica de mapa de calor con un tamaño personalizado
    fig, ax = plt.subplots(figsize=(30, 24))  # Ajusta el tamaño de la figura en pulgadas

    # Leer la imagen del entorno
    environment_img = mpimg.imread("Green-VirtualEnvironment_Top.png")

    # Ajustar el extent para centrar la imagen en el gráfico
    xmin, xmax, ymin, ymax = -20, 20, -20, 20  # Ajusta según tus coordenadas transformadas
    ax.imshow(environment_img, extent=[-15, 15, -8.5, 21.5], aspect='auto')

    # Generar el mapa de calor encima de la imagen del entorno usando kdeplot de Seaborn
    sns.kdeplot(
        data["X"], data["Y"], 
        cmap="Reds",  # Cambia el color del mapa de calor si lo deseas
        shade=True,  # Activa el sombreado para el mapa de calor
        bw_adjust=0.5,  # Ajusta la suavidad del mapa de calor
        ax=ax,
        alpha=0.5  # Transparencia del mapa de calor
    )

    ax.set_title("Player Heatmap")
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
    output_filename = os.path.splitext(csv_filename)[0] + "_heatmap" + ".png"
    plt.savefig(output_filename, dpi=300, bbox_inches='tight', transparent=True)

# Mostrar las gráficas una vez que se han guardado todas
plt.show()