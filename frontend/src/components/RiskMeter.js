import React from "react";

function RiskMeter({ data }) {
  return (
    <div>
      <h2 className="text-xl font-semibold">Leak Risk Overview</h2>
      <ul>
        {data.map((d, index) => (
          <li key={index}>{d.timestamp}: {d.Leak_Risk}</li>
        ))}
      </ul>
    </div>
  );
}

export default RiskMeter;
