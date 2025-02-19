using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System.IO;

public class PositionRecorder : MonoBehaviour
{
    public GameObject player;

    private string filename;

    private List<float> posX = new List<float>();
    private List<float> posY = new List<float>();

    private bool dataExported;
    void Start()
    {
        dataExported = false;

        filename = Application.streamingAssetsPath + "\\" + "PositionData" + ".csv";
        //filename = Application.persistentDataPath + "\\" + "PositionData" + ".csv";

        InvokeRepeating("RecordPosition", 0, 0.0083f);
    }

    public void Update()
    {
        
    }

    void RecordPosition()
    {
        if (!dataExported)
        {
            posX.Add(player.transform.position.x);
            posY.Add(player.transform.position.z);
        }
    }

    /*void ExportData()
    {
        TextWriter tw = new StreamWriter(filename, false);

        tw.WriteLine("X" + ";" + "Y");

        for (int i = 0; i < posX.Count; i++)
        {
            tw.WriteLine(posX[i] + ";" + posY[i]);
        }

        tw.Close();
    }*/
}

