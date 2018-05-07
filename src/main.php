<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.11.2/jquery.min.js"></script>

<button id="1" name="sound1" value="sound1" type="button">Click Me</button>
<button id="2" name="sound2" value="sound2" type="button">Click Me2</button>
<p></p>
<script type="text/javascript">
    $(document).ready(function(){
        $("button").click(function(){
            var buttonVal = $(this).val();
            $.post('script.php', {sound: buttonVal},
            function(data) {
                    //alert(data);
                    $("p").text(data);

                });
   });
});
</script>
