import React from 'react';
import axios from 'axios';

import AddCompany from '../AddCompany';
import AddJobForm from '../AddJobForm';
import ListCompanies from '../ListCompanies';
import ListJobs from '../ListJobs';
import ListUserJobs from '../ListUserJobs';
import LogIn from '../LogIn';
import Logout from '../Logout';
import SignUp from '../SignUp';

import UserJobsContext from '../../contexts/UserJobsContext';


axios.defaults.withCredentials = true


class Main extends React.Component {

  constructor(props) {
    super(props);

    this.state = {
      user: null,
      companies: [],
      jobs: [],
      userJobs: [],
    }

    this.fetchCompanies = this.fetchCompanies.bind(this);
    this.fetchJobs = this.fetchJobs.bind(this);
    this.fetchUserJobs = this.fetchUserJobs.bind(this);
    this.setUser = this.setUser.bind(this);
  }

  componentDidMount() {

    this.fetchCompanies();
    this.fetchUser();
    this.fetchJobs();
    this.fetchUserJobs();
  }

  fetchUser() {
    console.log(window.location);
    let url = '/api/users/current';
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
    const url = '/api/companies/';

    axios.get(url)
    .then(res => {
      // console.log(res.data);
      const companies = res.data;
      this.setState({
        companies
      });
    });

  }

  fetchJobs() {
    console.log('Fetching jobs');
    let url = `/api/jobs/`;

    axios.get(url)
    .then(res => {
      // console.log(res.data);
      const jobs = res.data;
      this.setState({
        jobs
      });
    });
  }

  fetchUserJobs() {
    console.log('Fetching user jobs');
    const url = '/api/users/jobs/';

    axios.get(url)
    .then(res => {
      const userJobs = res.data;
      console.log(userJobs);

      if (!userJobs.status){
        this.setState({
          userJobs
        });
      }
      
    });
  }

  render() {
    const { user, companies, jobs, userJobs } = this.state;

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
      <UserJobsContext.Provider value={{fetchUserJobs: this.fetchUserJobs}}>
        <div className="container">
          <h1>Applications</h1>
          <AddCompany
            fetchCompanies={this.fetchCompanies}
          />
          <AddJobForm
            companies={ companies }
          />
          {sessionComponents}
          <ListCompanies
            companies={ companies }
            fetchCompanies={this.fetchCompanies}
          />
          <ListJobs
            jobs={ jobs }
            fetchJobs={ this.fetchJobs }
          />
          <ListUserJobs
            userJobs={ userJobs }
          />
        </div>
      </UserJobsContext.Provider>
    );
  }

}

export default Main;
