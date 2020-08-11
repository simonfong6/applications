import React from 'react';
import axios from 'axios';
import { GoPlus } from "react-icons/go";

import Clipboard from '../Clipboard';


class ListJobItem extends React.Component {

  constructor(props) {
    super(props);
  }

  addJob = (uuid) => {
    console.log(`Adding job: ${uuid}`)

    const data = {
      uuid
    };

    let endpoint = `/api/users/jobs/new`;

    axios.post(endpoint, data)
    .then(res => {
      console.log(res);
      console.log(res.data);

      this.props.fetchUserJobs();
    })
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
        <td>
          <span
            className='pointer'
          >
            <GoPlus
              onClick={ () => this.addJob(uuid) }
            />
          </span>
        </td>
      </tr>
    );
  }

}

export default ListJobItem;
