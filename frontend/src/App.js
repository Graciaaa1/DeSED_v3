import React, { useState } from "react";
import Upload from "./Upload";
import Results from "./Results";

function App() {
  const [analysis, setAnalysis] = useState(null);

  return (
    <div className="min-h-screen flex flex-col items-center justify-center bg-gray-100">
      <h1 className="text-3xl font-bold text-blue-600">Voice Depression Detector</h1>
      <Upload setAnalysis={setAnalysis} />
      {analysis && <Results analysis={analysis} />}
    </div>
  );
}

export default App;
