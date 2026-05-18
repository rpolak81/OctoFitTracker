import React, { useEffect, useState } from 'react';

const CODESPACE_NAME = process.env.REACT_APP_CODESPACE_NAME || '';
const API_BASE = CODESPACE_NAME
  ? `https://${CODESPACE_NAME}-8000.app.github.dev`
  : (process.env.REACT_APP_API_URL || 'http://localhost:8000');

function Activities() {
  const [activities, setActivities] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetch(`${API_BASE}/api/activities/`)
      .then(res => {
        if (!res.ok) throw new Error(`HTTP ${res.status}`);
        return res.json();
      })
      .then(data => { setActivities(data); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, []);

  if (loading) return <div className="container mt-4"><div className="spinner-border text-primary" role="status"><span className="visually-hidden">Ładowanie...</span></div></div>;
  if (error) return <div className="container mt-4"><div className="alert alert-danger">Błąd: {error}</div></div>;

  return (
    <div className="container mt-4">
      <h2 className="h3 mb-4">Aktywności</h2>
      <div className="card">
        <div className="card-body">
          <table className="table table-striped table-bordered mb-0">
            <thead className="table-dark">
              <tr>
                <th>#</th>
                <th>Użytkownik</th>
                <th>Typ</th>
                <th>Czas (min)</th>
                <th>Data</th>
              </tr>
            </thead>
            <tbody>
              {activities.length === 0 ? (
                <tr><td colSpan="5" className="text-center text-muted">Brak aktywności</td></tr>
              ) : (
                activities.map((a, i) => (
                  <tr key={a.id}>
                    <td>{i + 1}</td>
                    <td>{a.user}</td>
                    <td>{a.type}</td>
                    <td>{a.duration}</td>
                    <td>{a.date}</td>
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

export default Activities;
