using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class SemanticDifferentialResponses : MonoBehaviour
{
    [Header("Semantic scales")]
    public GameObject[] semanticScales;
    public Slider evaluationSlider;

    [Header("Responses")]
    public List<float> evaluationResponses = new List<float>();

    private int counter;

    void Start()
    {
        for (int i = 1; i < semanticScales.Length; i++)
        {
            semanticScales[i].SetActive(false);
        }

        counter = 0;
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
                gameObject.SetActive(false);
            }
        }
    }

    public void PreviousSemanticScale()
    {
        if (counter >= 1)
        {
            evaluationResponses.RemoveAt(counter - 1);
            semanticScales[counter].SetActive(false);
            counter--;
            semanticScales[counter].SetActive(true);
        }
    }
}
