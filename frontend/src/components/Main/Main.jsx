import React from 'react';

import AddJobForm from '../AddJobForm';

class Main extends React.Component {

  constructor(props) {
    super(props);

    this.state = {
      data: {
        data: -1
      }
    }
  }

  componentDidMount() {
    fetch('/api/data')
    .then(resp => resp.json())
    .then(data => this.setState({data: data}));

  }

  render() {
    const { data } = this.state;
    return (
      <div className="container">
        <h1>Applications</h1>
        {data.data}
        <AddJobForm />
      </div>
    );
  }

}

export default Main;
