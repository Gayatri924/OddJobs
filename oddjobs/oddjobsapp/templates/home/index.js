// install via npm
npm install getstream --save

// install using bower
bower install getstream

// latest build is available at this link as well
https://raw.githubusercontent.com/GetStream/stream-js/master/dist/js/getstream.js

var stream = require('getstream');
// Instantiate a new client (server side)
client = stream.connect('7a7vvthtmw7d', 'dxm9bj3zdgvf84jq4m9h362svdmz8neqfryptc9jsfkhur5nz5tbvmhyt9arbrqd', 'us-east');
// Instantiate a new client (client side)
client = stream.connect('7a7vvthtmw7d', null, 'us-east');
// Find your API keys here https://getstream.io/dashboard/

var chris = client.feed('user', 'chris');

// Add an Activity; message is a custom field - tip: you can add unlimited custom fields!
chris.addActivity({
  actor: 'chris',
  verb: 'add',
  object: 'picture:10',
  foreign_id: 'picture:10',
  message: 'Beautiful bird!'
}).then(
  null, // nothing further to do
  function(err) {
    // Handle or raise the Error.
  }
);

// Create a following relationship between Jack's "timeline" feed and Chris' "user" feed:
var jack = client.feed('timeline', 'jack');
jack.follow('user', 'chris').then(
  null, // nothing further to do
  function(err) {
    // Handle or raise the Error.
  }
);


// Read Jack's timeline and Chris' post appears in the feed:
jack.get({ limit: 10 }).then(function(results) {
  var activityData = results; // work with the feed activities
},function(err) {
    // Handle or raise the Error.
});

// Remove an Activity by referencing it's Foreign Id:
chris.removeActivity({ foreignId: 'picture:10' }).then(
  null, // nothing further to do
  function(err) {
    // Handle or raise the Error.
  }
);