#!/usr/bin/node
import redis from 'redis';

const client = redis.createClient();

function publishMessage(message, time) {
  setTimeout(() => {
    client.publish('holberton school channel', `${message}`);
  }, time);
  console.log(`About to send ${message}`);
}

client.on('connect', () => console.log('Redis client connected to the server'));
client.on('error', (error) => console.log(`Redis client not connected to the server: ${error.message}`));

publishMessage('Holberton Student #1 starts course', 100);
publishMessage('Holberton Student #2 starts course', 200);
publishMessage('KILL_SERVER', 300);
publishMessage('Holberton Student #3 starts course', 400);
