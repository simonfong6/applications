import React from 'react';

import ListJobItem from '../ListJobItem';


const TABLE_HEADERS = [
  'Company',
  'Role',
  'Type',
];


class ListJobs extends React.Component {

  constructor(props) {
    super(props);
  }

  render() {

    const { jobs } = this.props;

    return (
      <div>
        <h2>ListJobs</h2>
        <table className="table">
          <thead>
            <tr>
              {
                TABLE_HEADERS.map(header => (
                  <th
                    scope="col"
                    key={header}
                  >
                    {header}
                  </th>
                ))
              }
            </tr>
          </thead>
          <tbody>
            {
              jobs.map(job => (
                <ListJobItem
                  key={job.uuid}
                  job={ job }
                  fetchJobs={ this.props.fetchJobs }
                />
              ))
          }
          </tbody>
        </table>
      </div>
    );
  }

}

export default ListJobs;
