import kue from 'kue';
import chai from 'chai';
const expect = chai.expect;
import sinon from 'sinon';

import createPushNotificationsJobs from './8-job';
import sendNotification from './7-job_processor';

const queue = kue.createQueue();
describe('Test createPushNotificationsJobs function', () => {

  let spyCLog;

  before(() => {
    queue.testMode.enter(true);
  });

  beforeEach(() => {

    // Put a spy on console.log
    spyCLog = sinon.spy(console, 'log');
  });

  afterEach(() => {
    queue.testMode.clear();

    // Restore `console.log`'s spy
    spyCLog.restore()
  });

  after(() => {
    queue.testMode.exit();
  });

  it('throws an Error if jobs is not an array', () => {
    expect((() => createPushNotificationsJobs('unemployed', queue)))
      .to.throw(Error, 'Jobs is not an array');
  });

  it('creates one job and log the info to the console', () => {

    const jobs = [{
      phoneNumber: '45789735',
      message: 'Hello!'
    }];

    // Call function
    createPushNotificationsJobs(jobs, queue);

    expect(queue.testMode.jobs.length).to.equal(1);
    expect(queue.testMode.jobs[0].type).to.equal('push_notification_code_3');
  });

  it('creates two jobs and log the infos to the console', () => {

    const jobs = [
    {
      phoneNumber: '45789735',
      message: 'Hello!'
    },
    {
      phoneNumber: '74569170',
      message: 'Bye!'
    }];

    // Call function
    createPushNotificationsJobs(jobs, queue);

    expect(queue.testMode.jobs.length).to.equal(2);
  });

  it('Test processing successfully', function(done) {

    const jobs = [
    {
      phoneNumber: '45789735',
      message: 'Hello!'
    },
    {
      phoneNumber: '74569170',
      message: 'Bye!'
    }];

    // Create jobs
    createPushNotificationsJobs(jobs, queue);

    // Process jobs
    queue.process('push_notification_code_3', function(job, done) {
      sendNotification(job.data.phoneNumber, job.data.message, job, done);
    });

    queue.on('job complete', function(id) {
      kue.Job.get(id, function(err, job) {
        expect(spyCLog.calledWith(`Sending notification to ${job.data.phoneNumber}, with message: ${job.data.message}`)).to.be.true;
        done();
      });
    });
  });
});
