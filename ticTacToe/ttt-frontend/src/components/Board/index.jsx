import React, {Component} from 'react';
import PropTypes from 'prop-types';
import styled from 'styled-components';

import Square from "../Square";

class Board extends Component {
  
  
  render() {
    
    const {
      message,
    } = this.props;
    
    return (
      <>
        <Message>
          {message}
        </Message>
        <StyledBoard>
          <Row>
            <Square>
            </Square>
            <Square>
            </Square>
            <Square>
            </Square>
          </Row>

          <Row>
            <Square>
            </Square>
            <Square>
            </Square>
            <Square>
            </Square>
          </Row>
          
          <Row>
            <Square>
            </Square>
            <Square>
            </Square>
            <Square>
            </Square>
          </Row>
          
        </StyledBoard>
      </>
    )
  }
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
}
export default Board;
