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
      setWinningIdxs(checkForWinner(newBoard));
      checkForGameOver()
    }
  };
  
  const checkForGameOver = () => {
    if (!boardArray.includes('E')) {
      setGameOver(true);
    }
  }

  const checkForWinner = (newBoard) => {
    for (let i = 0; i < 3; i++) {
      if (
          newBoard[3*i] === newBoard[3*i + 1] &&
          newBoard[3*i + 1] === newBoard[3*i + 2] &&
          newBoard[3*i+2] !== 'E'
      ) {
          // Return row idxs
          return [3*i, 3*i+1, 3*i+2];
      } else if (
          newBoard[i] === newBoard[3 + i] &&
          newBoard[3 + i] === newBoard[6 + i] &&
          newBoard[6 + i] !== 'E'
      ) {
        // Return column idxs
        return [i, 3+i, 6+i];
      }
    }
    
    // Diagonals
    if (
      newBoard[0] === newBoard[4] &&
      newBoard[4] === newBoard[8] &&
      newBoard[8] !== 'E'
    ) {
      // Diagonal
      return [0, 4, 8];
    } else if (
      newBoard[2] === newBoard[4] &&
      newBoard[4] === newBoard[6] &&
      newBoard[6] !== 'E'
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
