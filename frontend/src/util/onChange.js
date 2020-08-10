function onChange(event, property) {
  const value = event.target.value;

  const state = {};

  state[property] = value;

  this.setState(state);
};

export default onChange;
