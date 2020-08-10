import React from 'react';

import Clipboard from '../Clipboard';


class ListJobItem extends React.Component {

  constructor(props) {
    super(props);
  }

  render() {
    const { job } = this.props;

    const { uuid, company, url, role, type } = job;

    return (
      <tr>
        <td>
          <a
            href={ company.url }
          >
            { company.name }
          </a>
        </td>
        <td>
          <a
            href={ url }
          >
            { role }
          </a>
          <Clipboard
            value={ url }
          />
        </td>
        <td>
          { type }
        </td>
      </tr>
    );
  }

}

export default ListJobItem;
