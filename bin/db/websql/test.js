/** @html5rocks **/
var test.webdb    =   {};

var test.webdb.open = function() {
  var kByte  = 1024;
  var dbSize = kByte * kByte; // 1MB
  test.webdb.db = openDatabase("Test", "1.0", "the red fox jumps over the lazy brown dog", dbSize);
}

test.webdb.onError = function handle_error (tx, e) {
  // body...
  alert("There has been an error: " + e.message);
}

test.webdb.onSuccess = function notify_user (tx, r) {
  // body...
  alert("Test db passed.");
}