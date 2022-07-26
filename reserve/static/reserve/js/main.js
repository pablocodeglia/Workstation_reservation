/////////////////////////
// FIND COWORKERS CODE //
/////////////////////////

const user_input = $("#user-input");
const search_icon = $("#search-icon");
const coworkers_div = $("#replaceable-content");
const endpoint = "/find_coworkers/";
const delay_by_in_ms = 700;
let scheduled_function = false;

let ajax_call = function (endpoint, request_parameters) {
  $.getJSON(endpoint, request_parameters).done((response) => {
    // fade out the coworkers_div, then:
    coworkers_div
      .fadeTo("slow", 0)
      .promise()
      .then(() => {
        // replace the HTML contents
        coworkers_div.html(response["html_from_view"]);
        // fade-in the div with new contents
        coworkers_div.fadeTo("slow", 1);
        // stop animating search icon
        search_icon.removeClass("fa-solid fa-circle-notch blink");
        search_icon.addClass("fas fa-search");
      });
  });
};

user_input.on("keyup", function () {
  const request_parameters = {
    q: $(this).val(), // value of user_input: the HTML element with ID user-input
  };

  // start animating the search icon with the CSS class
  search_icon.removeClass("fas fa-search");
  search_icon.addClass("fa-solid fa-circle-notch blink");

  // if scheduled_function is NOT false, cancel the execution of the function
  if (scheduled_function) {
    clearTimeout(scheduled_function);
  }

  // setTimeout returns the ID of the function to be executed
  scheduled_function = setTimeout(
    ajax_call,
    delay_by_in_ms,
    endpoint,
    request_parameters
  );
});

///////////////////////////
// PARSE JS TO FLOORPLAN //
///////////////////////////

const value = JSON.parse(
  JSON.parse(document.getElementById("ws_json").textContent)
);
