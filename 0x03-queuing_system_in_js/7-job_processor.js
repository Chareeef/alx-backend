import kue from 'kue';

// Create jobs queue
const jobs = kue.createQueue();

// Blacklisted phone numbers
const blacklistedNums = ['4153518780', '4153518781'];

// Function to process jobs and send notifications
export default function sendNotification(phoneNumber, message, job, done) {

  job.progress(0, 100);

  if (blacklistedNums.includes(phoneNumber)) {
    return done(new Error(`Phone number ${phoneNumber} is blacklisted`));
  }

  job.progress(50, 100);

  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
  return done();
}

jobs.process('push_notification_code_2', 2, (job, done) => {
  sendNotification(job.data.phoneNumber, job.data.message, job, done);
});
