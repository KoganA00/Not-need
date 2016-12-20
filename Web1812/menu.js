
function changeGeography()
{
	blackAll();
	var image=document.getElementById("geography");	
	var name="geography1.png";
	image.src=name;
}

function changeAnimals()
{
	blackAll();
	var image=document.getElementById("animals");	
	var name ="animals1.png";
	image.src=name;
}
function changeClimate()
{
	blackAll();
	var image=document.getElementById("climate");	
	var name ="climate1.png";
	image.src=name;
}
function changePolitics()
{
	blackAll();
	var image=document.getElementById("politics");	
	var name ="politics1.png";
	image.src=name;
}
function blackAll()
{
	var image=document.getElementById("animals");	
	var name ="animals.png";
	image.src=name;
	var image=document.getElementById("geography");	
	var name ="geography.png";
	image.src=name;
	var image=document.getElementById("politics");	
	var name ="politics.png";
	image.src=name;
	var image=document.getElementById("climate");	
	var name ="climate.png";
	image.src=name;
}