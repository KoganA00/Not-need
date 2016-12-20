jQuery(document).ready(function(){
	function htmSlider(){
		/* Зададим следующие переменные */

		/* обертка слайдера */
		var slideWrap = jQuery('.slide-wrap');
		/* ссылки на предудыщий иследующий слайд */
		var nextLink = jQuery('.next-slide');
		var prevLink = jQuery('.prev-slide');

		var playLink = jQuery('.auto');
		
		var is_animate = false;
		
		/* ширина слайда с отступами */
		var slideWidth = jQuery('.slide-item').outerWidth();
		
		/* смещение слайдера */
		var newLeftPos = slideWrap.position().left - slideWidth;
		
		/* Клик по ссылке на следующий слайд */
		nextLink.click(function(){
			if(!slideWrap.is(':animated')) {
	
				slideWrap.animate({left: newLeftPos}, 500, function(){
					slideWrap
						.find('.slide-item:first')
						.appendTo(slideWrap)
						.parent()
						.css({'left': 0});
				});

			}
		});

		/* Клик по ссылке на предыдующий слайд */
		prevLink.click(function(){
			if(!slideWrap.is(':animated')) {
			
				slideWrap
					.css({'left': newLeftPos})
					.find('.slide-item:last')
					.prependTo(slideWrap)
					.parent()
					.animate({left: 0}, 500);

			}
		});
		
		
		
	

	}

	/* иницилизируем функцию слайдера */
	htmSlider();
});