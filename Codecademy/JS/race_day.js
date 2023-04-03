let raceNumber = Math.floor(Math.random() * 1000);

console.log(`Race number is ${raceNumber}`);

let registeredEarly = false;

let runnerAge = 20;

if (runnerAge > 18 && registeredEarly === true) {
  raceNumber += 1000;
}

if (runnerAge > 18 && registeredEarly === true) {
  console.log(
    `The race number for early registered adult runners is ${raceNumber} 
and they will race at 9:30 am.`
  );
} else if (runnerAge > 18 && registeredEarly === false) {
  console.log(
    `The race number for lately registered adult runners is ${raceNumber} 
and they will race at 11:00 am.`
  );
} else if (runnerAge < 18) {
  console.log(
    `Under 18 runners will race at 12:30 pm in race number ${raceNumber}`
  );
} else {
  console.log(
    `Runners who are exactly 18 years old are instructed to visit to the 
registration desk`
  );
}

