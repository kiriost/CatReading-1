var choose = $('.chooseleft');
var loginYes = $('.loginYes');
var loginNo = $('.loginNo');

choose.click(function(){
        loginYes.toggle();
	    loginNo.toggle();
	})



$('#captcha-img').click(function(){
        $("#captcha-img")[0].src = "/captcha/?" + Math.random();
        $("#captcha")[0].value = "";
});


////输入框聚焦时
//identify.focus(function(){
//	 identify.keyup(function(){
//	 if(identify.val()!=code){
//		$('#codeFalse').show();
//		$('#codeTrue').hide();
//	 }else if(identify.val()==code){
//		$('#codeFalse').hide();
//		  $('#codeTrue').show();
//	 }
//	 })
//})


$("form").on("submit", function(){
	var phone = $("#phone").val();
	var captcha = $("#captcha").val();

	$.ajax({
		beforeSend: csrfTokenHeader,
		url: "/MessageAPIView/",
  		async: false,
		data: {phone: phone, captcha: captcha, pageState: 0},
		dataType: "json",
		type: "GET",
		success: function (data) {
			console.log(data.code);
			if(!data.code) {
				console.log(data.data)
				window.location.href = "/twoRegister/";
			}
			else{
//			    alert(data.data)
			    $('#message').append(data.data)
			}
		},
		error: function (){
			alert("错误");
		}
	});
	return false;
});

