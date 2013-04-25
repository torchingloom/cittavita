$(function(){
	$('A[href=#]').live('click', function(e){
		e.preventDefault();
	});

	var storage = $('#storage'),
		initial = true;
	
	$.cycleSetHash = function( slide ) {
		var id = storage.children().eq( slide );
		if (id.length) window.location.hash = id.attr('id');
	};

	storage.cycle({
		fx      : 'scrollHorz',
		speed   : 600,
		timeout : 0,
		startingSlide : 0
	});
	
	var storageData = storage.data('cycle.opts');
	
	$('#next, #prev').click(function( e ){
		e.preventDefault();
		
		if($('.stack').is(':animated')) return false;
		
		initial = false;
		
		var isNext = this.id == 'next',
			nextSlide = isNext ? storageData.nextSlide : (storageData.currSlide == 0 ? storageData.slideCount : storageData.currSlide) -1;
		
		storageData.rev = isNext ? ( nextSlide == 0 ? true : false ) : ( nextSlide == (storageData.slideCount - 1) ? true : false);
		$.cycleSetHash( nextSlide );
	});


	$.router(/^(?:(page\d+)(?:-([a-z0-9_-]+))?)?$/i, function(m, pageID, imgID) {
		var idx,
			closeModal = true;
		
		if (typeof pageID === 'undefined' || !pageID.length) {
			idx = 0;
		} else {
			var el = $('#' + pageID);
			idx = el.index();
			if (idx < 0) idx = 0;
		}
		
		if (idx >= 0) {
			storage.cycle( idx );
			if (typeof imgID !== 'undefined' && imgID.length > 0) {
				
				var imgEl = $('#' + imgID), source = false;
				
				if (imgEl.length) {
					if (imgEl.attr('rel')) source = imgEl.attr('rel');
					else {
						source = imgEl.find('INPUT:hidden[name=ajaxhref]');
						if (source.length) source = source.val();
						else source = false;  
					}
				}
				
				if (source) {
					closeModal = false;
					jQuery.fn.modalBox({ 
						draggable              : false,
						setWidthOfModalLayer   : 896,
						setTypeOfFadingLayer   : 'custom',
						setStylesOfFadingLayer : {
							custom : 'background-color: #fff; filter: alpha(opacity=30); opacity: 0.3;'
						},
						callFunctionAfterShow  : function() {
							var el = this,
								nv = $('.item_thumbs', el.modalBoxBodyContent),
								nvcount = 0;;
							
							$('.item_image', el.modalBoxBodyContent).cycle({
								//fx                 : 'none',
								timeout            : 0,
								speed              : 250,
								startingSlide      : 0,
								pager              : $('.item_thumbs UL', el.modalBoxBodyContent),
								pagerAnchorBuilder : function(idx, slide) {
									return $('.item_thumbs LI:eq(' + idx + ') A', el.modalBoxBodyContent);
								}
							});
							
							listener(nv, nvcount);
						},
						callFunctionBeforeHide : function() {
							$('.item_image', this.modalBoxBodyContent).cycle('destroy');
						},
						callFunctionAfterHide  : function() {
							if (initial) {
								initial = false;
								$.cycleSetHash( storageData.currSlide );
							} else window.history.back();
						},
						minimalTopSpacingOfModalbox : 0,
						directCall: { 
							source : source
						}
					});
				} else initial = false;
			}
			
			if (closeModal) $.fn.modalBox('close');
		}
	});

	function listener(nv, nvcount){
		var _length = $('LI', nv).length,
			_thumbs = Math.ceil($('.item_thumbs_wrap', nv).width() / $('LI', nv).outerWidth(true)),
			_widthw = $('LI', nv).outerWidth(true) * _thumbs
			_countr = Math.ceil(_length / _thumbs) - 1;
		
		$('.prev', nv).addClass('disabled');
		
		if(_length <= _thumbs) $('.next', nv).addClass('disabled');
		
		nv.find('.next, .prev').click(function(e){
			e.preventDefault();
			
			if($(this).is('.disabled')) return false;
			
			nvcount += $(this).is('.next') ? 1 : -1;
			
			if(nvcount > 0) $('.prev', nv).removeClass('disabled');
			if(nvcount <= 0) $('.prev', nv).addClass('disabled');
			if(nvcount >= _countr) $('.next', nv).addClass('disabled');
			if(nvcount < _countr) $('.next', nv).removeClass('disabled');
			
			$('UL', nv).animate({
				left : _widthw * -nvcount
			});
		});
		
		
	}
	
	$(document).keydown(function(e){
		if(!$('#modalBoxFaderLayer').length){
			if(e.keyCode == 37) $('#prev').trigger('click');
			if(e.keyCode == 39) $('#next').trigger('click');
		}
	});
	
	$('.items .item_picture').not('.noborder .item_picture').each(function(){
		var el = $(this);
		el.css({
			marginTop  : el.height() / -2,
			marginLeft : el.width() / -2
		});
	});

	$('A.openmodalbox_width').click(function( e ){
		e.preventDefault();
		
		initial = false;
		
		if (this.id) {
			var currSlide = storage.children().eq( storageData.currSlide );
			if (currSlide.length) {
				window.location.hash = currSlide.attr('id') + '-' + this.id
			}
		}
	});
	
	//console.log();
});
