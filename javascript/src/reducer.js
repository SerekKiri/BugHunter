const { serverReducer } = require('./commands/server')
const { combineReducers } = require('redux');

const reducer = combineReducers({
  servers: serverReducer,
  lastUpdated: (state = {}) => state,
})

module.exports = reducer