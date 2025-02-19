using TMPro;
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

    void Start()
    {
        //Don't destroy
        DontDestroyOnLoad(this.gameObject);
        DontDestroyOnLoad(player);

        //Save first code
        userCode = letterDropdown.text + numberDropdown.text;
    }

    void Update()
    {
        
    }

    public void ChangeScene()
    {
        if (!string.IsNullOrEmpty(sceneName))
        {
            SceneManager.LoadScene(sceneName);
        }
        else
        {
            Debug.LogWarning("Scene name is not set!");
        }
    }

    public void SaveUserCode()
    {
       userCode = letterDropdown.text + numberDropdown.text;
    }
}
