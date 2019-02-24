import React from 'react';
import PropTypes from 'prop-types';
import styled from 'styled-components';

const Square = (props) => {
  
  const {
    marker,
    makeMove
  } = props;
  
  
  const handleClick = (e) => {
    if (marker) {
      return null
    } else {
      makeMove();
    }
  }
  
  return (
    <SquareContent onClick={() => handleClick}>
      
    </SquareContent>
    
  )
}


const SquareContent = styled.div`
  border: 5px solid black;
  border-radius: 0.3em;
  min-width: 6rem;
  min-height: 6rem;
  cursor: pointer;
`


Square.propTypes = {
  marker: PropTypes.string,
  makeMove: PropTypes.func,
}
export default Square;
