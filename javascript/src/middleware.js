const fs = require('fs');
const updateData = store => next => action => {
  const result = next(action)
  fs.writeFileSync("./servers.json", JSON.stringify(store.getState(), null, 2));
  return result
}

module.exports = {
  updateData,
}