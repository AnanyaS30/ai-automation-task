from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from radon.complexity import cc_visit
import uvicorn
import subprocess
import os
import json
import re

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this to your needs
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Function to analyze the code using pylint
def parse_pylint_output(pylint_output):
    naming_score = 10  # Default naming score
    comments_score = 20  # Default comments score
    docstring_warning = re.search(r'C0116', pylint_output)  # Look for missing docstrings
    naming_warning = re.search(r'C0103', pylint_output)  # Look for non-conforming names
    
    if docstring_warning:
        comments_score = 5  # Lower comments score if docstring is missing

    if naming_warning:
        naming_score = 5  # Lower naming score if naming convention is wrong
    
    return naming_score, comments_score

# Function to analyze the code using radon (complexity)
def analyze_with_radon(file_content):
    results = cc_visit(file_content.decode("utf-8"))
    complexity_score = sum([cc.complexity for cc in results])  # Sum all function complexities
    modularity_score = 20 if complexity_score < 10 else 10  # Penalize if complexity is high
    print(f"Radon Complexity Output: {results}")
    return modularity_score

# Function to calculate scores from pylint and radon outputs
def calculate_score(pylint_output, radon_output):
    naming_score, comments_score = parse_pylint_output(pylint_output)
    modularity_score = analyze_with_radon(radon_output)
    overall_score = naming_score + modularity_score + comments_score + 40  # Adjust as needed

    return {
        "overall_score": overall_score,
        "breakdown": {
            "naming": naming_score,
            "modularity": modularity_score,
            "comments": comments_score,
            "formatting": 12,  # Placeholder
            "reusability": 10,  # Placeholder
            "best_practices": 15  # Placeholder
        },
        "recommendations": [
            "Use snake_case for function names.",
            "Add docstrings to your functions.",
            "Avoid deeply nested functions."
        ]
    }

# Main endpoint to analyze the code
@app.post("/analyze-code")
async def analyze_code(file: UploadFile = File(...)):
    content = await file.read()
    print(f"Received file content: {content.decode('utf-8')}")
    
    # Run analysis
    pylint_output = analyze_with_pylint(content)
    radon_output = analyze_with_radon(content)
    result = calculate_score(pylint_output, radon_output)
    
    # Return the result as JSON
    return json.dumps(result)


# Run the FastAPI app using Uvicorn
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
