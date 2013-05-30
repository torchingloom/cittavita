
basket = {
    add : function (item_id, count)
    {
    	count = count || 1
        this.show_loading()
        $.getJSON
        (
            '/item-add-to-basket/'+ item_id +'/'+ count,
            function(data)
            {
                if (data.add_status)
                {
                    return basket.show_ok()
                }
                basket.show_nook()
            }
        );
    },

    show_loading : function ()
    {
        $('.basket-addbutton').hide()
        $('.basket-loading').show()
    },

    show_ok : function ()
    {
        $('.basket-loading').hide()
        $('.basket-added').show()
    },

    show_nook : function ()
    {
        $('.basket-loading').hide()
        $('.basket-added').hide()
        $('.basket-addbutton').show()
    }
}