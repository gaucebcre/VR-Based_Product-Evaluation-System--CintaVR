using UnityEngine;
using System.Collections;
using System.IO;
using System.Globalization;

public class CSVObjectSpawner : MonoBehaviour
{
    // Asignar el archivo CSV en el inspector
    public TextAsset csvFile;

    // Prefab que se generará en las posiciones indicadas en el CSV
    public GameObject prefabToSpawn;

    // Método para leer el CSV y generar los objetos en las posiciones indicadas
    public void GenerateObjectsFromCSV()
    {
        // Verificar si el archivo CSV y el prefab están asignados
        if (csvFile == null || prefabToSpawn == null)
        {
            Debug.LogError("Por favor, asigna un archivo CSV y un prefab.");
            return;
        }

        // Leer las líneas del archivo CSV
        string[] lines = csvFile.text.Split(new char[] { '\n' });

        // Comenzar desde la segunda línea para ignorar la cabecera
        for (int i = 1; i < lines.Length; i++)
        {
            string line = lines[i];

            // Evitar líneas vacías
            if (string.IsNullOrEmpty(line))
                continue;

            // Separar las columnas del CSV usando el punto y coma como separador
            string[] columns = line.Split(';');

            // Verificar que haya al menos dos columnas (X y Y)
            if (columns.Length < 2)
            {
                Debug.LogWarning("La línea " + i + " no tiene suficientes columnas.");
                continue;
            }

            // Configurar la cultura para que reconozca la coma como separador decimal
            var cultureInfo = new CultureInfo("es-ES"); // Cultura española
            cultureInfo.NumberFormat.CurrencyDecimalSeparator = ",";

            // Convertir los valores de X y Y a float usando la cultura española
            if (float.TryParse(columns[0], NumberStyles.Any, cultureInfo, out float x) &&
                float.TryParse(columns[1], NumberStyles.Any, cultureInfo, out float y))
            {
                // Crear una nueva posición usando los valores del CSV (X, Z)
                Vector3 position = new Vector3(x, 0, y);

                // Instanciar el prefab en la posición indicada
                Debug.Log($"Generando objeto en la posición: {position}");
                Instantiate(prefabToSpawn, position, Quaternion.identity);
            }
            else
            {
                Debug.LogWarning("Error al leer las coordenadas en la línea " + i);
            }
        }

        // Mensaje de finalización
        Debug.Log("Generación de objetos completada.");
    }

    // Método para ejecutar la generación en el Editor de Unity (puedes invocar esto desde el Inspector)
    [ContextMenu("Generar Objetos Desde CSV")]
    private void GenerateObjects()
    {
        GenerateObjectsFromCSV();
    }
}





