import kue from 'kue';

// Create queue
const queue = kue.createQueue();

function sendNotification(phoneNumber, message) {
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
}

// Process jobs
queue.process('push_notification_code', (job) => {
  sendNotification(job.data.phoneNumber, job.data.message);
});
