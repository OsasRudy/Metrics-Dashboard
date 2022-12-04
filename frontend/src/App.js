import React, {Component} from 'react'
import './App.css';
import './index.css'
// import Card from 'react-bootstrap/Card';
import {Container, Row, Col, Card} from "react-bootstrap";

import Dashboard from './Dashboard';
function App() {

    return (
        <div className="App">
            <div className="AppGlass">
                <Dashboard/>
            </div>
        </div>
    );
}


export default App;






