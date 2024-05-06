import kue from 'kue';

// Create queue
const queue = kue.createQueue();

// Create job
const object = {
  phoneNumber: '4153518780',
  message: 'This is the code to verify your account'
};

const job = queue
  .create('push_notification_code', object)
  .save((err) => {
    if (!err) {
      console.log('Notification job created:', job.id);
    }
  });

// Handle job events
job.on('complete', (result) => console.log('Notification job completed'))
  .on('failed', () => console.log('Notification job failed'));
