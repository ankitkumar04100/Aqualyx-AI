import UploadCSV from "../components/UploadCSV";

export default function Home() {
  return (
    <div>
      <h2 className="text-2xl font-bold mb-4">Water Leak Prediction</h2>
      <UploadCSV />
    </div>
  );
}
