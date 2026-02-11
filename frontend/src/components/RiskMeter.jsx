export default function RiskMeter({ risk = 0.65 }) {
  const percentage = Math.round(risk * 100);

  return (
    <div className="bg-white p-6 rounded shadow">
      <h3 className="text-lg font-semibold mb-2">Leak Risk Level</h3>
      <div className="w-full bg-gray-200 rounded-full h-6">
        <div
          className={`h-6 rounded-full ${
            percentage > 70
              ? "bg-danger"
              : percentage > 40
              ? "bg-yellow-400"
              : "bg-success"
          }`}
          style={{ width: `${percentage}%` }}
        />
      </div>
      <p className="mt-2 font-bold">{percentage}% Risk</p>
    </div>
  );
}
