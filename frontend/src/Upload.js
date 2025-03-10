import React, { useState } from "react";

function Upload({ setAnalysis }) {
  const [file, setFile] = useState(null);

  const handleUpload = async () => {
    const formData = new FormData();
    formData.append("file", file);

    const response = await fetch("http://localhost:5000/upload", {
      method: "POST",
      body: formData,
    });

    const result = await response.json();
    setAnalysis(result);
  };

  return (
    <div className="mt-4">
      <input type="file" onChange={(e) => setFile(e.target.files[0])} />
      <button onClick={handleUpload} className="bg-blue-500 text-white px-4 py-2 rounded mt-2">
        Upload & Analyze
      </button>
    </div>
  );
}

export default Upload;
