import React, { useEffect, useState } from 'react';

const API_BASE = process.env.REACT_APP_API_URL || 'http://localhost:8000';

function Leaderboard() {
  const [entries, setEntries] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetch(`${API_BASE}/api/leaderboard/`)
      .then(res => {
        if (!res.ok) throw new Error(`HTTP ${res.status}`);
        return res.json();
      })
      .then(data => { setEntries(data); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, []);

  if (loading) return <div className="container mt-4"><div className="spinner-border text-primary" role="status"><span className="visually-hidden">Ładowanie...</span></div></div>;
  if (error) return <div className="container mt-4"><div className="alert alert-danger">Błąd: {error}</div></div>;

  return (
    <div className="container mt-4">
      <h2 className="h3 mb-4">Tablica wyników</h2>
      <div className="card">
        <div className="card-body">
          <table className="table table-striped table-bordered mb-0">
            <thead className="table-dark">
              <tr>
                <th>#</th>
                <th>Użytkownik</th>
                <th>Wynik</th>
              </tr>
            </thead>
            <tbody>
              {entries.length === 0 ? (
                <tr><td colSpan="3" className="text-center text-muted">Brak danych</td></tr>
              ) : (
                entries
                  .sort((a, b) => b.score - a.score)
                  .map((e, i) => (
                    <tr key={e.id}>
                      <td>{i + 1}</td>
                      <td>{e.user}</td>
                      <td><span className="badge bg-primary">{e.score}</span></td>
                    </tr>
                  ))
              )}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
}

export default Leaderboard;
