var date= new Date(year,month-1,day)

var x = JSON.parse(JSON.stringify(taken_appts));
x = taken_appts;

console.log('taken_appts: '+JSON.stringify(x,null,4));
// console.log(x[0]);
// console.log(x[1]);
// console.log(x[2]);
// console.log(x[3]);
// console.log(x[4]);
// console.log(x[5]);

// console.log(x[6]);
// console.log(x[7]);
// console.log(x[8]);
// console.log(x[9]);
// console.log(x[10]);

function next(){
	date.setDate(date.getDate()+1)
document.getElementById('displayDate').innerHTML = date.getFullYear()+" " +(date.getMonth()+1)+" "+date.getDate()
}
function prev(){
	date.setDate(date.getDate()-1)
document.getElementById('displayDate').innerHTML = date.getFullYear()+" " +(date.getMonth()+1)+" "+date.getDate()
}

function cellClick(provider_id, appt_time){
	alert(provider_id+appt_time)
}