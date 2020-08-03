import React from 'react';
import axios from 'axios';
import { MdContentCopy } from 'react-icons/md';
import { MdDelete } from 'react-icons/md';
import { FcCheckmark } from 'react-icons/fc';


import './Company.css';


class Company extends React.Component {

  constructor(props) {
    super(props);

    this.state = {
      copySucess: false
    }
  }

  copyToClipboard(text) {
    if (!document.hasFocus()) {
      return;
    }
    navigator.clipboard.writeText(text);

    this.setState({
      copySucess: true
    });

    setTimeout(() => {
      this.setState({
        copySucess: false
      });
    }, 1000);
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

    const {copySucess}  = this.state;

    let icon;

    if (copySucess) {
      icon = <span className='ml-1'><FcCheckmark /></span>;
    } else {
      icon = (<span className='pointer ml-1'>
       <MdContentCopy onClick={() => this.copyToClipboard(auto_link)}/>
      </span>);
    }

    let deleteIcon = <span className='pointer ml-1'><MdDelete onClick={() => this.delete(name)}/></span>
    

    career_link = career_link || 'None';
    auto_link = auto_link || 'None';
    return (
        <tr>
          <td>{name}{deleteIcon}</td>
          <td><a href={career_link}>{career_link}</a></td>
          <td><a href={auto_link} id='copy'>{auto_link}</a>{icon}</td>
        </tr>
    );
  }

}

export default Company;
