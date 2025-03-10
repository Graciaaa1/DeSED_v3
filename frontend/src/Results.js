import React from "react";

function Results({ analysis }) {
  return (
    <div className="mt-6 bg-white p-4 rounded-lg shadow-lg">
      <h2 className="text-xl font-bold">Analysis Results</h2>
      <p className="mt-2">
        <strong>Prediction:</strong> {analysis.prediction}
      </p>
      <p>
        <strong>Accuracy:</strong> {(analysis.accuracy * 100).toFixed(2)}%
      </p>
    </div>
  );
}

export default Results;
