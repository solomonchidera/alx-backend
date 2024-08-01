#!/usr/bin/node

export default function createPushNotificationsJobs(jobs, queue) {
  if (!(jobs instanceof Array)) throw Error('Jobs is not an array');
  jobs.forEach((element) => {
    if (element) {
      const job = queue.create('push_notification_code_3', element);
      job.save((error) => {
        if (!error) console.log(`Notification job created: ${job.id}`);
        else console.log(`Notification job ${job.id} failed: ${error.message}`);
      });
      job.on('progress', (progress) => {
        console.log(`Notification job ${job.id} ${progress}% complete`);
      });
      job.on('complete', () => {
        console.log(`Notification job ${job.id} completed`);
      });
    }
  });
}
