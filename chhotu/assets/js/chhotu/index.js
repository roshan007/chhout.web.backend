$(document).ready(function(){

	var csrftoken = getCookie('csrftoken');
	function getCookie(name) {
		var cookieValue = null;
		if (document.cookie && document.cookie != '') {
			var cookies = document.cookie.split(';');
			for (var i = 0; i < cookies.length; i++) {
				var cookie = jQuery.trim(cookies[i]);
				if (cookie.substring(0, name.length + 1) == (name + '=')) {
					cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
					break;
				}
			}
		}
		return cookieValue;
	};
	careteProductCarousel("/products/?category=PRT,MGG", ".product1", "#myCarousel2");
	careteProductCarousel("/products/?category=BRG,SNW", ".product2", "#myCarousel3");
	careteProductCarousel("/products/?category=TST,BVR", ".product3", "#myCarousel4");
	careteProductCarousel("/products/?category=OTH", ".product4", "#myCarousel5");
	function careteProductCarousel(url, cls, id) {
		$.ajax({
			method: "GET",
			url: url,
			beforeSend: function (xhr) {
				xhr.setRequestHeader('X-CSRFToken', csrftoken)
			},
			success: function(response) {
				var htmlContent = "";
				$.each(response.results,function(key,val){
					htmlContent += (
						'<div class="col-lg-12 carousel-item products-carousel"><div class="container">'
						+'<div class="text-center">'
						+'<div class="card">'
						+'<img class="card-img-top" height="200px" width="100%" src="'+val.logo+'" alt="Card image cap">'
						+'<div class="card-block pt-10">'
						+'<p class="card-title text-xs-center">'+val.name+'</p>'
						+'<hr style="margin-top: 0;"/>'
						+'<h5 class="text-xs-left" style="display:inline-block"><i class="fa fa-inr" aria-hidden="true"></i> '+val.price+'</h5>'
						+'<select class="form-control" style="width: 60%;float: right;"><option value="">Quantity</option>'
							+'<option value="1">1</option>'
							+'<option value="2">2</option>'
							+'<option value="3">3</option>'
							+'<option value="4">4</option>'
							+'<option value="5">5</option>'
							+'<option value="6">6</option>'
							+'<option value="7">7</option>'
							+'<option value="8">8</option>'
							+'<option value="9">9</option>'
							+'<option value="10">10</option>'
						+'</select>'
						+'<div style="text-align: center;padding-top: 20px;">'
						+'<span class="text-xs-right"><a href="#" class="btn btn-primary btn-sm">Add to cart!</a></span>'
						+'</div>'
						+'</div>'
						+'</div>'
						+'</div>'
						+'</div>'
						+'</div>'
						);
				});
				$(cls).html(htmlContent);
				carousel(cls, id);
				function carousel(cls, id) {
					$(cls).slick({
						nextArrow: '<i class="fa fa-chevron-right" aria-hidden="true" style="position: absolute;top: 47%;right:0%;"></i>',
						prevArrow: '<i class="fa fa-chevron-left" aria-hidden="true" style="position: absolute;top: 47%;"></i>',
						infinite: true,
						slidesToShow: 4,
						slidesToScroll: 1,
						autoplay: false,
						autoplaySpeed: 4000,
						arrows : true,
						responsive: [{
							breakpoint: 1200,
							settings: {
								slidesToShow: 3,
								slidesToScroll: 3,
							}
						},
						{
							breakpoint: 768,
							settings: {
								slidesToShow: 2,
								slidesToScroll: 2,
							}
						},
						{
							breakpoint: 480,
							settings: {
								slidesToShow: 1,
								slidesToScroll: 1,
							}
						}]
					});
					$(id).carousel({
						interval:8000,
					});
				};
			},
			error: function (error) {

			},
		});
	};

	$("#logout-view").on("click", function(){
		$.ajax({
			type: 'GET',
			url: "/auth/logout/",
			beforeSend: function(xhr) {
				xhr.setRequestHeader("X-CSRFToken", csrftoken);
			},
			success: function(response) {
				window.location.href = "/";
			},
			error: function(error) {
				$("#loginerror").html(error.responseJSON.non_field_errors);
			}
		});
		return false;
	});
});