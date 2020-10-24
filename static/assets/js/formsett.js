

function updateElementIndex(el, prefixx, ndx) {
    var id_regex = new RegExp('(' + prefixx + '-\\d+-)');
    var replacement = prefixx + '-' + ndx + '-';
    if ($(el).attr("for")) $(el).attr("for", $(el).attr("for").replace(id_regex,
    replacement));
    if (el.id) el.id = el.id.replace(id_regex, replacement);
    if (el.name) el.name = el.name.replace(id_regex, replacement);
}

function addForm(btn, prefixx) {
    var formCount = parseInt($('#id_' + prefixx + '-TOTAL_FORMS').val());
    if (formCount < 1000) {
        // Clone a form (without event handlers) from the first form
        var row = $(".item:last").clone(false).get(0);

        // Insert it after the last form
        $(row).removeAttr('id').hide().insertAfter(".item:last").slideDown(300);

        // Remove the bits we don't want in the new row/form
        // e.g. error messages
        $(".errorlist", row).remove();
        $(row).children().removeClass("error");

        // Relabel or rename all the relevant bits
        $(row).find('.formsettt-field').each(function () {
            updateElementIndex(this, prefixx, formCount);
            $(this).val('');
            $(this).removeAttr('value');
            $(this).prop('checked', false);
        });

        // Add an event handler for the delete item/form link
        $(row).find(".delete").click(function () {
            return deleteForm(this, prefixx);
        });
        // Update the total form count
        $("#id_" + prefixx + "-TOTAL_FORMS").val(formCount + 1);

    } // End if

    return false;
}


function deleteForm(btn, prefixx) {
      var formCount = parseInt($('#id_' + prefixx + '-TOTAL_FORMS').val());
      if (formCount > 1) {
          // Delete the item/form
          var goto_id = $(btn).find('input').val();
          if( goto_id ){
            $.ajax({
                url: "/" + window.location.pathname.split("/")[1] + "/formsettt-data-delete/"+ goto_id +"/?next="+ window.location.pathname,
                error: function () {
                  console.log("error");
                },
                success: function (data) {
                  $(btn).parents('.item').remove();                 
                },
                type: 'GET'
            });
          }else{
            $(btn).parents('.item').remove();
          }

          var forms = $('.item'); // Get all the forms
          // Update the total number of forms (1 less than before)
          $('#id_' + prefixx + '-TOTAL_FORMS').val(forms.length);
          var i = 0;
          // Go through the forms and set their indices, names and IDs
          for (formCount = forms.length; i < formCount; i++) {
              $(forms.get(i)).find('.formsettt-field').each(function () {
                  updateElementIndex(this, prefixx, i);
              });
          }
      } // End if

      return false;
  }

  $("body").on('click', '.remove-form-row',function () {
    deleteForm($(this), String($('.add-form-row').attr('id')));
  });

  $("body").on('click', '.add-form-row',function () {
      return addForm($(this), String($(this).attr('id')));
  });
