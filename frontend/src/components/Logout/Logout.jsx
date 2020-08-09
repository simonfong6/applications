import React from 'react';
import axios from 'axios';


class Logout extends React.Component {

  constructor(props) {
    super(props);


  }

  sendRequest = () => {
    console.log('Logout');

    const url = '/api/users/logout';
    axios.get(url)
    .then(resp => {
      console.log(resp.data);
      this.props.setUser(null);
    });
  }

  render() {
    return (
      <div>
        <h2>Logout</h2>
        <button
          className='btn btn-primary'
          onClick={this.sendRequest}
        >
          Logout
        </button>
      </div>
    );
  }

}

export default Logout;
