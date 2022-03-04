var flashID = "nothing";
var flashID2 = "nothing";
var origColor = "";
var loaded = false;
var selected_Row = -1;
var hostname = window.location.protocol + '//' + window.location.hostname;
function flashtext(ele, ele2, col) {
    
    var tmpColCheck = 0;
    if (ele != "nothing"){
        tmpColCheck = document.getElementById(ele).style.color;
    }
    else{
        return false;
    }

    if (tmpColCheck === origColor) {
        if (ele != "nothing"){
            $('.' + ele).css("color", col);
        }
        if (ele2 != "nothing"){
            $('.' + ele2).css("color", col);
        }
    } else {
        if (ele != "nothing"){
            $('.' + ele).css("color", origColor);
        }
        if (ele2 != "nothing"){
            $('.' + ele2).css("color", origColor);
        }
    }
    
    
    // console.log(flashID);
    // console.log(flashID2);
}


function rowClick(ele1, ele2){
    if (ele1 == flashID && ele2 == flashID2){
        return true;
    }
    if (flashID != "nothing"){
        var wut = "#r" + flashID.substring(3) +"btnCol";
        $(wut).hide();
    //      console.log("hide " + wut);
        $('.' + flashID).css("color", origColor);
    //      document.getElementById(flashID).style.color = origColor;
    }
    if (flashID2 != "nothing"){
        $('.' + flashID2).css("color", origColor);
    //  document.getElementById(flashID2).style.color = origColor;
    }
    if (ele1 != "nothing"){
       origColor =  $('.' + ele1).css("color");
    //      origColor = document.getElementById(ele1).style.color;
    }
    flashID = ele1;
    flashID2 = ele2;
    
    console.log(flashID);
    console.log(flashID2);
    
    var wut = "#r" + ele1.substring(3) +"btnCol";
    //  var data = document.getElementById(wut).innerHTML;
    $(wut).show("slow");
    
}




$.extend(
{
    redirectPost: function(location, args)
    {
        var form = '';
        $.each( args, function( key, value ) {
            value = value.split('"').join('\"');
            form += '<input type="hidden" name="'+key+'" value="'+value+'">';
        });
        $('<form action="' + location + '" method="POST">' + form + '</form>').appendTo($(document.body)).submit();
    }

    
});
$.extend({
    redirectGet: function(location, args)
    {
        var form = '';
        $.each( args, function( key, value ) {
            value = value.split('"').join('\"');
            form += '<input type="hidden" name="'+key+'" value="'+value+'">';
        });
        $('<form action="' + location + '" method="GET">' + form + '</form>').appendTo($(document.body)).submit();
    }
});

setInterval(function () {
    flashtext(flashID, flashID2, 'blue');
}, 500); //set an interval timer up to repeat the function


// setInterval(function () {
//     reloadTable();
//     console.log("TABLE RELOADED");
// }, 50000);
reloadTable();

function reloadTable(){

     $.get( hostname + "/getTable", function( data ) {
                  $( "#tableHere" ).html( data );
                //   alert( "Load was performed." );
                });
 }

 function editReq(rowID){
        var editURL = hostname + "/edit";
        $.redirectGet(editURL, {studentKey: "" + rowID});
 }


  function removeReq(rowID){
        var editURL = hostname + "/remove";
        $.redirectPost(editURL, {studentKey: "" + rowID});
        // $.post(redirectPost(editURL, {studentKey: rowID});
 }



 window.addEventListener('click', function(e){   
  if (document.getElementById('mainTable').contains(e.target)){
    // Clicked in box
  } else{
    $(".btnCol").hide();
  }
});