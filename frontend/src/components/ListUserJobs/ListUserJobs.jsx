import React from 'react';

import ListUserJobItem from '../ListUserJobItem';

import UserJobsContext from '../../contexts/UserJobsContext';


const TABLE_HEADERS = [
  'Company',
  'Role',
  'Type',
  'Status',
];


class ListUserJobs extends React.Component {

  constructor(props) {
    super(props);
  }

  render() {

    const { userJobs } = this.props;

    return (
      <div>
        <h2>ListUserJobs</h2>
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
              userJobs.map(userJob => (
                <UserJobsContext.Consumer
                  key={userJob.uuid}
                >
                  {({ fetchUserJobs }) => (
                    <ListUserJobItem
                      userJob={ userJob }
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

export default ListUserJobs;
