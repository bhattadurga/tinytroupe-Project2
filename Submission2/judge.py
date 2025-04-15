def evaluate_model(model_dict):
    # Simulated evaluation based on model score
    score = model_dict.get("metrics", 0)
    if score > 0.8:
        feedback = "Excellent model!"
    elif score > 0.5:
        feedback = "Good, but could be improved."
    else:
        feedback = "Model performance is low. Consider trying a different algorithm."

    return {
        "score": score,
        "suggestions": feedback
    }
