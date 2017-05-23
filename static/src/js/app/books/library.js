var v = new Vue({
    delimiters: ['[[',']]'],
	el:"#book",
	data:{
		books:[
		
		]
	}
})

var a = new Vue({
    delimiters: ['[[',']]'],
	el:"#kind",
	data:{
		kind0:true,kind1:false,kind2:false,kind3:false,kind4:false,kind5:false,kind6:false,kind7:false,kind8:false,
		kind9:false,kind10:false,kind11:false,kind20:false,kind21:false,kind22:false,kind23:false,kind24:true,
		kind30:false,kind31:false,kind32:false,kind33:false,kind34:true,kind40:true,kind41:false,kind42:false,
		kind43:false,kind50:true,kind51:false,kind52:false,kind60:true,kind61:false,kind62:false,kind70:true,
		kind71:false,kind72:false,
		send1:0,send2:4,send3:4,send4:0,send5:0,send6:0
	},
	methods:{
		tokind:function(num1, num2, e){
			var num=num1*10-10+num2;
			if (num1==1){
				this.kind0=this.kind1=this.kind2=this.kind3=this.kind4=this.kind5=
				this.kind6=this.kind7=this.kind8=this.kind9=
				this.kind10=this.kind11=false;
				this.send1=num2;
			}
			else if (num1==3){
				this.kind20=this.kind21=this.kind22=this.kind23=this.kind24=false;
				this.send2=num2;
			}
			else if (num1==4){
				this.kind30=this.kind31=this.kind32=this.kind33=this.kind34=false;
				this.send3=num2;
			}
			else if (num1==5){
				this.kind40=this.kind41=this.kind42=this.kind43=false;
				this.send4=num2;
			}
			else if (num1==6){
				this.kind50=this.kind51=this.kind52=false;
				this.send5=num2;
			}
			else if (num1==7){
				this.kind60=this.kind61=this.kind62=false;
				this.send6=num2;
			}
			console.log(num);
			if (num==0) this.kind0=true;
			else if (num==1) this.kind1=true;
			else if (num==2) this.kind2=true;
			else if (num==3) this.kind3=true;
			else if (num==4) this.kind4=true;
			else if (num==5) this.kind5=true;
			else if (num==6) this.kind6=true;
			else if (num==7) this.kind7=true;
			else if (num==8) this.kind8=true;
			else if (num==9) this.kind9=true;
			else if (num==10) this.kind10=true;
			else if (num==11) this.kind11=true;
			else if (num==20) this.kind20=true;
			else if (num==21) this.kind21=true;
			else if (num==22) this.kind22=true;
			else if (num==23) this.kind23=true;
			else if (num==24) this.kind24=true;
			else if (num==30) this.kind30=true;
			else if (num==31) this.kind31=true;
			else if (num==32) this.kind32=true;
			else if (num==33) this.kind33=true;
			else if (num==34) this.kind34=true;
			else if (num==40) this.kind40=true;
			else if (num==41) this.kind41=true;
			else if (num==42) this.kind42=true;
			else if (num==43) this.kind43=true;
			else if (num==50) this.kind50=true;
			else if (num==51) this.kind51=true;
			else if (num==52) this.kind52=true;
			else if (num==60) this.kind60=true;
			else if (num==61) this.kind61=true;
			else if (num==62) this.kind62=true;

			$.get("/books/1/", {kind:this.send1, word:this.send2, hot:this.send3, datetime:this.send4, free:this.send5, finish:this.send6}, function(data){
				data=$.parseJSON(data);
				console.log(data);
				v.books=data.books;
			})
		}
	}
})

$.get("/LibraryViewAPI/", {kind:this.send1, word:this.send2, hot:this.send3, datetime:this.send4, free:this.send5, finish:this.send6}, function(data){
	data=$.parseJSON(data);
	console.log(data);
	v.books=data.books;
})