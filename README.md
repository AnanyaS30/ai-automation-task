
# AI Automation Task

This project analyzes code files for clean code practices and provides recommendations for improvement. It includes a frontend built with React and a backend built with FastAPI.

## Tech Stack
- Frontend: React
- Backend: FastAPI
- Code Analysis Tools: pylint, radon, flake8

## Setup Instructions

### Prerequisites
- Node.js and npm
- Python 3.x
- Git

### Clone the Repository
1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/your-username/ai-automation-task.git
   cd ai-automation-task
   ```

### Set Up the Frontend
1. Navigate to the `frontend` directory:
   ```bash
   cd frontend
   ```

2. Install the dependencies:
   ```bash
   npm install
   ```

3. Start the React app:
   ```bash
   npm start
   ```

### Set Up the Backend
1. Navigate to the `backend` directory:
   ```bash
   cd ../backend
   ```

2. Set up a virtual environment:
   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```bash
     .\venv\Scripts\activate
     ```

4. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. Start the FastAPI server:
   ```bash
   uvicorn main:app --reload
   ```

## Usage Instructions
1. Open your browser and navigate to `http://localhost:3000`.
2. Use the file upload form to upload a `.py` file.
3. Submit the form to analyze the uploaded file.
4. The analysis results, including the overall score, breakdown, and recommendations, will be displayed on the page.

## What This Tool Does
This tool analyzes Python code files to evaluate their adherence to clean code practices. It provides a comprehensive analysis based on several criteria and offers actionable recommendations for improvement. The analysis includes:

Overall Score: A score out of 100 that reflects the overall quality of the code.
Breakdown: Scores for specific categories such as naming conventions, function length and modularity, comments and documentation, formatting/indentation, reusability and DRY principles, and best practices in web development.
Recommendations: Clear and actionable suggestions for improving the code quality.

## Example Input and Output

### Example Input
File: `complex_function.py`
  def calculate_total(orders):
    total = 0
    for order in orders:
        total += order["value"]
    return total

### Expected Output
```json
{
  "overall_score": 90,
  "breakdown": {
    "naming": 10,
    "modularity": 20,
    "comments": 20,
    "formatting": 15,
    "reusability": 15,
    "best_practices": 20
  },
  "recommendations": [
    "Add docstrings to your functions."
  ]
}
```

## Testing
1. Created a directory named `test_files` in the root of the project.
2. Add sample Python files to the `test_files` directory.
3. Upload these files through the React frontend and verify the analysis results.

## Optional Enhancements
- **GitHub Actions**: Add a GitHub Action to automate code quality checks on every commit. Create a `.github/workflows/code-quality.yml` file:
  ```yaml
  name: Code Quality

  on: [push, pull_request]

  jobs:
    lint:
      runs-on: ubuntu-latest

      steps:
      - uses: actions/checkout@v2
      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: 3.x
      - name: Install dependencies
        run: |
          python -m venv venv
          source venv/bin/activate
          pip install pylint radon flake8
      - name: Lint with pylint
        run: |
          source venv/bin/activate
          pylint **/*.py
      - name: Check complexity with radon
        run: |
          source venv/bin/activate
          radon cc **/*.py
      - name: Check style with flake8
        run: |
          source venv/bin/activate
          flake8 **/*.py
  ```

## Conclusion

This AI Automation Task project provides a robust tool for analyzing Python code files to ensure adherence to clean code practices. By leveraging powerful code analysis tools such as pylint, radon, and flake8, the tool evaluates various aspects of the code, including naming conventions, modularity, comments, formatting, reusability, and best practices. The comprehensive analysis results, along with actionable recommendations, help developers improve their code quality and maintainability.

With a user-friendly frontend built in React and a scalable backend powered by FastAPI, this project offers an efficient and effective solution for code quality assessment. The optional GitHub Actions integration further enhances the workflow by automating code quality checks on every commit, ensuring continuous improvement and adherence to coding standards.
