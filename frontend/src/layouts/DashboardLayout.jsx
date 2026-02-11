import { Link } from "react-router-dom";

export default function DashboardLayout({ children }) {
  return (
    <div className="flex min-h-screen bg-gray-100">
      
      <aside className="w-64 bg-white shadow-lg p-6">
        <h1 className="text-2xl font-bold mb-8 text-primary">
          Aqualyx AI
        </h1>
        <nav className="space-y-4">
          <Link to="/" className="block hover:text-primary">Dashboard</Link>
          <Link to="/analytics" className="block hover:text-primary">Analytics</Link>
          <Link to="/savings" className="block hover:text-primary">Impact</Link>
        </nav>
      </aside>

      <main className="flex-1 p-8">
        {children}
      </main>

    </div>
  );
}
