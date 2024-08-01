#!/usr/bin/node
import redis from 'redis';

const client = redis.createClient();

const cities = {
  Portland: 50,
  Seattle: 80,
  'New York': 20,
  Bogota: 20,
  Cali: 40,
  Paris: 2,
};

for (const key in cities) {
  if (key) {
    client.hset('HolbertonSchools', key, cities[key], (error) => {
      if (!error) {
        console.log('Reply: 1');
      }
      client.quit();
    });
  }
}

client.hgetall('HolbertonSchools', (error, data) => {
  console.log(data);
});

client.on('connect', () => console.log('Redis client connected to the server'));
client.on('error', (error) => console.log(`Redis client not connected to the server: ${error.message}`));
