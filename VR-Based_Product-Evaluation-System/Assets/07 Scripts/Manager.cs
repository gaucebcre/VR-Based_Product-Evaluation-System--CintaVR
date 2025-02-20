using TMPro;
using Unity.VisualScripting;
using UnityEngine;
using UnityEngine.SceneManagement;
using UnityEngine.UI;

public class Manager : MonoBehaviour
{
    [Header("Player")]
    public GameObject player;

    [Header("Scene name")]
    public string sceneName;

    [Header("User code")]
    public string userCode;

    [Header("Other")]
    public TextMeshProUGUI letterDropdown;
    public TextMeshProUGUI numberDropdown;
    public GameObject semanticDifferential;

    private bool evaluationStarted;

    void Start()
    {
        //Don't destroy
        DontDestroyOnLoad(this.gameObject);
        DontDestroyOnLoad(player);

        //Save first code
        userCode = letterDropdown.text + numberDropdown.text;

        evaluationStarted = false;
    }

    void Update()
    {
        StartEvaluation();
    }

    public void ChangeScene()
    {
        if (!string.IsNullOrEmpty(sceneName))
        {
            SceneManager.LoadScene(sceneName);
        }
    }

    public void SaveUserCode()
    {
       userCode = letterDropdown.text + numberDropdown.text;
    }

    public void StartEvaluation()
    {
        if (SceneManager.GetActiveScene().name == "Evaluation-scene" && !evaluationStarted)
        {
            player.GetComponent<PositionRecorder>().enabled = true;
            gameObject.GetComponent<EyeTrackingRecorder>().enabled = true;

            if (semanticDifferential == null)
            {
                semanticDifferential = GameObject.FindGameObjectWithTag("SemanticDifferential");
                semanticDifferential.SetActive(false);
            }

            evaluationStarted = true;
        }
        
        else if (evaluationStarted && OVRInput.GetDown(OVRInput.Button.One))
        {
            semanticDifferential.SetActive(true);
            player.GetComponent<PositionRecorder>().enabled = false;
            gameObject.GetComponent<EyeTrackingRecorder>().enabled = false;
        }
    }
}
