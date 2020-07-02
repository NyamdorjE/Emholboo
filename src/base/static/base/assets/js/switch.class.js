				jQuery(function ($) {

				    $("#page-width").change(function () {
				        if ($(this).val() == 1200)
				            var w = "1200";
				        else {
				            var w = "100";
				        }
				        $.cookie("css-width", w, {
				            expires: 365
				        });
				        setTimeout(function () {
				            window.location.reload(true);
				        }, 100);
				    });
				    if ($.cookie("css-width")) {
				        var nw = $.cookie("css-width");
				        if (nw == "100") {
				            var nwb = "100%";
				            var nwl = "0px";
				            $.cookie("css-bg", null);
				        } else {
				            var nwb = "1200px";
				            var nwl = "auto";
				        }
				        $("div#wrapper").css("width", nwb);
				        $("nav").css("width", nwb);
				        $("nav").css("left", nwl);
				        $("#page-width option").each(function () {
				            if ($(this).val() == nw) {
				                $(this).attr("selected", "selected");
				            }
				        });
				    } else {
				        $("div#wrapper").css("width", "100%");
				    }
				    if ($.cookie("css") != null) {
				        $("#style-schem").attr("href", $.cookie("css"));
				    }
				    if ($.cookie("css-color") != null) {
				        $("#style-schem-color").attr("href", $.cookie("css-color"));
				    }
				    $("#color-skin a").click(function () {
				        $("link#style-schem-color").attr("href", "assets/css/layouts/" + $(this).data('rel') + ".css");
				        $.cookie("css-color", "assets/css/layouts/" + $(this).data('rel') + ".css", {
				            expires: 365
				        });

				        return false;
				    });
				    $("#dark-skin a").click(function () {
				        $("link#style-schem").attr("href", "assets/css/layouts/" + $(this).data('rel') + ".css")
				        $.cookie("css", "assets/css/layouts/" + $(this).data('rel') + ".css", {
				            expires: 365
				        });

				        return false;
				    });
				    $("#reset").click(function () {
				        $.cookie("css", null);
				        $.cookie("css-width", "100");
				        $.cookie("css-bg", null);

				        setTimeout(function () {
				            window.location.reload(true);
				        }, 10);
				    });

				});