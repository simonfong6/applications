import React from 'react';
import { MdContentCopy } from 'react-icons/md';
import { FcCheckmark } from 'react-icons/fc';

import './Clipboard.css';


const CLIPBOARD_TIMEOUT_MILLISECONDS = 1000;


class Clipboard extends React.Component {

  constructor(props) {
    super(props);

    this.state = {
      copied: false
    }
  }

  copyToClipboard(text) {
    const { timeout=CLIPBOARD_TIMEOUT_MILLISECONDS } = this.props;

    if (!document.hasFocus()) {
      return;
    }
    navigator.clipboard.writeText(text);

    this.setState({
      copied: true
    });

    setTimeout(() => {
      this.setState({
        copied: false
      });
    }, timeout);
  }

  render() {
    const { value } = this.props;
    const { copied }  = this.state;

    let icon;

    if (copied) {
      icon = (
        <span className='ml-1'>
          <FcCheckmark />
        </span>
      );
    } else {
      icon = (
        <span className='pointer ml-1'>
          <MdContentCopy onClick={() => this.copyToClipboard(value)}/>
        </span>
      );
    }
  
    return icon;
  }

}

export default Clipboard;
