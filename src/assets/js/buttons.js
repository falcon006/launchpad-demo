$(document).ready(function(){
    $("button").click(function(){
        var buttonVal = $(this).val();
        $.post('script.php',
               {sound: buttonVal},
                function(data) {
                    //alert(data);
                    $("p").text(data);
                });
    });
});
