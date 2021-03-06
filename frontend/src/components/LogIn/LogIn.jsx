import React from 'react';
import axios from 'axios';

import onChange from '../../util/onChange';


class LogIn extends React.Component {

  constructor(props) {
    super(props);

    this.state = {
      'email': '',
      'password': '',
      'message': ''
    };

    this.onChange = onChange.bind(this);
    this.onSubmit = this.onSubmit.bind(this);
  }

  onSubmit(event) {
    event.preventDefault();

    const { email, password } = this.state;

    console.log({ email, password });

    let message = '';

    this.setState({message});
  
    let url = `/api/users/login`;

    const user = {email, password}

    axios.post(url, user)
    .then(res => {
      console.log(res);
      console.log(res.data);
      
      url = `/api/users/current`;
      axios.get(url)
      .then(resp => {
        console.log(resp.data);
        const user = resp.data;
        this.props.setUser(user);
      });
    });

    
  }

  render() {
    const { email, password, message } = this.state;

    return (
      <div>
        <h2>LogIn</h2>
        <form>
          <div className="form-group">
            <label htmlFor="emailLogin">Email</label>
            <input
              type="email"
              className="form-control"
              placeholder="Email"
              id="emailLogin"
              value={ email }
              onChange={ (event) => this.onChange(event, 'email') }
            />
            <h5 className='text-danger'>{ message }</h5>
            <label htmlFor="password">Password</label>
            <input
              type="password"
              className="form-control"
              id="password"
              placeholder="Password"
              value={ password }
              onChange={ (event) => this.onChange(event, 'password') }
            />
          </div>
          <button
            type="submit"
            className="btn btn-primary"
            onClick={ this.onSubmit }
          >
            Login
          </button>
        </form>
      </div>
    );
  }

}

export default LogIn;
