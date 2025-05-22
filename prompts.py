def generate_prompt(topic, level):
    if level == "Beginner":
        return f"Explain the concept of {topic} like I'm 5 years old. Use simple language and analogies."
    elif level == "Intermediate":
        return f"Explain the concept of {topic} to a high school student. Be clear, use real-world examples."
    else:
        return f"Explain the concept of {topic} to a college-level student. Include technical terms and a formal explanation."
