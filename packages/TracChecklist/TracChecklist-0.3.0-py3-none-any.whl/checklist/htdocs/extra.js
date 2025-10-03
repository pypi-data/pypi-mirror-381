/*
 Toggles visibility of extra / collapsible content below checklist steps.
 Extra content is marked in the wiki template with:

    [x] this is a step to do //
    [+]
        This is some extra content ...
    [-]

The macro.py expander converts this into html with the structure:

    <label class="container">
      <input type="checkbox" name="step_2" value="done" checked="">This is a step to do
      <span class="checkmark"></span>
      <span class="extra">&#9432;</span>
    </label>

    <div class="extra">
        This is some extra content ...
    </div>

*/

$(document).ready(function () {
    // Attach a click handler to every span that should act as a toggle
    $('span.extra').on('click', function (e) {

        // Prevent the click from toggling the checkbox itself
        e.preventDefault();

        // get the .extra div
        var divId = $(this).attr('id') + '_div';
        // console.log("Extra toggled for " + divId);

        // Toggle its visibility – set height
        var divSize = $('#' + divId).height();
        // console.log("divSize is " + divSize);

        if (divSize > 1) {
            $('#' + divId).height(0);
        } else {
            $('#' + divId).height('auto');
        }

    });

    // Start with all extras hidden – set height to zero
    $('div.extra').height(0);
  });