#!/usr/bin/node
import kue from 'kue';

const jobObject = {
  phoneNumber: '4153518780',
  message: 'This is the code to verify your account',
};

const queue = kue.createQueue();

const jobType = 'push_notification_code';
const job = queue.create(jobType, jobObject).save((error) => {
  if (!error) console.log(`Notification job created: ${job.id}`);
  else console.log('Notification job failed');
});

job.on('complete', () => {
  console.log('Notification job completed');
});
