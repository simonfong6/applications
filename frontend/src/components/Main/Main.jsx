import React from 'react';

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
      <div>
        <h1>Main</h1>
        {data.data}
      </div>
    );
  }

}

export default Main;
