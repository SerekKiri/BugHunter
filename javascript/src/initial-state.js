const fs = require('fs');
const jsonData = JSON.parse(fs.readFileSync('./src/servers.json', 'utf8'))

module.exports = {
  jsonData,
}
