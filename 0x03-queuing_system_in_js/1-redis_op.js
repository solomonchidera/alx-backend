#!/usr/bin/node
import redis from 'redis';

const client = redis.createClient();

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, (error) => {
    if (!error) {
      redis.print(`${schoolName} Has been set to the value ${value}`);
    }
  });
}

function displaySchoolValue(schoolName) {
  client.get(schoolName, (error, value) => {
    if (!error) {
      console.log(`${schoolName} Has the value ${value}`);
    }
  });
}

client.on('connect', () => console.log('Redis client connected to the server'));
client.on('error', (error) => console.log(`Redis client not connected to the server: ${error.message}`));

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
