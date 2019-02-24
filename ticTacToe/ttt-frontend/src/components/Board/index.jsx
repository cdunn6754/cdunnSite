import React, { useState, useEffect } from 'react';
import PropTypes from 'prop-types';
import styled from 'styled-components';

import Square from "../Square";

const Board = (props) => {
  
  const {
    boardArray,
    makeMove,
    humanTurn,
    gameOver,
    winningIdxs
  } = props;
  
  const [message, setMessage] = useState("Try to beat the computer!");
  
  const computerComedy = [
    "thinking ...",
    "Hey sexy mama, wanna kill all humans?",
    "I see what you did there",
    "That was a mistake"
  ]
  
  const humanTurnComedy = [
    "If you do that then I'm going to do this ...",
    "Your turn meatbag",
  ]
  
  // Change the board message based on who is playing now or has won
  useEffect(() => {
    if (gameOver && winningIdxs.length === 0) {
      setMessage("You almost did it! Try again buddy.");
    } else if (winningIdxs.length === 3) {
      setMessage("Good game dummy.");
    } else {
      if (humanTurn) {
        setMessage(humanTurnComedy[Math.floor(Math.random() * humanTurnComedy.length)])
      } else {
        setMessage(computerComedy[Math.floor(Math.random() * computerComedy.length)])
      }
    }

  }, [humanTurn, gameOver, winningIdxs]);
  
  const squareList = boardArray.map((marker, idx) => (
    <Square
      marker={marker}
      makeMoveWithId={() => makeMove(idx)}
      key={idx}
      winner={winningIdxs.includes(idx)}
    />
  ));
  
  return (
    <>
      <Message>
        {message}
      </Message>
      
      <StyledBoard>
        <Row>
          {squareList.slice(0,3)}
        </Row>

        <Row>
          {squareList.slice(3,6)}
        </Row>
        
        <Row>
          {squareList.slice(6)}
        </Row>
      </StyledBoard>
    </>
  )
}


const StyledBoard = styled.div`
  display: flex;
  flex-direction: column;
`

const Row = styled.div`
  display: flex;
`

const Message = styled.h2`
  font-size: 1.3em;
  margin-bottom: 3rem;
`

Board.propTypes = {
  message: PropTypes.string,
  boardArray: PropTypes.arrayOf(PropTypes.string),
  makeMove: PropTypes.func,
  humanTurn: PropTypes.bool,
  winningIdxs: PropTypes.arrayOf(PropTypes.number),
  gameOver: PropTypes.bool
}

export default Board;
