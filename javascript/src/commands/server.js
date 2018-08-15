function send(message) {
  const fs = require('fs');

    const pipe = (...fns) => val => fns.reduce((acc, fn) => fn(acc), val)
    
    const dispatch = action => state => reducer(state, action)

function reducer(state, action) {
  switch(action.type) {
    case 'UPDATE_TIME': {
      return {
        ...state,
        time: new Date(),
      }
    }
    case 'ADD_CHANNEL': {
        return {
          ...state,
          data: [
            ...state.data,
            action.payload.id
          ],
        }
      }
    case 'ADD_SERVER': {
      return {
        ...state,
        servers: {
          ...state.servers,
          [action.payload.server]: action.payload.channel,
        }
      }
    }
    default: return state
  }
}

const addChannel = (id) => ({
  type: 'ADD_CHANNEL',
  payload: {
    id,
  }
})

const updateTime = () => ({
  type: 'UPDATE_TIME',
});

const addServer = (msg) => ({
  type: 'ADD_SERVER',
  payload: {
    channel: msg.channel.id,
    server: msg.guild.id,
  }
})

const transformation = pipe(
  dispatch(addServer(message)),
)

const updateJsonData = (file, pred) => {
  const jsonData = JSON.parse(fs.readFileSync(file, 'utf8'))
  fs.writeFileSync(file, JSON.stringify(pred(jsonData), null, 2));
}

// wołaj to kiedy Ci się tam podoba 
updateJsonData('./src/servers.json', transformation)
}

module.exports = send