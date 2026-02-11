import { LineChart, Line, XAxis, YAxis, Tooltip, ResponsiveContainer } from "recharts";
import useWaterStore from "../store/useWaterStore";

export default function UsageChart() {
  const { prediction } = useWaterStore();

  if (!prediction) return null;

  return (
    <div className="bg-white p-6 rounded-2xl shadow-xl h-96">
      <h3 className="text-xl font-semibold mb-4">Usage Trend</h3>

      <ResponsiveContainer width="100%" height="100%">
        <LineChart data={prediction.usage_data}>
          <XAxis dataKey="time" />
          <YAxis />
          <Tooltip />
          <Line type="monotone" dataKey="usage" stroke="#0ea5e9" strokeWidth={3} />
        </LineChart>
      </ResponsiveContainer>
    </div>
  );
}
