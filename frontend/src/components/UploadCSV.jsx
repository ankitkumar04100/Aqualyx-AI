import { useState } from "react";
import api from "../services/api";

export default function UploadCSV() {
  const [file, setFile] = useState(null);
  const [result, setResult] = useState(null);

  const handleUpload = async () => {
    if (!file) return;

    const formData = new FormData();
    formData.append("file", file);

    try {
      const response = await api.post("/upload", formData);
      setResult(response.data);
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <div className="bg-white p-6 rounded shadow">
      <input
        type="file"
        accept=".csv"
        onChange={(e) => setFile(e.target.files[0])}
      />
      <button
        onClick={handleUpload}
        className="bg-primary text-white px-4 py-2 rounded ml-2"
      >
        Upload & Analyze
      </button>

      {result && (
        <div className="mt-4">
          <p>Leak Probability: {result.leak_probability}</p>
          <p>Risk Level: {result.risk_level}</p>
        </div>
      )}
    </div>
  );
}
