<?php
    header('Content-Type: image/jpeg');
    
    include("image_resizing.php");
    
    $imgr = new imageResizing();

    if(isset($_POST['cropping-image']) && $_POST['cropping-image'] != NULL){
        
        $image = "/path/to/your/image/".$_POST['cropping-image']; // Change this path to get this feature works
        
        $imgr->load($image);        
        $imgX = intval($_POST['imgX']);
        $imgY = intval($_POST['imgY']);
        $imgW = intval($_POST['imgW']);
        $imgH = intval($_POST['imgH']);
        
        /*echo $imgX." ".$imgY." ".$imgW." ".$imgH;*/
        
        $imgr->resize($imgW,$imgH,$imgX,$imgY);
        $imgr->output($imgr->image_type);
    }

?>