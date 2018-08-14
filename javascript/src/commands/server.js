const fs = require('fs')

// imports
let test = fs.readFileSync('./servers.json')
test.time = new Date()

fs.writeFile ("server.json", JSON.stringify(test), function(err) {
    if (err) throw err
    console.log('Change json')
})
