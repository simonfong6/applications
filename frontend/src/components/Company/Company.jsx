import React from 'react';


class Company extends React.Component {

  constructor(props) {
    super(props);
  }

  render() {
    let { name, career_link } = this.props.company;

    career_link = career_link || 'None';
    return (
        <tr>
          <td>{name}</td>
          <td><a href={career_link}>{career_link || 'None'}</a></td>
        </tr>
    );
  }

}

export default Company;
