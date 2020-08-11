import React from 'react';
import axios from 'axios';

import Clipboard from '../Clipboard';


class ListUserJobItem extends React.Component {

  constructor(props) {
    super(props);
  }

  update = (uuid, status) => {
    const endpoint = '/api/users/jobs/update'

    const data = {
      uuid,
      status,
    }

    axios.post(endpoint, data)
    .then(res => {
      console.log(res.data);
      this.props.fetchUserJobs();
    });
  }

  render() {

    const { job, status, uuid } = this.props.userJob;

    const { company, url, role, type } = job;

    const statusToActions = new Map();

    statusToActions.set('Not Applied', 'Apply')
    statusToActions.set('Applied', 'None')

    const actionToStatus = new Map();

    actionToStatus.set('Apply', 'Applied')
    actionToStatus.set('None', 'None')

    const action = statusToActions.get(status);
    const newStatus = actionToStatus.get(action);

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
        <td>
          { status }
        </td>
        <td>
          <button
            className='btn btn-primary'
            onClick={ () => this.update(uuid, newStatus) }
          >
            { action }
          </button>
        </td>
      </tr>
    );
  }

}

export default ListUserJobItem;
