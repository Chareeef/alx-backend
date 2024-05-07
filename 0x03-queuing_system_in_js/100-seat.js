import express from 'express';
import kue from 'kue';
import redis from 'redis';
import { promisify } from 'util';

// Create Redis client
const client = redis.createClient();

// Promisify client.get
const getAsync = promisify(client.get).bind(client);

function reserveSeat(number) {
  // Set the key available_seats
  client.set('available_seats', number);
}

async function getCurrentAvailableSeats() {
  // Return the current number of available seats
  return await getAsync('available_seats');
}

// Initialize available_seats to 50 and enable reservation
reserveSeat(50);
let reservationEnabled = true;

// Create jobs queue
const queue = kue.createQueue();
  
// Create Express app
const app = express();

// 'GET /available_seats' route
app.get('/available_seats', async (req, res) => {
  res.json({ 'numberOfAvailableSeats': await getCurrentAvailableSeats() });
});

// 'GET /reserve_seat' route
app.get('/reserve_seat', (req, res) => {

  // Verify if reservation is enabled
  if (!reservationEnabled) {
    return res.json({ "status": "Reservations are blocked" });
  }

  // Create job for reservation
  const job = queue
    .create('reservation')
    .save((error) => {
      if (!error) {
        return res.json({ "status": "Reservation in process" });
      } else {
        return res.json({ "status": "Reservation failed" });
      }
    });

  job.on('complete', () => console.log(`Seat reservation job ${job.id} completed`))
    .on('failure', (error) => console.log(`Seat reservation job ${job.id} failed: ${error.message}`));
});

// 'GET /process' route
app.get('/process', (req, res) => {

  // Process jobs
  queue.process('reservation', async (job, done) => {

    // Get seats number
    const current_seats = await getCurrentAvailableSeats();

    // If there is no more seats, fail the job
    if (current_seats === 0) {
      console.log('Error');
      return done(new Error('Not enough seats available'));
    }

    // Decrease seats by one
    const updated_seats = current_seats - 1;
    reserveSeat(updated_seats);

    // Block reservation if all seats are taken
    if (updated_seats === 0) {
      reservationEnabled = false;
    }

    // Complet job
    return done();
  });

  return res.json({ "status": "Queue processing" });
});

// Start listening
app.listen(1245)
