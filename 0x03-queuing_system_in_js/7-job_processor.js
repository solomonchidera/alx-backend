#!/usr/bin/node
import kue from 'kue';

const blackList = ['4153518780', '4153518781'];
const queue = kue.createQueue();

function sendNotification(phoneNumber, message, job, done) {
  if (blackList.includes(phoneNumber)) {
    console.log(`Phone number ${phoneNumber} is blacklisted`);
    done(new Error(`Phone number ${phoneNumber} is blacklisted`));
  } else {
    job.progress(50, 100);
    console.log(
      `Sending notification to ${phoneNumber}, with message: ${message}`
    );
    done();
  }
}

queue.process('push_notification_code_2', 2, (job, done) => {
  const { phoneNumber, message } = job.data;
  sendNotification(phoneNumber, message, job, done);
});

queue.on('job enqueue', (id, type) => {
  console.log(`Processing job ${id} (${type})`);
});
