
import React, { useState } from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import logo from './octofitapp-small.png';


function App() {
  const [showModal, setShowModal] = useState(false);

  return (
    <div>
      {/* Bootstrap Navbar */}
      <nav className="navbar navbar-expand-lg navbar-dark bg-primary">
        <div className="container-fluid">
          <a className="navbar-brand d-flex align-items-center" href="#">
            <img src={logo} alt="OctoFit Logo" className="octofit-logo me-2" />
            OctoFit Tracker
          </a>
          <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
            <span className="navbar-toggler-icon"></span>
          </button>
          <div className="collapse navbar-collapse" id="navbarNav">
            <ul className="navbar-nav">
              <li className="nav-item">
                <a className="nav-link active" aria-current="page" href="#">Home</a>
              </li>
              <li className="nav-item">
                <a className="nav-link" href="#">Teams</a>
              </li>
              <li className="nav-item">
                <a className="nav-link" href="#">Activities</a>
              </li>
              <li className="nav-item">
                <a className="nav-link" href="#">Leaderboard</a>
              </li>
            </ul>
          </div>
        </div>
      </nav>

      <div className="container mt-4">
        {/* Bootstrap Heading */}
        <h1 className="display-4 mb-4">Witamy w OctoFit Tracker!</h1>

        {/* Bootstrap Card */}
        <div className="card mb-4">
          <div className="card-body">
            <h5 className="card-title">Twój postęp</h5>
            <p className="card-text">Monitoruj swoje aktywności i rywalizuj z innymi!</p>
            <button className="btn btn-primary" onClick={() => setShowModal(true)}>Dodaj Aktywność</button>
          </div>
        </div>

        {/* Bootstrap Table */}
        <h2 className="h4">Ostatnie aktywności</h2>
        <table className="table table-striped table-bordered">
          <thead className="table-dark">
            <tr>
              <th>#</th>
              <th>Typ</th>
              <th>Czas (min)</th>
              <th>Data</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>1</td>
              <td>Bieganie</td>
              <td>30</td>
              <td>2024-05-18</td>
            </tr>
            <tr>
              <td>2</td>
              <td>Rower</td>
              <td>45</td>
              <td>2024-05-17</td>
            </tr>
          </tbody>
        </table>

        {/* Bootstrap Link */}
        <a href="#" className="btn btn-link">Zobacz wszystkie aktywności</a>

        {/* Bootstrap Modal */}
        {showModal && (
          <div className="modal show d-block" tabIndex="-1" role="dialog">
            <div className="modal-dialog" role="document">
              <div className="modal-content">
                <div className="modal-header">
                  <h5 className="modal-title">Dodaj Aktywność</h5>
                  <button type="button" className="btn-close" aria-label="Close" onClick={() => setShowModal(false)}></button>
                </div>
                <div className="modal-body">
                  {/* Bootstrap Form */}
                  <form>
                    <div className="mb-3">
                      <label htmlFor="activityType" className="form-label">Typ aktywności</label>
                      <input type="text" className="form-control" id="activityType" placeholder="np. Bieganie" />
                    </div>
                    <div className="mb-3">
                      <label htmlFor="duration" className="form-label">Czas (min)</label>
                      <input type="number" className="form-control" id="duration" placeholder="np. 30" />
                    </div>
                    <div className="mb-3">
                      <label htmlFor="date" className="form-label">Data</label>
                      <input type="date" className="form-control" id="date" />
                    </div>
                  </form>
                </div>
                <div className="modal-footer">
                  <button type="button" className="btn btn-secondary" onClick={() => setShowModal(false)}>Anuluj</button>
                  <button type="button" className="btn btn-primary">Zapisz</button>
                </div>
              </div>
            </div>
          </div>
        )}
      </div>
    </div>
  );
}

export default App;
