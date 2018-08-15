

const R = require('ramda');
const { createReducer, createActionTypes } = require('zeal-redux-utils');

const ActionType = createActionTypes("server", [
  "ADD",
]);

const serverReducer = createReducer({}, {
  [ActionType.ADD]: (state, { payload }) => R.assoc(payload.server, payload.channel, state),
})

const addServer = (msg) => ({
  type: ActionType.ADD,
  payload: {
    channel: msg.channel.id,
    server: msg.guild.id,
  }
})

module.exports = {
  serverReducer,
  actions: {
    addServer,
  }
};
