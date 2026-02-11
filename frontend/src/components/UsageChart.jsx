import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  Tooltip,
  ResponsiveContainer
} from "recharts";

const data = [
  { time: "1AM", usage: 0.5 },
  { time: "6AM", usage: 1.2 },
  { time: "9AM", usage: 3.5 },
  { time: "12PM", usage: 1.8 },
  { time: "6PM", usage: 2.1 }
];

export default function UsageChart() {
  return (
    <div className="bg-white p-6 rounded shadow h-80">
      <h3 className="text-lg font-semibold mb-4">Water Usage Trend</h3>
      <ResponsiveContainer width="100%" height="100%">
        <LineChart data={data}>
          <XAxis dataKey="time" />
          <YAxis />
          <Tooltip />
          <Line type="monotone" dataKey="usage" stroke="#0ea5e9" />
        </LineChart>
      </ResponsiveContainer>
    </div>
  );
}
