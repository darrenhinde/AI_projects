import React, { Component } from 'react';
import { Link } from 'react-router-dom';

export default class Navbar extends Component {
    render() {
        return (
            <nav className="navbar navbar-dark bg-dark navbar-expand-lg">
                <Link to="/home" className="navbar-brand">CryptoVibes</Link>
                <div className="collpase navbar-collapse">
                <ul className="navbar-nav mr-auto">

                    <li className="navbar-item">
                    <Link to="/" className="nav-link">Dashboard</Link>
                    </li>

                    <li className="navbar-item">
                    <Link to="/summary" className="nav-link">Summarizer</Link>
                    </li>

                    <li className="navbar-item">
                    <Link to="/trending" className="nav-link">Trending</Link>
                    </li>

                </ul>
                </div>
            </nav>
        );
    }
}