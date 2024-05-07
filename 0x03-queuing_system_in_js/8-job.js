import kue from 'kue';

// Create push_notification_code_3 jobs
export default function createPushNotificationsJobs(jobs, queue) {
  
  // Check that `jobs` is an array
  if (!Array.isArray(jobs)) {
    throw new Error('Jobs is not an array');
  }

  jobs.forEach((data) => {

    // Create a job on the queue
    const job = queue.create('push_notification_code_3', data)
    job.save((err) => {
      if (!err) {
        console.log(`Notification job created: ${job.id}`);
      }
    });

    // Handle job events
    job.on('progress', (progress) => console.log(`Notification job ${job.id} ${progress}% complete`))
      .on('failure', (error) => console.log(`Notification job ${job.id} failed: ${error.message}`))
      .on('complete', () => console.log(`Notification job ${job.id} completed`));
  });
}
