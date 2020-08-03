import React from 'react';
import axios from 'axios';

import AddJobForm from '../AddJobForm';
import ListCompanies from '../ListCompanies';


class Main extends React.Component {

  constructor(props) {
    super(props);

    this.state = {
      data: {
        data: -1
      },
      companies: []
    }

    this.fetchCompanies = this.fetchCompanies.bind(this);
  }

  componentDidMount() {
    fetch('/api/data')
    .then(resp => resp.json())
    .then(data => this.setState({data: data}));

    this.fetchCompanies();
  }

  fetchCompanies() {
    console.log('Fetching companies');
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
    const { data } = this.state;
    return (
      <div className="container">
        <h1>Applications</h1>
        {data.data}
        <AddJobForm
          fetchCompanies={this.fetchCompanies}
        />
        <ListCompanies
          companies={this.state.companies}
          fetchCompanies={this.fetchCompanies}
        />
      </div>
    );
  }

}

export default Main;
