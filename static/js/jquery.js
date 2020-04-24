$(document).ready(function(){
    var myNav = $(".navbar");
    // Set different background on NavBar while scrolling
    $(window).on('scroll', function() {
    "use strict";
    if ($(window).scrollTop() >= 100) {
        myNav.addClass("scroll");
    }
    else {
        myNav.removeClass("scroll");
    }
    });
     
    // This steps were insired from GeeksforGeeks and StackOverflow
    // Add and remove ingredient row
    $("#addIngridient").click(function() {
        $('<input class="form-control" id="ingredients" type="text" name="ingredients" required type="text" value="">').insertBefore('#addIngridient');	
         });
        // Remove aditional row
	$('#removeIngridient').click(function() {
		$('#ingredientsList input:last').remove();
	});
                
      // add and remove step
      //Add aditional preparations step row
	$('#addSteps').click(function() {
		$('<input class="form-control" id="steps" type="text" name="steps" required type="text" value="">').insertBefore('#addSteps');

	});	
	
	
	// Remove aditional preparation step row
	$('#removeSteps').click(function() {
		$('#stepsList input:last').remove();
    });
    

    // Hide flash messages
    $('.alert').alert()

    $(".alert").click(function(){
     ("button").hide("slow");
    });
 }); 




