import React from 'react';

import Company from '../Company';

const TABLE_HEADERS = ['Name', 'Link', 'Auto Generated Link'];

class ListCompanies extends React.Component {

  constructor(props) {
    super(props);
  }

  render() {

    const { companies } = this.props;

    return (
      <div>
        <h2>Companies</h2>
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
              companies.map(company => (
                <Company
                  key={company.name}
                  company={ company }
                />
              ))
          }
          </tbody>
        </table>
      </div>
    );
  }

}

export default ListCompanies;
