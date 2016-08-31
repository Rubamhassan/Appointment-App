var date= new Date(year,month-1,day)

taken_appts = JSON.parse(JSON.stringify(taken_appts));

function cleanTaken_appts(){
	for(var i=0;i<taken_appts.length;i++){
		if(taken_appts[i].appt_time[0] == '&'){
			taken_appts[i].appt_time = String(taken_appts[i].appt_time).slice(5).slice(0,-5);
			taken_appts[i].appt_date = String(taken_appts[i].appt_date).slice(5).slice(0,-5);
		}
	}
}

cleanTaken_appts();
console.log('taken_appts: '+JSON.stringify(taken_appts,null,4));

isDoctor = isDoctor==="True"?true:false;
console.log(isDoctor)

function getID(p_id, time){
	var conversion = {
		'8:00am': 1,
		'9:00am': 2,
		'10:00am': 3,
		'11:00am': 4,
		'1:00pm': 5,
		'2:00pm': 6,
		'3:00pm': 7,
		'4:00pm': 8,
		'5:00pm': 9
	}
	return String(p_id)+String(conversion[time]);
}

// set cells disabled
function disableCells(){
	taken_appts.forEach(function(appt){
		var id = getID(appt.provider_id, appt.appt_time);

		if((date.getMonth()+1)+"/"+date.getDate()+"/"+date.getFullYear()
			=== appt.appt_date){
			if(!isDoctor){
				document.getElementById(id).innerHTML = 'unavailable';
				document.getElementById(id).bgColor = "lightgrey";
				document.getElementById(id).onclick = function(){
					alert('this slot is not available, chose another spot');
				}
			}
			else{
				document.getElementById(id).innerHTML = appt.first_name+' '+appt.last_name;
				document.getElementById(id).bgColor = "lightgrey";	
			}
		}
	});
}

function generateNextPrevLinks(){
	// next
	var elem = document.getElementById('next');
	date.setDate(date.getDate()+1);
	var link = 'appt_book?appt_year='
		+date.getFullYear()+'&appt_month='
		+(date.getMonth()+1)+'&appt_day='
		+date.getDate();
	elem.setAttribute("href", link);

	if(!isDoctor){
		var today = new Date();
		today = new Date(today.getFullYear(), today.getMonth(), today.getDate());
		today.setDate(today.getDate()+3);
		if(date <= today){
			return;
		}
	}

	// prev
	elem = document.getElementById('prev');
	date.setDate(date.getDate()-2);
	link = 'appt_book?appt_year='
		+date.getFullYear()+'&appt_month='
		+(date.getMonth()+1)+'&appt_day='
		+date.getDate();
	elem.setAttribute("href", link);

	// reset date
	date.setDate(date.getDate()+1);
}

generateNextPrevLinks();
disableCells();

function cellClick(provider_id, appt_time){
	if(isDoctor){
		// do nothing
	}
	else{
		var url = "/appt_book/"+date.getFullYear()+"/"+(date.getMonth()+1)
			+"/"+date.getDate()+"/"+provider_id+"/"+appt_time;
		

		$.post(url,
    	   function() {
			alert('Appointment saved successfully!');
			$(location).attr('href', "/confirm_appt");
    	   });
	}
}