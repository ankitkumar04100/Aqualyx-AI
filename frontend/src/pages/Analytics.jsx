import UsageChart from "../components/UsageChart";
import RiskMeter from "../components/RiskMeter";

export default function Analytics() {
  return (
    <div className="space-y-6">
      <RiskMeter />
      <UsageChart />
    </div>
  );
}
