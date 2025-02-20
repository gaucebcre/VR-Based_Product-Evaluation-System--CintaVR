using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System.IO;

public class PositionRecorder : MonoBehaviour
{
    [Header("Player")]
    public GameObject player;

    [Header("Frequence (hz)")]
    [Tooltip("In hertz)")]
    public int frequence = 120;
    private float realFrequency;

    [Header("Is data exported?")]
    public bool dataExported = false;
    public bool dataAvailable = false;

    private string filename;
    private List<float> posX = new();
    private List<float> posY = new();    

    void Start()
    {
        filename = Application.streamingAssetsPath + "\\" + gameObject.GetComponent<Manager>().userCode + "_Position-Data" + ".csv";
        //filename = Application.persistentDataPath + "\\" + gameObject.GetComponent<Manager>().userCode + "_Position-Data" + ".csv";

        UpdateInvoke();
    }

    void UpdateInvoke()
    {
        if (frequence <= 0)
        {
            return;
        }

        realFrequency = 1f / frequence;
        CancelInvoke("RecordPosition");
        InvokeRepeating("RecordPosition", 0, realFrequency);
    }

    public void Update()
    {
        if (dataExported && !dataAvailable)
        {
            ExportData();
            dataAvailable = true;
        }
    }

    void RecordPosition()
    {
        if (!dataExported)
        {
            posX.Add(player.transform.position.x);
            posY.Add(player.transform.position.z);
        }
    }

    void ExportData()
    {
        TextWriter tw = new StreamWriter(filename, false);

        tw.WriteLine("X" + ";" + "Y");

        for (int i = 0; i < posX.Count; i++)
        {
            tw.WriteLine(posX[i] + ";" + posY[i]);
        }

        tw.Close();
    }
}

