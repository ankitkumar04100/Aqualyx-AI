import useWaterStore from "../store/useWaterStore";

export default function AIExplanation() {
  const { prediction } = useWaterStore();

  if (!prediction) return null;

  return (
    <div className="bg-white p-6 rounded-2xl shadow-xl">
      <h3 className="text-xl font-semibold mb-4">
        🤖 Why This Risk Was Predicted
      </h3>

      <ul className="list-disc pl-6 space-y-2">
        <li>Sudden spike of {prediction.spike_percent}% detected</li>
        <li>Usage exceeded historical average</li>
        <li>Unusual nighttime water activity</li>
      </ul>
    </div>
  );
}
