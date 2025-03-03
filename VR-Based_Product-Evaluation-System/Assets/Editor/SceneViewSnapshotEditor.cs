using UnityEngine;
using UnityEditor;

[CustomEditor(typeof(SceneViewSnapshot))]
public class SceneViewSnapshotEditor : Editor
{
    public override void OnInspectorGUI()
    {
        base.OnInspectorGUI();

        SceneViewSnapshot sceneViewSnapshot = (SceneViewSnapshot)target;

        // Agregar un botón de captura al Editor
        if (GUILayout.Button("Capturar Snapshot"))
        {
            sceneViewSnapshot.CaptureScreenshot(); // Llamar a la función de captura
            Debug.Log("Captura realizada desde el Editor.");
        }
    }
}

