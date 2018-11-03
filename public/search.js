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
            var search_list = '';
            for (var i = 0; i < song_arr.length; i++) {
                search_list += '<li>' + '<h4>Title: ' + song_arr[i].name + '<h4>Artists: ';
                for (var j = 0; j < song_arr[i].artists.length; j++) {
                    search_list += song_arr[i].artists[j].name;
                    if (j != song_arr[i].artists.length - 1) {
                        search_list += ', ';
                    }
                }
                search_list += '<h3>id: ' + song_arr[i].id + '</h3>';
                search_list += '</li>';
            }
            document.getElementById('search_results').innerHTML = search_list;
        });
    });
}, false);

var features;
document.getElementById('generate-colors').addEventListener('click', function() {
    var id = document.getElementById('input-id').value;
    $.ajax({
      url: '/audio-features',
      data: {
        'refresh_token': params.refresh_token
      }
    }).done(function(data) {
        $.ajax({
            url: `/audio-features?id=${id}&access_token=${data.access_token}`
        }).done(function(data) {
            features = data.features;
        });
    });
}, false);
