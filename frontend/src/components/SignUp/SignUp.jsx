import React from 'react';
import axios from 'axios';


class SignUp extends React.Component {

  constructor(props) {
    super(props);

    this.state = {
      'email': '',
      'passwordFirst': '',
      'passwordSecond': '',
      'message': ''
    };

    this.onChange = this.onChange.bind(this);
    this.onSubmit = this.onSubmit.bind(this);
  }

  onChange(property, event) {
    const value = event.target.value;

    const state = {};

    state[property] = value;

    this.setState(state);
  }

  onSubmit(event) {
    event.preventDefault();

    const { email, passwordFirst, passwordSecond } = this.state;

    console.log({ email, passwordFirst, passwordSecond });

    let message = '';

    if (passwordFirst !== passwordSecond) {
      message = 'Passwords do not match.';
    }

    this.setState({message});
  
    let url = `/api/users/new`;

    const password = passwordFirst;
    const user = {email, password}

    axios.post(url, user)
    .then(res => {
      console.log(res);
      console.log(res.data);
    })

    
  }

  render() {
    const { email, passwordFirst, passwordSecond, message } = this.state;

    return (
      <div>
        <h2>SignUp</h2>
        <form>
          <div className="form-group">
            <label htmlFor="email">Email</label>
            <input
              type="email"
              className="form-control"
              placeholder="Email"
              id="email"
              value={ email }
              onChange={ (event) => this.onChange('email', event) }
            />
            <h5 className='text-danger'>{ message }</h5>
            <label htmlFor="passwordFirst">Password</label>
            <input
              type="password"
              className="form-control"
              id="passwordFirst"
              placeholder="Password"
              value={ passwordFirst }
              onChange={ (event) => this.onChange('passwordFirst', event) }
            />
            <label htmlFor="passwordSecond">Confirm Password</label>
            <input
              type="password"
              className="form-control"
              id="passwordSecond"
              placeholder="Password"
              value={ passwordSecond }
              onChange={ (event) => this.onChange('passwordSecond', event) }
            />
          </div>
          <button
            type="submit"
            className="btn btn-primary"
            onClick={ this.onSubmit }
          >
            SignUp
          </button>
        </form>
      </div>
    );
  }

}

export default SignUp;
