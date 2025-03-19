import React, { useEffect, useState } from "react";
import axios from "axios";

function App() {
  const [trendData, setTrendData] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchTrends = async () => {
      try {
        const response = await axios.get("http://127.0.0.1:5000/api/trends");
        setTrendData(response.data);
        setLoading(false);
      } catch (error) {
        console.error("Error fetching trends data:", error);
        setLoading(false);
      }
    };
    fetchTrends();
  }, []);

  return (
    <div className="App">
      <h1>Google Trends for "Adidas Sambas"</h1>
      {loading ? (
        <p>Loading...</p>
      ) : trendData ? (
        <table>
          <thead>
            <tr>
              <th>Date</th>
              <th>Popularity</th>
            </tr>
          </thead>
          <tbody>
            {Object.entries(trendData["adidas sambas"]).map(([date, value]) => (
              <tr key={date}>
                <td>{date}</td>
                <td>{value}</td>
              </tr>
            ))}
          </tbody>
        </table>
      ) : (
        <p>No data available</p>
      )}
    </div>
  );
}

export default App;
