import React from 'react';

function LiveTracker({ trendData }) {
  if (!trendData || Object.keys(trendData).length === 0) {
    return <p>No trend data available</p>;
  }

  return (
    <div>
      <h2>Live Tracker for Google Trends</h2>
      <table>
        <thead>
          <tr>
            <th>Date</th>
            <th>Interest Level</th>
          </tr>
        </thead>
        <tbody>
          {Object.entries(trendData).map(([date, value]) => (
            <tr key={date}>
              <td>{date}</td>
              <td>{value["adidas sambas"]}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default LiveTracker;
