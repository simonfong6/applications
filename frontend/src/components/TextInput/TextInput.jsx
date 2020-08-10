import React from 'react';
import _ from 'lodash';


class TextInput extends React.Component {

  constructor(props) {
    super(props);

    const id = _.uniqueId();

    this.state = {
      defaultId: id
    };
  }

  render() {
    const { defaultId } = this.state;
    const { label, id=defaultId, value, onChange, type="text" } = this.props;

    return (
      <div>
        <label
          htmlFor={ id }
        > 
          { label }
        </label>
        <input
          type={ type }
          className="form-control"
          id={ id }
          placeholder={ label }
          value={ value }
          onChange={ onChange }
        />
      </div>
    );
  }

}

export default TextInput;
