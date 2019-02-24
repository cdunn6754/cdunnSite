import React, { useState } from 'react';

import Board from "../components/Board";

const BoardContainer = () => {
  
  const [boardArray, setBoardArray] = useState(Array(9).fill('E'));
  const [humanTurn, setHumanTurn] = useState(true);
  const [winningIdxs, setWinningIdxs] = useState([]);
  const [gameOver, setGameOver] = useState(false);
  
  const humanMarker = 'X';
  
  const makeMove = (squareId) => {
    // Only make a move if they square is empty
    if (boardArray[squareId] === "E") {
      let newBoard = boardArray.slice();
      newBoard.splice(squareId, 1, humanMarker);
      setBoardArray(newBoard);
      setHumanTurn(!humanTurn);
      setWinningIdxs(checkForWinner());
      checkForGameOver()
    }
  };
  
  const checkForGameOver = () => {
    if (!boardArray.includes('E')) {
      setGameOver(true);
    }
  }
  
  const checkForWinner = () => {
    for (let i = 0; i < 3; i++) {
      if (
          boardArray[3*i] === boardArray[3*i + 1] &&
          boardArray[3*i + 1] === boardArray[3*i + 2] &&
          boardArray[3*i+2] !== 'E'
      ) {
          // Return row idxs
          return [3*i, 3*i+1, 3*i+2];
      } else if (
          boardArray[i] === boardArray[3 + i] &&
          boardArray[3 + i] === boardArray[6 + i] &&
          boardArray[6 + i] !== 'E'
      ) {
        // Return column idxs
        return [i, 3+i, 6+i];
      }
    }
    
    // Diagonals
    if (
      boardArray[0] === boardArray[4] &&
      boardArray[4] === boardArray[8] &&
      boardArray[8] !== 'E'
    ) {
      // Diagonal
      return [0, 4, 8];
    } else if (
      boardArray[2] === boardArray[4] &&
      boardArray[4] === boardArray[6] &&
      boardArray[6] !== 'E'
    ) {
      // Anti diagonal
      return [2, 4, 6]
    }
    
    return []
  }
  
  return <Board
      {...{
        boardArray,
        makeMove,
        humanTurn,
        winningIdxs,
        gameOver,
      }}
    />
}

export default BoardContainer
