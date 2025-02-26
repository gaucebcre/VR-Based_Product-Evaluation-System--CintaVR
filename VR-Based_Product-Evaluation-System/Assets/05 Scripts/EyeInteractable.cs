using UnityEngine;
using UnityEngine.Events;

[RequireComponent(typeof(Collider))]
[RequireComponent(typeof(Rigidbody))]

public class EyeInteractable : MonoBehaviour
{
    public bool IsHovered { get; set; }

    //public float dwellTime;
    public bool isHovered;

    void Start()
    {
        isHovered = false;
    }

    // Update is called once per frame
    void FixedUpdate()
    {
        if (IsHovered)
        {
            isHovered = true;
            //dwellTime += Time.deltaTime;
        }

        else
        {
            isHovered = false;
        }
    }
}
