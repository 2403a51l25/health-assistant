def predict_disease(symptoms):
    fever, cough, headache, fatigue, bodypain, cold = symptoms

    # 🔴 STRICT SINGLE SYMPTOM RULES
    if fever and not cough and not headache and not fatigue and not bodypain and not cold:
        return "Fever Infection"

    if cough and not fever and not headache and not fatigue and not bodypain and not cold:
        return "Allergy"

    if headache and not fever and not cough and not fatigue and not bodypain and not cold:
        return "Migraine"

    if fatigue and not fever and not cough and not headache and not bodypain and not cold:
        return "Weakness"

    if bodypain and not fever and not cough and not headache and not fatigue and not cold:
        return "Body Pain Issue"

    if cold and not fever and not cough and not headache and not fatigue and not bodypain:
        return "Throat Infection"

    # 🟡 IMPORTANT COMBINATIONS
    if cough and cold and not fever:
        return "Throat Infection"

    if headache and fatigue:
        return "Stress"

    if fever and cough and cold:
        return "Common Cold"

    if fever and headache and bodypain:
        return "Dengue"

    if fever and bodypain:
        return "Typhoid"

    if fever and fatigue:
        return "Diabetes"

    # 🟢 FULL SYMPTOMS
    if fever and cough and headache and fatigue and bodypain and cold:
        return "Flu"

    # 🔵 FALLBACK LOGIC (best match)
    diseases = {
        "Flu":            [1,1,1,1,1,1],
        "Common Cold":    [1,1,0,1,0,1],
        "Allergy":        [0,1,1,0,0,1],
        "Migraine":       [0,0,1,1,1,0],
        "Stress":         [0,0,1,1,0,0],
        "Typhoid":        [1,0,0,1,1,0],
        "Dengue":         [1,1,1,1,1,0],
        "Weakness":       [0,0,0,1,0,0],
        "Diabetes":       [1,0,0,1,0,0],
        "Body Pain Issue":[0,0,0,0,1,1],
        "Fever Infection":[1,0,0,0,0,1],
        "Throat Infection":[0,1,0,0,0,1]
    }

    best_match = None
    max_score = -1

    for disease, pattern in diseases.items():
        score = sum([1 for i in range(len(symptoms)) if symptoms[i] == pattern[i]])

        if score > max_score:
            max_score = score
            best_match = disease

    return best_match