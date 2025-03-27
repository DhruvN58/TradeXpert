import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import { Dashboard } from "./pages/Dashboard";
import { Login } from "./pages/Login";
import { Trade } from "./pages/Trade";
import { PaperTrading } from "./pages/PaperTrading";
import { Navbar } from "./components/Navbar";
import { WebSocketProvider } from "./context/WebSocketContext";

function App() {
  return (
    <WebSocketProvider>
      <Router>
        <Navbar />
        <div className="container mx-auto p-4">
          <Routes>
            <Route path="/" element={<Dashboard />} />
            <Route path="/login" element={<Login />} />
            <Route path="/trade" element={<Trade />} />
            <Route path="/paper-trading" element={<PaperTrading />} />
          </Routes>
        </div>
      </Router>
    </WebSocketProvider>
  );
}

export default App;
