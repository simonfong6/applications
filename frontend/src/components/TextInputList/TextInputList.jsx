import React from 'react';
import _ from 'lodash';


class TextInputList extends React.Component {

  constructor(props) {
    super(props);

    const id = _.uniqueId();
    const listId = _.uniqueId();

    this.state = {
      defaultId: id,
      listId,
    };
  }

  render() {
    const { defaultId, listId } = this.state;
    const { label, id, value, onChange, type="text", options=[] } = this.props;

    return (
      <div>
        <label
          htmlFor={ id }
        > 
          { label }
        </label>
        <input
          className="form-control"
          type={ type }
          id={ id }
          list={ listId }
          placeholder={ label }
          value={ value }
          onChange={ onChange }
        />
        <datalist
          id={ listId }
        >
          {
            options.map(value => (
              <option
                key={ value }
                value={ value }
              />
            ))
          }
        </datalist>
      </div>
    );
  }

}

export default TextInputList;
