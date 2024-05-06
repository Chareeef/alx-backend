import redis from 'redis';

// Attempt to connect
const client = redis.createClient();

// Log whether it's a success or failure
client
  .on('error', (err) => console.log('Redis client not connected to the server:', err.message))
  .on('connect', () => console.log('Redis client connected to the server'));

// Create `HolbertonSchools` Hash
client.hset('HolbertonSchools', 'Portland', 50, redis.print);
client.hset('HolbertonSchools', 'Seattle', 80, redis.print);
client.hset('HolbertonSchools', 'New York', 20, redis.print);
client.hset('HolbertonSchools', 'Bogota', 20, redis.print);
client.hset('HolbertonSchools', 'Cali', 40, redis.print);
client.hset('HolbertonSchools', 'Paris', 2, redis.print);

// Display `HolbertonSchools` Hash
client.hgetall('HolbertonSchools', (err, hash) => console.log(hash));
