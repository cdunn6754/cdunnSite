import React, { useState, useEffect } from 'react';

import Board from "../components/Board";
import {API_URL} from "../urls";

const BoardContainer = () => {
  
  const [boardArray, setBoardArray] = useState(Array(9).fill('E'));
  const [humanTurn, setHumanTurn] = useState(true);
  const [winningIdxs, setWinningIdxs] = useState([]);
  const [gameOver, setGameOver] = useState(false);
  const humanMarker = "X";
  
  useEffect(() => {
    // if it's the ais turn
    if (!humanTurn) {
      const agent_marker = humanMarker === "X" ? "O" : "X"
      const data = {
        board_array: boardArray,
        agent_marker
      };
      fetch(
        API_URL, {
          method:"POST",
          mode: "cors",
          headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
          },
          body: JSON.stringify(data),
        }
      )
        .then(response => response.json())
        .then(json => makeMove(json.next_move, agent_marker))
        .then(() => setHumanTurn(!humanTurn))
    }
  }, [humanTurn])
  
  const resetBoard = () => {
    setBoardArray(Array(9).fill('E'));
    setHumanTurn(true);
    setGameOver(false);
    setWinningIdxs([])
  }
    
  const makeMove = (squareId, marker=humanMarker) => {
    // Only make a move if they square is empty
    if (boardArray[squareId] === "E" && !gameOver) {
      let newBoard = boardArray.slice();
      newBoard.splice(squareId, 1, marker);
      setBoardArray(newBoard);
      setHumanTurn(!humanTurn);
      setWinningIdxs(checkForWinner(newBoard));
      checkForGameOver(newBoard)
    }
  };
  
  const checkForGameOver = (newBoard) => {
    if (!newBoard.includes('E') || checkForWinner(newBoard).length > 0) {
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
        resetBoard
      }}
    />
}

export default BoardContainer
