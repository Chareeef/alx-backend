import redis from 'redis';

// Attempt to connect
const client = redis.createClient();

// Log whether it's a success or failure
client
  .on('error', (err) => console.log('Redis client not connected to the server:', err.message))
  .on('connect', () => console.log('Redis client connected to the server'));

// Subscribe to 'holberton school channel'
const channel_name = 'holberton school channel';
client.subscribe(channel_name);

// Handle incoming messages
client.on('message', (channel, message) => {

  // If 'KILL_SERVER' message, unsubscríbe and quit
  if (message === 'KILL_SERVER') {
    client.unsubscribe(channel_name);
    client.quit();
  } else { // Log message
    console.log(message);
  }
});
