import React, { Component } from 'react';
import './App.css';

import Board from './components/Board';

class App extends Component {
  render() {
    const message = "Try to beat the computer!"

    return (
      <div className="App">
        <Board {...{message}}></Board>
      </div>
    );
  }
}

export default App;
