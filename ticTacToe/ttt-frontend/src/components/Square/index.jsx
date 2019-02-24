import React from 'react';
import PropTypes from 'prop-types';
import styled from 'styled-components';

const Square = (props) => {
  
  const {
    marker,
    makeMoveWithId
  } = props;
  
  const displayMarker = marker === "E" ? " " : marker;
  
  return (
    <SquareContent onClick={makeMoveWithId}>
      {displayMarker}
    </SquareContent>
    
  )
}


const SquareContent = styled.div`
  border: 5px solid #333333;
  border-radius: 0.3em;
  min-width: 6rem;
  min-height: 6rem;
  cursor: pointer;
  font-size: 5rem;
  display: flex;
  justify-content: center;
  align-content: center;
  color: ${props => props.winner ? "red" : "black"};
`


Square.propTypes = {
  marker: PropTypes.string,
  makeMoveWithId: PropTypes.func,
  winner: PropTypes.bool
}
export default Square;
