/**
 * Created by erik on 11/14/15.
 */

    //called when page is loaded.
    $(document).ready(function() {
        displaySigninButtons();
    });

    //displays welcome and hides signin
    function displaySigninButtons() {
         if (sessionStorage.getItem('email') != null) {
             $('#FB_signinButton').attr('style', 'display: none');
             $('#GP_signinButton').attr('style', 'display: none');
             $('#user_id').text("Welcome " + sessionStorage.getItem('email'));
       }
    }
function signInCallback(authResult) {
  if (authResult['code']) {
    // Hide the sign-in button now that the user is authorized
      displaySigninButtons();
    // Send the one-time-use code to the server, if the server responds, write a 'login successful' message to the web page and then redirect back to the main restaurants page
    $.ajax({
      type: 'POST',
      url: '/gconnect?state={{STATE}}',
      processData: false,
      data: authResult['code'],
      contentType: 'application/octet-stream; charset=utf-8',
      success: function(result) {
        // Handle or verify the server response if necessary.
        if (result) {

            //$('#result').html('Login Successful!</br>'+ result + '</br>Redirecting...');

            console.log(authResult);
            $.ajax(
                    {
                        type: 'POST',
                        url: 'https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=' + authResult['access_token'],
                        success: function(result2){
                            console.log(result2);
                            sessionStorage.setItem("email", result2.email);
                            sessionStorage.setItem("user_id", result2.user_id);

                        }
                    });

        } else if (authResult['error']) {
          console.log('There was an error: ' + authResult['error']);
        } else {
          $('#result').html('Failed to make a server-side call. Check your configuration and console.');
        }
      },
      error: function(result) {
        console.log('There was an error: ' + result);
      }

  }); } }


<!--FACEBOOK SIGN IN -->
  window.fbAsyncInit = function() {
  FB.init({
    appId      : '734426900022927',
    cookie     : true,  // enable cookies to allow the server to access
                        // the session
    xfbml      : true,  // parse social plugins on this page
    version    : 'v2.2' // use version 2.2
  });
  };
  // Load the SDK asynchronously
  (function(d, s, id) {
    var js, fjs = d.getElementsByTagName(s)[0];
    if (d.getElementById(id)) return;
    js = d.createElement(s); js.id = id;
    js.src = "//connect.facebook.net/en_US/sdk.js";
    fjs.parentNode.insertBefore(js, fjs);
  }(document, 'script', 'facebook-jssdk'));

  // Here we run a very simple test of the Graph API after login is
  // successful.  See statusChangeCallback() for when this call is made.
  function sendTokenToServer() {
    var access_token = FB.getAuthResponse()['accessToken'];
    console.log(access_token)
    console.log('Welcome!  Fetching your information.... ');
    FB.api('/me', function(response) {
      console.log('Successful login for: ' + response.name);
     $.ajax({
      type: 'POST',
      url: '/fbconnect?state={{STATE}}',
      processData: false,
      data: access_token,
      contentType: 'application/octet-stream; charset=utf-8',
      success: function(result) {
        // Handle or verify the server response if necessary.
        FB.api('/me', {fields: 'email, name, picture'}, function(response) {
        //  FB.api('/me',  function(response) {
            console.log(response);
             if (result) {
                 displaySigninButtons();
                 sessionStorage.setItem("email", response.email);
                 sessionStorage.setItem("picture", response.picture.data.url);
                 sessionStorage.setItem("name", response.name);
             }
            else {
                $('#result').html('Failed to make a server-side call. Check your configuration and console.');
            }
        });


      }


  });
    });
  }


