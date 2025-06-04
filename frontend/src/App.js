import React, { useState } from 'react';

function App() {
  const [player1, setPlayer1] = useState(null);
  const [player2, setPlayer2] = useState(null);
  const [id1, setId1] = useState('');
  const [id2, setId2] = useState('');

  const fetchData = async () => {
    const res1 = await fetch(`http://localhost:8000/players/${id1}`);
    const res2 = await fetch(`http://localhost:8000/players/${id2}`);
    if (res1.ok) setPlayer1(await res1.json());
    if (res2.ok) setPlayer2(await res2.json());
  };

  return (
    <div>
      <h1>Soccer Player Compare</h1>
      <input placeholder="Player 1 ID" value={id1} onChange={e => setId1(e.target.value)} />
      <input placeholder="Player 2 ID" value={id2} onChange={e => setId2(e.target.value)} />
      <button onClick={fetchData}>Compare</button>
      {player1 && player2 && (
        <div>
          <h2>{player1.name} vs {player2.name}</h2>
          <p>Goals: {player1.goals} vs {player2.goals}</p>
          <p>Assists: {player1.assists} vs {player2.assists}</p>
        </div>
      )}
    </div>
  );
}

export default App;
