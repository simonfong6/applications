import React from 'react';
import axios from 'axios';

const TABLE_HEADERS = ['name', 'link'];

class ListCompanies extends React.Component {

  constructor(props) {
    super(props);

    this.state = {
      companies: []
    };

    
  }

  componentDidMount() {
    this.fetchCompanies();
  }

  fetchCompanies() {
    let url = `/api/companies`;

    axios.get(url)
    .then(res => {
      // console.log(res.data);
      const companies = res.data;
      this.setState({
        companies
      });
    });

  }


  render() {

    const { companies } = this.state;

    console.log('Render');
    console.log(companies);
    return (
      <div>
        <h2>Companies</h2>
        <table class="table">
          <thead>
            {
              TABLE_HEADERS.map(header => (
                <th scope="col">{header}</th>
              ))
            }
          </thead>
          <tbody>
            {
              companies.map(company => (
                <tr key={company.name}>
                  <td>{company.name}</td>
                  <td>{company.career_link || 'None'}</td>
                </tr>
              ))
          }
          </tbody>
        </table>
      </div>
    );
  }

}

export default ListCompanies;
