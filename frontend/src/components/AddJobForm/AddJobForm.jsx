import React from 'react';
import axios from 'axios';
import _ from 'lodash';


import TextInput from '../TextInput';
import TextInputList from '../TextInputList';
import onChange from '../../util/onChange';


class AddJobForm extends React.Component {

  constructor(props) {
    super(props);

    this.state = {
      company: '',
      url: '',
      role: '',
      type: '',
    };

    this.onChange = onChange.bind(this);
    this.submitOnClick = this.submitOnClick.bind(this);
  }

  submitOnClick(event) {
    event.preventDefault();

    const { company, url, role, type } = this.state;

    const data = { company, url, role, type };

    console.log(data);

    let endpoint = `/api/jobs/new`;

    axios.post(endpoint, data)
    .then(res => {
      console.log(res);
      console.log(res.data);
      // this.props.fetchCompanies();
    })

    
  }

  companiesList() {
    const { companies:companyObjects } = this.props;

    let companies = companyObjects.map(companyObject => {
      return companyObject.name;
    });

    return companies;
  }

  render() {

    const { company, url, role, type } = this.state;

    const companies = this.companiesList();

    const roles = [
      'Software Engineer',
      'Software Engineer - Backend',
      'Software Engineer - Frontend',
      'Software Engineer - Fullstack',
      'Software Engineer - Infrastructure',
    ];

    const types = ['Intern', 'Fulltime'];

    return (
      <div>
        <h2>AddJobForm</h2>
        <form>
          <div className="form-group">
            <TextInputList
              label="Company"
              value={ company }
              onChange={ (event) => this.onChange(event, 'company') }
              options={ companies }
            />
            <TextInput
              label="URL"
              value={ url }
              onChange={ (event) => this.onChange(event, 'url') }
            />
            <TextInputList
              label="Role"
              value={ role }
              onChange={ (event) => this.onChange(event, 'role') }
              options={ roles }
            />
            <TextInputList
              label="Type"
              value={ type }
              onChange={ (event) => this.onChange(event, 'type') }
              options={ types }
            />
          </div>
          <button
            type="submit"
            className="btn btn-primary"
            onClick={ this.submitOnClick }
          >
            Submit
          </button>
        </form>
      </div>
    );
  }

}

export default AddJobForm;
