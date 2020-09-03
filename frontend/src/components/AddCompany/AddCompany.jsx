import React from 'react';
import axios from 'axios';


class AddCompany extends React.Component {

  constructor(props) {
    super(props);

    this.state = {
      data: {
        company: ""
      }
    };

    this.companyOnChange = this.companyOnChange.bind(this);
    this.submitOnClick = this.submitOnClick.bind(this);
  }

  companyOnChange(event) {
    const company = event.target.value;

    this.setState({
      data: {
        company: company
      }
    });
  }

  submitOnClick(event) {
    event.preventDefault();

    const { data } = this.state;

    let url = `/api/companies/new`;

    axios.post(url, data)
    .then(res => {
      console.log(res);
      console.log(res.data);
      this.props.fetchCompanies();
    })

    
  }


  render() {
    return (
      <div>
        <h2>AddCompany</h2>
        <form>
          <div className="form-group">
            <label htmlFor="company">Company</label>
            <input
              type="text"
              className="form-control"
              id="company"
              placeholder="Company"
              value={ this.company }
              onChange={ this.companyOnChange }/>
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

export default AddCompany;
