import React, { useState } from "react";
import axios from "axios"; // Make sure you have axios installed (`npm install axios`)

const App = () => {
  const [file, setFile] = useState(null);
  const [analysisResult, setAnalysisResult] = useState(null);
  const [loading, setLoading] = useState(false);

  // Handle file change
  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  // Handle file upload and analysis
  const handleFileUpload = async () => {
    if (!file) return;

    setLoading(true);

    const formData = new FormData();
    formData.append("file", file);

    try {
      const response = await axios.post("http://localhost:8000/analyze-code", formData, {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      });
      setAnalysisResult(response.data); // Set the result from the backend
    } catch (error) {
      console.error("Error during file upload and analysis:", error);
    }

    setLoading(false);
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>Python Code Analyzer</h1>

        {/* File upload input */}
        <div className="upload-container">
          <input type="file" className="file-input" onChange={handleFileChange} />
          <button
            className="upload-button"
            onClick={handleFileUpload}
            disabled={loading}
          >
            {loading ? "Analyzing..." : "Upload and Analyze"}
          </button>
        </div>

        {/* Display analysis result */}
        {analysisResult && (
          <div className="analysis-result">
            <h2>Analysis Results</h2>
            <pre>{JSON.stringify(analysisResult, null, 2)}</pre>
          </div>
        )}
      </header>
    </div>
  );
};

export default App;
