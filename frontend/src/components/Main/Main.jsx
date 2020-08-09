import React from 'react';
import axios from 'axios';

import AddCompany from '../AddCompany';
import ListCompanies from '../ListCompanies';
import LogIn from '../LogIn';
import Logout from '../Logout';
import SignUp from '../SignUp';


axios.defaults.withCredentials = true


class Main extends React.Component {

  constructor(props) {
    super(props);

    this.state = {
      data: {
        data: -1
      },
      companies: [],
      user: null
    }

    this.fetchCompanies = this.fetchCompanies.bind(this);
    this.setUser = this.setUser.bind(this);
  }

  componentDidMount() {
    fetch('/api/data')
    .then(resp => resp.json())
    .then(data => this.setState({data: data}));

    this.fetchCompanies();
    this.fetchUser();
  }

  fetchUser() {
    const url = '/api/users/current';
    axios.get(url)
    .then(resp => {
      const data = resp.data;
      console.log(data);

      // Has email means user object.
      if (data.email) {
        this.setUser(data);
      }
    });
  }

  setUser(user) {
    console.log(user);
    this.setState({
      user
    });
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
    const { data, user } = this.state;

    let sessionComponents = null;

    if (!user) {
      sessionComponents = (
        <div>
          <SignUp />
          <LogIn
            setUser={this.setUser}
          />
        </div>
      );
    } else {
      sessionComponents = <Logout setUser={this.setUser} />;
    }

    return (
      <div className="container">
        <h1>Applications</h1>
        {data.data}
        <AddCompany
          fetchCompanies={this.fetchCompanies}
        />
        {sessionComponents}
        <ListCompanies
          companies={this.state.companies}
          fetchCompanies={this.fetchCompanies}
        />
      </div>
    );
  }

}

export default Main;
