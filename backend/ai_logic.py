# backend/ai_logic.py
# Contains the core "AI" behavior.
# For this prototype, we implement a rule-based, supportive response generator.
# This makes behavior transparent for examiners and avoids the need for a real LLM.

from typing import Tuple


# List of crisis keywords that trigger the safety layer.
CRISIS_KEYWORDS = [
    "suicide",
    "kill myself",
    "self harm",
    "self-harm",
    "harm myself",
    "want to die",
    "die",
    "end it all",
]


def check_crisis(message: str) -> bool:
    """
    Check if the message contains any crisis-related terms.
    This is a simple keyword-based safety layer (can be extended with NLP later).
    """
    lowered = message.lower()
    for kw in CRISIS_KEYWORDS:
        if kw in lowered:
            return True
    return False


def generate_crisis_response() -> str:
    """
    Return a crisis response encouraging the user to seek immediate professional help.
    IMPORTANT: No normal AI conversation when this is triggered.
    """
    return (
        "It sounds like you might be going through something very serious and painful right now. "
        "I am not a crisis service or a substitute for professional care. "
        "If you are in immediate danger or thinking about harming yourself, please contact your local emergency number right away. "
        "You can also reach out to a trusted person in your life or a licensed mental health professional as soon as possible. "
        "If available in your country, you may also contact a suicide prevention or mental health crisis hotline."
    )


def generate_supportive_response(message: str) -> str:
    """
    Generate a structured, supportive response without giving any diagnosis.
    The structure follows:
      1. Emotional validation
      2. Normalization / optimism
      3. Simple, practical coping suggestions
      4. Gentle encouragement for professional support (non-urgent)
    """
    # Simple heuristics to adapt tone slightly based on keywords.
    lowered = message.lower()

    if any(word in lowered for word in ["anxious", "anxiety", "worried", "nervous"]):
        feeling = "anxious"
    elif any(word in lowered for word in ["sad", "down", "low", "depressed", "upset"]):
        feeling = "down"
    elif any(word in lowered for word in ["angry", "frustrated", "irritated"]):
        feeling = "frustrated"
    else:
        feeling = "overwhelmed"

    # 1. Emotional validation
    part1 = (
        f"Thank you for sharing this with me. From what you wrote, it sounds like you might be feeling {feeling}, "
        "and that can be really hard to carry on your own."
    )

    # 2. Normalization / optimism
    part2 = (
        "Your feelings are valid, and many people go through moments like this. "
        "Even though it may not feel like it right now, it is possible for things to become more manageable over time."
    )

    # 3. Simple coping strategies
    part3 = (
        "For the next little while, you might try one or two small steps: "
        "take a few slow, deep breaths, have a glass of water, gently stretch your body, "
        "or take a short walk if that is accessible and safe for you. "
        "Sometimes writing down what you are feeling or breaking big problems into smaller pieces can also help."
    )

    # 4. Gentle encouragement for professional help
    part4 = (
        "I am here to offer support and reflection, but I am not a therapist and I cannot provide any diagnosis. "
        "If these feelings keep coming back or interfere with your daily life, it could be helpful to talk with a qualified mental health professional "
        "or someone you trust in your life."
    )

    return " ".join([part1, part2, part3, part4])


def process_message(message: str) -> Tuple[str, bool]:
    """
    Main entry point for the backend:
    - Check for crisis content.
    - If crisis, return crisis response and mark as is_crisis=True.
    - Otherwise, return a supportive, non-diagnostic response.
    """
    if check_crisis(message):
        return generate_crisis_response(), True
    else:
        return generate_supportive_response(message), False
