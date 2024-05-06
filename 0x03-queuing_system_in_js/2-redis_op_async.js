import redis from 'redis';
import { promisify } from 'util';

// Attempt to connect
const client = redis.createClient();

// Log whether it's a success or failure
client
  .on('error', (err) => console.log('Redis client not connected to the server:', err.message))
  .on('connect', () => console.log('Redis client connected to the server'));

// promisify client.get
const getAsync = promisify(client.get).bind(client);

async function displaySchoolValue(schoolName) {
  // Get and display school's value with promise style

  try {
    const value = await getAsync(schoolName);
    console.log(value);
  } catch (error) {
    console.log(error.message);
  }
}

function setNewSchool(schoolName, value) {
  // Update school's value
  client.set(schoolName, value, redis.print);
}

// Call functions
(async () => {
  await displaySchoolValue('Holberton');
  setNewSchool('HolbertonSanFrancisco', '100');
  await displaySchoolValue('HolbertonSanFrancisco');
})();
