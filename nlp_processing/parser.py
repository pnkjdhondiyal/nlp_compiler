import spacy

nlp = spacy.load("en_core_web_sm")

def extract_info(sentence):
    doc = nlp(sentence)
    
    operations_map = {
        "add": ["add", "plus", "sum"],
        "subtract": ["subtract", "minus"],
        "multiply": ["multiply", "times"],
        "divide": ["divide"]
    }

    operation = None
    variables = []

    for token in doc:
        word = token.text.lower()
        
        # Ignore 'by' to avoid misinterpretation
        if word == "by":
            continue

        # Identify mathematical operations
        for key, synonyms in operations_map.items():
            if word in synonyms:
                operation = key
                break
        
        # Extract numbers
        if token.pos_ in ["NUM"]:
            variables.append(token.text)

    return {"operation": operation, "variables": variables}

# Example Usage
if __name__ == "__main__":
    print(extract_info("Multiply 4 by 6"))  # Expected: {'operation': 'multiply', 'variables': ['4', '6']}
    print(extract_info("Divide 100 by 4"))  # Expected: {'operation': 'divide', 'variables': ['100', '4']}
