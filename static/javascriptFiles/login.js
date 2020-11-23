
var galleryItems=document.getElementsByClassName('c');
var no_of_ids=12,no_of_imgs=46,timer=5000;

function showItems()
{
	for(var i=0;i<no_of_ids;i++)
	{
		galleryItems[i].classList.remove("show");
		galleryItems[i].classList.add("hide");
		 galleryItems[i].classList.remove("hide");
		galleryItems[i].classList.add("show");
	}
}
 
  
          
         
function collasec()
{
	
	var ind=(Math.floor(Math.random()*no_of_ids)+1);var arr='#i'+ind;
		
		$(arr).attr("src","http://localhost:8000/static/images/img"+ (Math.floor(Math.random() * no_of_imgs) + 1)+".jpg").stop(true,true).hide().fadeIn(8000);
				
		
	
		 setTimeout(collasec, timer);

}

window.onload=function(){showItems();

setTimeout(collasec, timer);



}