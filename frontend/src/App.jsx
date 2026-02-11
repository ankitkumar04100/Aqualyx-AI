import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
import Home from "./pages/Home";
import Analytics from "./pages/Analytics";
import Savings from "./pages/Savings";

export default function App() {
  return (
    <Router>
      <div className="min-h-screen bg-gray-50">
        <nav className="bg-primary text-white p-4 flex justify-between">
          <h1 className="font-bold text-xl">Aqualyx AI</h1>
          <div className="space-x-4">
            <Link to="/">Home</Link>
            <Link to="/analytics">Analytics</Link>
            <Link to="/savings">Savings</Link>
          </div>
        </nav>

        <div className="p-6">
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/analytics" element={<Analytics />} />
            <Route path="/savings" element={<Savings />} />
          </Routes>
        </div>
      </div>
    </Router>
  );
}
