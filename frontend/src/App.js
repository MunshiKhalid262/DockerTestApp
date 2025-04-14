import React, { useEffect, useState } from 'react';

function App() {
  const [data, setData] = useState("");

  useEffect(() => {
    fetch(`${process.env.REACT_APP_API_URL}/`)
      .then(res => res.json())
      .then(data => setData(data.message))
      .catch(err => console.error("API fetch error:", err));
  }, []);
  

  return (
    <div>
      <h1>{data}</h1>
    </div>
  );
}

export default App;
