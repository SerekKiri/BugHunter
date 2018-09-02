const fs = require('fs');
const jsonData = JSON.parse(fs.readFileSync('./servers.json', 'utf8'))

module.exports = {
  jsonData,
}
