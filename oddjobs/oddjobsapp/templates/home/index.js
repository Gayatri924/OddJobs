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
//import settings from "../../../oddjobs/settings.py";

/*function loadFile(filePath) {
  var result = null;
  var xmlhttp = new XMLHttpRequest();
  xmlhttp.open("GET", filePath, false);
  xmlhttp.send();
  if (xmlhttp.status==200) {
    result = xmlhttp.responseText;
  }
  return result;
}*/
/*var data = loadFile("secret.txt");//loadFile("oddjobs/oddjobsapp/templates/home/secret.txt");
var arrdata = data.split(" ");*/
var STREAM_API_KEY = "7a7vvthtmw7d";//arrdata[0];
//var STREAM_API_SECRET = arrdata[1];


var client = stream.connect(STREAM_API_KEY);//,STREAM_API_SECRET);//, 'us-east');
// Instantiate a new client (client side)
//client = stream.connect(STREAM_API_KEY, null, 'us-east');
// Find your API keys here https://getstream.io/dashboard/

var chris = client.feed('user', 'chris');


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

var user1 = client.feed('user', '1');

// Client-side: Instantiate a feed for feed group 'user', user id '1' and a security token generated server side
var user1 = client.feed('user', '1', $token);

// Add an activity to the feed
var activity = {actor: 'User:1', verb: 'pin', object: 'Place:42', target: 'Board:1'};

// Asynchronous methods return Promise since v3.0.0
user1.addActivity(activity)
    .then(function(data) { /* on success */ })
    .catch(function(reason) { /* on failure, reason.error contains an explanation */ });
