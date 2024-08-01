#!/usr/bin/node
import redis from 'redis';
import { promisify } from 'util';

const client = redis.createClient();

const asyncSet = promisify(client.set).bind(client);

async function setNewSchool(schoolName, value) {
  try {
    await asyncSet(schoolName, value);
    console.log(`${schoolName} Has been set to the value ${value}`);
  } catch (error) {
    console.log(`There has been an error while setting ${schoolName} to ${value}`);
  } finally {
    client.quit();
  }
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
