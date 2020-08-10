import React from 'react';
import axios from 'axios';
import { MdContentCopy } from 'react-icons/md';
import { MdDelete } from 'react-icons/md';
import { FcCheckmark } from 'react-icons/fc';

import Clipboard from '../Clipboard';


import './Company.css';


class Company extends React.Component {

  constructor(props) {
    super(props);
  }

  delete(name) {
    axios.delete(`/api/companies/${name}`)
    .then(response => {
      console.log(response.data);
      this.props.fetchCompanies();
    });
  }

  render() {
    let { name, career_link, auto_link } = this.props.company;

    let deleteIcon = <span className='pointer ml-1'><MdDelete onClick={() => this.delete(name)}/></span>
    

    career_link = career_link || 'None';
    auto_link = auto_link || 'None';
    return (
        <tr>
          <td>{name}{deleteIcon}</td>
          <td>
            <a
              href={career_link}
            >
              {career_link}
            </a>
          </td>
          <td>
            <a
              href={auto_link}
            >
              {auto_link}
            </a>
            <Clipboard
              value={auto_link}
            />
          </td>
        </tr>
    );
  }

}

export default Company;
