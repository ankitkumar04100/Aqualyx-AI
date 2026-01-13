import React, { useState } from "react";
import RiskMeter from "./RiskMeter";
import UsageGraph from "./UsageGraph";
import axios from "axios";

function Dashboard() {
  const [data, setData] = useState([]);

  const handleFileUpload = async (event) => {
    const formData = new FormData();
    formData.append("file", event.target.files[0]);
    const response = await axios.post("https://your-backend-url/predict", formData);
    setData(response.data);
  };

  return (
    <div className="p-4">
      <h1 className="text-2xl font-bold mb-4">Aqualyx AI Dashboard</h1>
      <input type="file" onChange={handleFileUpload} />
      <RiskMeter data={data} />
      <UsageGraph data={data} />
    </div>
  );
}

export default Dashboard;
