import React, { Component } from 'react';
import './App.css';

import BoardContainer from './BoardContainer';

class App extends Component {
  render() {
    return (
      <div className="App">
        <BoardContainer/>
      </div>
    );
  }
}

export default App;
