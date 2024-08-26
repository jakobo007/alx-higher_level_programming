#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const tasks = JSON.parse(body);
    const completedTaskByUser = {};

    tasks.forEach(task => {
        if(task.completed) {
            if (!completedTaskByUser[task.UserId]) {
                completedTaskByUser[task.UserId] = 0;
            }
            completedTaskByUser[task.UserId]++;
        }
    });
    console.log(completedTaskByUser);
  }
});
