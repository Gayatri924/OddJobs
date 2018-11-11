// latest build is available at this link as well
//https://raw.githubusercontent.com/GetStream/stream-js/master/dist/js/getstream.js

//var stream = require('getstream');
// Instantiate a new client (server side)
/*
window.sendMessage = function(){
  console.log("Helo")
}
*/
//private var key = '7a7vvthtmw7d';
//var secret = 'dxm9bj3zdgvf84jq4m9h362svdmz8neqfryptc9jsfkhur5nz5tbvmhyt9arbrqd';
import settings from .; 

<<<<<<< HEAD
window.sendMessage = function(){
    console.log("Hello")
}
client = stream.connect('xkwvpuatj96g', 'cq47pqm65e5749avhzbmcbgdb3wz8czhaxazez7gdrg6cqwpywcdzyxvfh6rcrmh', 'us-east');
=======
var client = stream.connect(settings.STREAM_API_KEY, settings.STREAM_API_SECRET, 'us-east');
>>>>>>> 3b784628d52fe50f95f5d0c1922bb05bf9f221da
// Instantiate a new client (client side)
client = stream.connect(settings.STREAM_API_KEY, null, 'us-east');
// Find your API keys here https://getstream.io/dashboard/

var chris = client.feed('user', 'chris');

<<<<<<< HEAD
=======

window.sendMessage = function(){
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
}


>>>>>>> 3b784628d52fe50f95f5d0c1922bb05bf9f221da
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
<<<<<<< HEAD
=======

>>>>>>> 3b784628d52fe50f95f5d0c1922bb05bf9f221da

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

var user1 = client.feed('user', '1');

// Client-side: Instantiate a feed for feed group 'user', user id '1' and a security token generated server side
var user1 = client.feed('user', '1', $token);

// Add an activity to the feed
var activity = {actor: 'User:1', verb: 'pin', object: 'Place:42', target: 'Board:1'};

// Asynchronous methods return Promise since v3.0.0
user1.addActivity(activity)
    .then(function(data) { /* on success */ })
    .catch(function(reason) { /* on failure, reason.error contains an explanation */ });
