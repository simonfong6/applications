import React from 'react';


const UserJobsContext = React.createContext({
  fetchUserJobs: () => {},
});

export default UserJobsContext;
