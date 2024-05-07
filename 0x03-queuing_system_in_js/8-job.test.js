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
    queue.testMode.enter();
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

    expect(spyCLog.calledOnceWith(sinon.match('Notification job created: 1'))).to.be.true;
    expect(queue.testMode.jobs.length).to.equal(1);
    expect(queue.testMode.jobs[0].type).to.equal('push_notification_code_3');
    expect(queue.testMode.jobs[0].data).to.eql({ phoneNumber: '45789735', message: 'Hello!' });
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

    expect(spyCLog.calledWith(sinon.match('Notification job created: 2'))).to.be.true;
    expect(spyCLog.calledWith(sinon.match('Notification job created: 3'))).to.be.true;
    expect(queue.testMode.jobs.length).to.equal(2);
    expect(queue.testMode.jobs[0].type).to.equal('push_notification_code_3');
    expect(queue.testMode.jobs[0].data).to.eql({ phoneNumber: '45789735', message: 'Hello!' });
    expect(queue.testMode.jobs[1].type).to.equal('push_notification_code_3');
    expect(queue.testMode.jobs[1].data).to.eql({ phoneNumber: '74569170', message: 'Bye!' });
  });
});
