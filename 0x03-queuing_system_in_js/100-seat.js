#!/usr/bin/node
import redis from 'redis';
import kue from 'kue';
import express from 'express';
import { promisify } from 'util';

const client = redis.createClient();
const queue = kue.createQueue();
const server = express();

const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);

let reservationEnabled = true;

async function reserveSeat(number) {
  await setAsync('available_seats', number);
}
async function getCurrentAvailableSeats() {
  const availableSeats = await getAsync('available_seats');
  return availableSeats;
}

server.get('/available_seats', async (req, res) => {
  const currentAvailableSeats = await getCurrentAvailableSeats();
  if (!currentAvailableSeats) reservationEnabled = false;
  res.json({ numberOfAvailableSeats: currentAvailableSeats });
});

server.get('/reserve_seat', (req, res) => {
  if (!reservationEnabled) res.json({ status: 'Reservation are blocked' });
  else {
    const job = queue.create('reserve_seat');
    job.save((error) => {
      if (!error) res.json({ status: 'Reservation in process' });
      else res.json({ status: 'Reservation failed' });
    });
    job.on('failed', (error) => {
      console.log(`Seat reservation job ${job.id} failed: ${error}`);
    });
    job.on('complete', () => {
      console.log(`Seat reservation job ${job.id} completed`);
    });
  }
});

server.get('/process', (req, res) => {
  queue.process('reserve_seat', async (job, done) => {
    try {
      const currentAvailableSeats = await getCurrentAvailableSeats();
      if (!currentAvailableSeats || currentAvailableSeats <= 0) {
        reservationEnabled = false;
        done(new Error('Not enough seats available'));
      } else if (currentAvailableSeats > 0) {
        await reserveSeat(currentAvailableSeats - 1);
        if (currentAvailableSeats - 1 === 0) {
          reservationEnabled = false;
        }
        done();
      }
    } catch (error) {
      console.log(error);
      done();
    }
  });
  res.json({ status: 'Queue processing' });
});

server.listen('1245', () => {
  reserveSeat(50);
  console.log('The server is listening on 1245');
});
