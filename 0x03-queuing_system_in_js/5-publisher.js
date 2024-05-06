import redis from 'redis';

// Attempt to connect
const client = redis.createClient();

// Log whether it's a success or failure
client
  .on('error', (err) => console.log('Redis client not connected to the server:', err.message))
  .on('connect', () => console.log('Redis client connected to the server'));

function publishMessage(message, delay) {
  console.log('About to send', message);

  // Send message after some delay
  setTimeout((() => client.publish('holberton school channel', message)), delay);
}

// Publish messages
publishMessage("Holberton Student #1 starts course", 100);
publishMessage("Holberton Student #2 starts course", 200);
publishMessage("KILL_SERVER", 300);
publishMessage("Holberton Student #3 starts course", 400);
