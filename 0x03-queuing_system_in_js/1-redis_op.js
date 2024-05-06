import redis from 'redis';

// Attempt to connect
const client = redis.createClient();

// Log whether it's a success or failure
client
  .on('error', (err) => console.log('Redis client not connected to the server:', err.message))
  .on('connect', () => console.log('Redis client connected to the server'));

function displaySchoolValue(schoolName) {
  // Get and display school's value
  client.get(schoolName, (error, value) => {
    if (error) throw error;
    console.log(value);
  });
}

function setNewSchool(schoolName, value) {
  // Update school's value
  client.set(schoolName, value, redis.print);
}

// Call functions
displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
