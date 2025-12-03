import React, { useState } from 'react';
import UploadForm from './components/UploadForm';
import ResultsGallery from './components/ResultsGallery';

function App() {
  const [isLoading, setIsLoading] = useState(false);
  const [results, setResults] = useState(null);
  const [taskId, setTaskId] = useState(null);

  const handleGenerate = async (logo, productImage, description) => {
    setIsLoading(true);

    const formData = new FormData();
    formData.append('logo', logo);
    formData.append('product_image', productImage);
    formData.append('product_description', description);

    try {
      const response = await fetch('http://localhost:8080/creative/generate', {
        method: 'POST',
        body: formData,
      });

      const data = await response.json();
      if (data.status === 'success') {
        setResults(data);
        setTaskId(data.task_id);
      }
    } catch (error) {
      console.error("Error generating creatives:", error);
      alert("Failed to generate creatives. Please try again.");
    } finally {
      setIsLoading(false);
    }
  };

  const handleDownload = () => {
    if (taskId) {
      window.location.href = `http://localhost:8080/creative/download/${taskId}`;
    }
  };

  return (
    <div className="app">
      <h1>Auto-Creative Engine</h1>
      <p className="subtitle">Generate high-quality brand assets in seconds using AI.</p>

      <UploadForm onGenerate={handleGenerate} isLoading={isLoading} />

      {isLoading && <div className="loader"></div>}

      <ResultsGallery results={results} onDownload={handleDownload} />
    </div>
  );
}

export default App;
