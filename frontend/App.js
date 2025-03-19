import React, { useState } from 'react';

function App() {
    const [keywords, setKeywords] = useState('');
    const [popularityData, setPopularityData] = useState([]);
    const [loading, setLoading] = useState(false);

    const handleFetchTrends = async () => {
        setLoading(true);
        const response = await fetch(
            `/api/google-trends?keywords=${keywords.split(',').join('&keywords=')}`
        );
        const data = await response.json();
        setPopularityData(data);
        setLoading(false);
    };

    return (
        <div className="App">
            <h1>Fashion Trend Predictor</h1>
            <input
                type="text"
                value={keywords}
                onChange={(e) => setKeywords(e.target.value)}
                placeholder="Enter keywords (e.g., adidas sambas, ballet flats)"
            />
            <button onClick={handleFetchTrends}>Fetch Trends</button>

            {loading ? (
                <p>Loading...</p>
            ) : (
                <div>
                    {popularityData && Object.keys(popularityData).length > 0 ? (
                        <div>
                            <h2>Trend Popularity</h2>
                            {Object.entries(popularityData).map(([date, values], index) => (
                                <p key={index}>
                                    {date}: {JSON.stringify(values)}
                                </p>
                            ))}
                        </div>
                    ) : (
                        <p>No data available</p>
                    )}
                </div>
            )}
        </div>
    );
}

export default App;
