$(document).ready(function(){
    // disable refine button if none selected
    $('.btn-refine').attr('disabled', true);
    $('#sector, #salary, #location, #jobType').change(function(){
        if(this.value != '0'){
        $('.btn-refine').attr('disabled', false);
        }
        else {
            $('.btn-refine').attr('disabled', true);
            
        }
    }) 
})