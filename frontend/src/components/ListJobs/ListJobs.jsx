import React from 'react';

import ListJobItem from '../ListJobItem';

import UserJobsContext from '../../contexts/UserJobsContext';


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
                <UserJobsContext.Consumer
                  key={job.uuid}
                >
                  {({ fetchUserJobs }) => (
                    <ListJobItem
                      key={job.uuid}
                      job={ job }
                      fetchJobs={ this.props.fetchJobs }
                      fetchUserJobs={ fetchUserJobs }
                    />
                  )}
                </UserJobsContext.Consumer>
              ))
          }
          </tbody>
        </table>
      </div>
    );
  }

}

export default ListJobs;
