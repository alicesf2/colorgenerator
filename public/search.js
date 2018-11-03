function getHashParams() {
  var hashParams = {};
  var e, r = /([^&;=]+)=?([^&;]*)/g,
      q = window.location.hash.substring(1);
  while ( e = r.exec(q)) {
     hashParams[e[1]] = decodeURIComponent(e[2]);
  }
  return hashParams;
}
var params = getHashParams();
var song_arr;
document.getElementById('search-button').addEventListener('click', function() {
    var query = document.getElementById('search-bar').value;
    $.ajax({
      url: '/refresh_token',
      data: {
        'refresh_token': params.refresh_token
      }
    }).done(function(data) {
        $.ajax({
            url: `/search?query=${query}&access_token=${data.access_token}`
        }).done(function(data) {
            song_arr = data.song_arr;
            for (var i = 0; i < song_arr.length; i++) {
                document.getElementById('search_results').innerHTML += '<li>' + '<h4>Title: ' + song_arr[i].name + '<h4>Artists: ';
                for (var j = 0; j < song_arr[i].artists.length; j++) {
                    document.getElementById('search_results').innerHTML += song_arr[i].artists[j].name + ', ';
                }
                document.getElementById('search_results').innerHTML += '</li>';
            }
        });
    });
}, false);
