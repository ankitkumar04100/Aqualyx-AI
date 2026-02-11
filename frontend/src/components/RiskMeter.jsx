import useWaterStore from "../store/useWaterStore";

export default function RiskMeter() {
  const { prediction } = useWaterStore();

  if (!prediction) return null;

  const percentage = Math.round(prediction.leak_probability * 100);

  const color =
    percentage > 70
      ? "bg-red-500"
      : percentage > 40
      ? "bg-yellow-400"
      : "bg-green-500";

  return (
    <div className="bg-white p-6 rounded-2xl shadow-xl">
      <h3 className="text-xl font-semibold mb-4">Leak Risk Level</h3>

      <div className="w-full bg-gray-200 rounded-full h-6">
        <div
          className={`h-6 rounded-full ${color} transition-all duration-500`}
          style={{ width: `${percentage}%` }}
        />
      </div>

      <p className="mt-3 font-bold text-lg">{percentage}% Risk</p>
    </div>
  );
}
