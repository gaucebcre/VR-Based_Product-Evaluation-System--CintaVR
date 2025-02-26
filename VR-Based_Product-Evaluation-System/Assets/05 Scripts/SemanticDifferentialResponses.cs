using Oculus.Interaction;
using System.Collections;
using System.Collections.Generic;
using System.IO;
using UnityEngine;
using UnityEngine.UI;
using UnityEngine.XR.OpenXR.Input;

public class SemanticDifferentialResponses : MonoBehaviour
{
    [Header("Semantic scales")]
    public GameObject[] semanticScales;
    public Slider evaluationSlider;

    [Header("Responses")]    
    public List<float> evaluationResponses = new List<float>();

    [Header("Export data to HMD?")]
    public bool toHMD = false;

    [Header("Other")]
    public int counter;
    private GameObject manager;
    private string filename;
    private bool dataExported = false;

    void Start()
    {
        manager = GameObject.FindGameObjectWithTag("Manager");

        for (int i = 1; i < semanticScales.Length; i++)
        {
            semanticScales[i].SetActive(false);
        }

        counter = 0;
    }

    void Update()
    {
        if (!toHMD)
        {
            filename = Application.streamingAssetsPath + "\\" + manager.GetComponent<Manager>().userCode + "_Semantic-Differential" + ".csv";
        }

        else
        {
            filename = Application.persistentDataPath + "\\" + manager.GetComponent<Manager>().userCode + "_Semantic-Differential" + ".csv";
        }

        if (!dataExported && counter == semanticScales.Length)
        {            
            ExportData();
            dataExported = true;
        }
    }

    public void NextSemanticScale()
    {
        if (counter < semanticScales.Length)
        {
            evaluationResponses.Add(evaluationSlider.value);
            evaluationSlider.value = 0;
            semanticScales[counter].SetActive(false);
            counter++;

            if (counter < semanticScales.Length)
            {
                semanticScales[counter].SetActive(true);
            }

            else
            {
                //Change canvas position, as disabling it stops data exportation
                gameObject.transform.position = new Vector3(0, -2, 0);
            }
        }
    }

    public void PreviousSemanticScale()
    {
        if (counter >= 1)
        {
            evaluationResponses.RemoveAt(counter - 1);
            evaluationSlider.value = 0;
            semanticScales[counter].SetActive(false);
            counter--;
            semanticScales[counter].SetActive(true);
        }
    }

    public void ExportData()
    {
        Debug.Log("Exporting data");

        TextWriter tw = new StreamWriter(filename, false);

        tw.WriteLine("Scale" + ";" + "Value");

        for (int i = 0; i < evaluationResponses.Count; i++)
        {
            tw.WriteLine("SD" + (i + 1) + ";" + evaluationResponses[i]);
        }

        tw.Close();

        Debug.Log("Data exported");
    }
}
