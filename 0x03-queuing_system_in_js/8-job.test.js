#!/usr/bin/node
import kue from 'kue';
import sinon from 'sinon';
import { expect } from 'chai';
import createPushNotificationsJobs from './8-job';

const queue = kue.createQueue();

/* eslint-disable */
describe('createPushNotificationsJobs', () => {
  let sinonList = [];
  before(() => queue.testMode.enter());
  afterEach(() => {
    queue.testMode.clear();
    sinonList.forEach((spies) => {
      spies.restore();
    });
    sinonList = [];
  });
  after(() => {
    queue.testMode.exit();
  });

  it('Testing a non array...', () => {
    const job = {
      phoneNumber: '569877867',
      message: 'The verification code is 9667',
    };
    expect(() => createPushNotificationsJobs(job, queue)).to.throw(
      Error,
      'Jobs is not an array'
    );
  });

  it('Testing creates job log', () => {
    const consoleLog = sinon.spy(console, 'log');
    sinonList.push(consoleLog);
    const job = [
      {
        phoneNumber: '569865867',
        message: 'The verification code is 9627',
      },
    ];
    createPushNotificationsJobs(job, queue);
    expect(consoleLog.args[0][0]).to.includes('Notification job created:');
  });

  it('Testing the type of jobs', () => {
    const createSpy = sinon.spy(queue, 'create');
    sinonList.push(createSpy);
    const jobs = [
      {
        phoneNumber: '569865867',
        message: 'The verification code is 9657',
      },
      {
        phoneNumber: '569865867',
        message: 'The verification code is 9627',
      },
    ];
    createPushNotificationsJobs(jobs, queue);
    jobs.forEach((job) => {
      expect(createSpy.calledWith('push_notification_code_3', job)).to.be.true;
    });
  });
});
