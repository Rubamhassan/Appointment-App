var date= new Date(year,month-1,day)

function next(){
	date.setDate(date.getDate()+1)
document.getElementById('displayDate').innerHTML = date.getFullYear()+" " +(date.getMonth()+1)+" "+date.getDate()
}
function prev(){
	date.setDate(date.getDate()-1)
document.getElementById('displayDate').innerHTML = date.getFullYear()+" " +(date.getMonth()+1)+" "+date.getDate()
}

