/** 
 * 对话框实现
 * 参考 https://www.layui.com/doc/modules/layer.html
 * 
 * 对外接口:
 * 1. 展示对话框并且自适应设备
 *    xnote.showDialog(title, html, buttons = [], functions = [])
 *    xnote.openDialog(title, html, buttons = [], functions = [])
 *    xnote.showDialogEx(options)
 * 
 * 2. 展示iframe页面
 *    xnote.showIframeDialog(title, url)
 *    xnote.showAjaxDialog(title, url, buttons, functions)
 * 
 * 3. 展示选项的对话框
 *    // option参数的定义 {html, title = false}
 *    xnote.showOptionDialog(option)
 * 
 * 4. 系统自带的弹窗替换
 *    xnote.alert(message)
 *    xnote.confirm(message, callback)
 *    xnote.prompt(title, defaultValue, callback)
 *    // 打开文本编辑的对话框
 *    xnote.showTextDialog(title, text, buttons, functions)
 *    xnote.openTextDialog(title, text, buttons, functions)
 * 
 */


if (window.xnote === undefined) {
    throw new Error("xnote is undefined!");
}

var xnoteDialogModule = {}
xnote.dialog = xnoteDialogModule;

xnoteDialogModule.idToIndexMap = {};

xnoteDialogModule.handleOptions = function (options) {
    if (options.dialogId === undefined) {
        options.dialogId = this.createNewId();
    }
    return options;
}

xnote.getDialogArea = function () {
    if (isMobile()) {
        return ['100%', '100%'];
    } else {
        return ['600px', '80%'];
    }
}

getDialogArea = xnote.getDialogArea;

xnote.getDialogAreaLarge = function() {
    if (xnote.isMobile()) {
        return ['100%', '100%'];
    } else {
        return ['80%', '80%'];
    }
}

xnote.getDialogAreaFullScreen = function() {
    return ["100%", "100%"];
}

xnote.getNewDialogId = function () {
    var dialogId = xnote.state._dialogId;
    if (dialogId === undefined) {
        dialogId = 1;
    } else {
        dialogId++;
    }
    xnote.state._dialogId = dialogId;
    return "_xnoteDialog" + dialogId;
}

xnoteDialogModule.showIframeDialog = function (title, url, buttons, functions) {
    var area = getDialogArea();
    return layer.open({
        type: 2,
        shadeClose: false,
        title: title,
        maxmin: true,
        area: area,
        content: url,
        scrollbar: false,
        btn: buttons,
        functions: functions
    });
}

xnoteDialogModule._getCloseAnim = function() {
    if (xnote.isMobile()) {
        return 2;
    } else {
        return undefined;
    }
}
// 关闭对话框的入口方法
xnoteDialogModule.closeDialog = function (flag) {
    if (xnote.isMobile()) {
        anim = 2; // 向下滑出
    }
    if (flag === "last") {
        // 如果你想关闭最新弹出的层，直接获取layer.index即可
        var index = layer.index;
        layer.close(index, xnoteDialogModule._getCloseAnim());
    }

    if (typeof(flag) === 'number') {
        layer.close(flag, xnoteDialogModule._getCloseAnim());
        // TODO 移除_dialogIdStack中的元素
    }
}

// 打开对话框
xnoteDialogModule.openDialogEx = function (options) {
    return xnoteDialogModule.openDialogExInner(options);
}

xnote.showDialogEx = function () {
    return xnoteDialogModule.openDialogEx.apply(xnoteDialogModule, arguments);
}

/**
 * 创建对话框
 * @param {object} options 创建选项
 * @param {string} options.title 标题
 * @param {string} options.html HTML内容
 * @param {list[string]} options.buttons 按钮文案
 * @param {list[function]} options.functions 回调函数(第一个是成功的回调函数)
 * @param {boolean} options.closeForYes 成功后是否关闭对话框(默认关闭)
 * @returns index
 */
xnoteDialogModule.openDialogExInner = function (options) {
    options = xnoteDialogModule.handleOptions(options);

    var area = options.area;
    var title = options.title;
    var html  = options.html;
    var buttons = options.buttons;
    var functions = options.functions;
    var anim = options.anim;
    var closeBtn = options.closeBtn;
    var onOpenFn = options.onOpenFn;
    var shadeClose = xnote.getOrDefault(options.shadeClose, false);
    var closeForYes = xnote.getOrDefault(options.closeForYes, true);
    var template = options.template;
    var defaultValues = options.defaultValues; // 模板的默认值
    var yesFunction = function(index, layero, dialogInfo) {};
    var successFunction = function(layero, index, that/*原型链的this对象*/) {};
    var dialogId = options.dialogId;

    // 详细文档 https://www.layui.com/doc/modules/layer.html
    // @param {int} anim 动画的参数
    // undefined: 默认动画
    // 0：平滑放大。默认
    // 1：从上掉落
    // 2：从最底部往上滑入
    // 3：从左滑入
    // 4：从左翻滚
    // 5：渐显
    // 6：抖动出现

    if (template !== undefined && html !== undefined) {
        throw new Error("不能同时设置template和html选项");
    }

    if (template !== undefined) {
        var templateBody = $(template).html();
        dialogId = xnote.getNewDialogId();

        var ele = $("<div>").attr("id", dialogId).html(templateBody);
        html = ele.prop("outerHTML");

        if (defaultValues !== undefined) {
            html = xnote.renderTemplate(html, defaultValues); 
        }
    }

    if (functions === undefined) {
        functions = [];
    }

    if (!(functions instanceof Array)) {
        functions = [functions];
    }

    if (functions.length>0) {
        yesFunction = functions[0];
    }

    if (area === undefined) {
        area = xnote.getDialogArea();
    }

    if (area == "large") {
        area = xnote.getDialogAreaLarge();
    }

    if (area == "fullscreen") {
        area = xnote.getDialogAreaFullScreen();
    }

    if (anim === undefined && xnote.isMobile()) {
        // 手机上默认从底部往上滑
        anim = 2;
    }

    var params = {
        type: 1,
        title: title,
        shadeClose: shadeClose,
        closeBtn: closeBtn,
        area: area,
        content: html,
        anim: anim,
        success: successFunction,
        // scrollbar是弹层本身的滚动条，不是整个页面的
        scrollbar: false
    }

    if (buttons !== undefined) {
        params.btn = buttons
        params.yes = function (index, layero) {
            console.log(index, layero);
            var dialogInfo = {
                id: dialogId
            };
            var yesResult = yesFunction(index, layero, dialogInfo);
            if (yesResult === undefined && closeForYes) {
                layer.close(index);
            }
            return yesResult;
        }
    }

    var index = layer.open(params);
    options.layerIndex = index;

    // id映射
    xnoteDialogModule.idToIndexMap[dialogId] = index;

    // 打开对话框的回调
    if (onOpenFn) {
        onOpenFn(index);
    }

    return index;
}

/**
 * 打开一个对话框
 * @param {string} title 标题
 * @param {string|DOM} html 文本或者Jquery-DOM对象 比如 $(".mybox")
 * @param {array} buttons 按钮列表
 * @param {array} functions 函数列表
 * @returns 弹层的索引
 */
xnoteDialogModule.openDialog = function(title, html, buttons, functions) {
    var options = {};
    options.title = title;
    options.html  = html;
    options.buttons = buttons;
    options.functions = functions;
    return xnoteDialogModule.openDialogEx(options);
}

xnoteDialogModule.showDialog = function () {
    return xnoteDialogModule.openDialog.apply(xnoteDialogModule, arguments);
}

// 打开文本对话框
xnoteDialogModule.openTextDialogByOption = function(options) {
    var title = options.title;
    var text = options.text;
    var buttons = options.buttons;
    var functions = options.functions;
    var features = options.features;

    var req = {};
    var dialogId = xnoteDialogModule.createNewId();

    req.title = title;
    req.dialogId = dialogId;
/*
<div class="card dialog-body">
    <textarea class="dialog-textarea"></textarea>
</div>

<div class="dialog-footer">
    <div class="float-right">
        <button class="large btn-default" data-dialog-id="{{!dialogId}}" onclick="xnote.dialog.closeByElement(this)">关闭</button>
    </div>
</div>
 */
    var div = $("<div>");
    var textarea = $("<textarea>").addClass("dialog-textarea").text(text);
    var dialogBody = $("<div>").addClass("card dialog-body").append(textarea);
    var btnBox = $("<div>").addClass("float-right");
    var closeBtn = $("<button>").attr("data-dialog-id", dialogId)
        .addClass("btn large btn-default")
        .attr("onclick", "xnote.dialog.closeByElement(this)")
        .text("关闭");
    var dialogFooter = $("<div>").addClass("dialog-footer").append(btnBox.append(closeBtn));

    if (buttons === undefined) {
        div.append(dialogBody);
        div.append(dialogFooter);
    } else {
        div.append(textarea);
    }

    req.html = div.html();
    req.buttons = buttons;
    req.functions = functions;
    if (features != undefined) {
        xnote._updateDialogFeatures(req, features);
    }
    return xnote.showDialogEx(req);
}

xnoteDialogModule.openTextDialog = function(title, text, buttons, functions, features) {
    return xnoteDialogModule.openTextDialogByOption({
        title: title,
        text: text,
        buttons: buttons,
        functions: functions,
        features: features
    });
}

xnote._updateDialogFeatures = function (options, features) {
    for (var i = 0; i < features.length; i++) {
        var item = features[i];
        if (item === "large") {
            options.area = "large";
        }
    }
}

/**
 * 打开ajax对话框
 * @param {object} options 打开选项
 */
xnoteDialogModule.openAjaxDialogEx = function (options) {
    var respFilter = xnote.getOrDefault(options.respFilter, function (resp) {
        return resp;
    });

    xnote.http.get(options.url, function (resp) {
        options.html = respFilter(resp);
        xnote.showDialogEx(options);
        // 刷新各种组件的默认值
        xnote.refresh();
    });
}

/**
 * 打开ajax对话框
 * @param {string} title 对话框标题
 * @param {string} url 对话框URL
 * @param {list<string>} buttons 按钮名称
 * @param {list<function>} functions 按钮对应的函数
 */
xnoteDialogModule.openAjaxDialog = function(title, url, buttons, functions) {
    var options = {};
    options.title = title;
    options.buttons = buttons;
    options.functions = functions;
    options.url = url;
    
    return xnoteDialogModule.openAjaxDialogEx(options);
}

// 函数别名
xnoteDialogModule.showAjaxDialog = function () {
    return xnoteDialogModule.openAjaxDialog.apply(xnoteDialogModule, arguments);
}

// 询问函数，原生prompt的替代方案
xnote.promptInternal = function(title, defaultValue, callback, formType) {
    if (layer && layer.prompt) {
        // 使用layer弹层
        layer.prompt({
            title: title,
            value: defaultValue,
            scrollbar: false,
            // formType: 0-文本, 1-密码框, 2-textarea
            formType: formType,
            area: ['400px', '300px']
        },
        function(value, index, element) {
            callback(value);
            layer.close(index);
        })
    } else {
        // 使用系统默认的prompt
        var result = prompt(title, defaultValue);
        callback(result);
    }
};

xnote.prompt = function(title, defaultValue, callback) {
    return xnote.promptInternal(title, defaultValue, callback, 0);
};


xnote.promptTextarea = function (title, defaultValue, callback) {
    var functions;

    if (callback) {
        functions = function (index, layero) {
            var inputText = layero.find("textarea").val();
            callback(inputText);
        }
    }
    return xnote.openTextDialog(title, defaultValue, ["确定", "取消"], functions);
}

// 确认函数
xnote.confirm = function(message, callback) {
    if (layer && layer.confirm) {
        layer.confirm(message,
        function(index) {
            callback(true);
            layer.close(index);
        });
    } else {
        var result = confirm(message);
        callback(result);
    }
};

// 警告函数
xnote.alert = function(message) {
    if (layer && layer.alert) {
        layer.alert(message);
    } else {
        alert(message);
    }
};

/**
 * 展示Toast信息
 * @param {string} message 展示信息
 * @param {number} time 显示时间
 * @param {function} callback 回调函数
 */
xnote.toast = function (message, time, callback) {
    if (layer && layer.msg) {
        layer.msg(message, {time: time});
    } else {
        myToast(message, time);
    }

    if (callback) {
        if (time === undefined) {
            time = 1000;
        }
        setTimeout(callback, time);
    }
}

var myToast = function(message, timeout) {
    if (timeout == undefined) {
        timeout = 1000;
    }
    var maxWidth = $(document.body).width();
    var maxHeight = $(document.body).height()
    var fontSize = 14;
    var toast = $("<div>").css({
        "margin": "0 auto",
        "position": "fixed",
        "left": 0,
        "top": "24px",
        "font-size": fontSize,
        "padding": "14px 18px",
        "border-radius": "4px",
        "background": "#000",
        "opacity": 0.7,
        "color": "#fff",
        "line-height": "22px",
        "z-index": 1000
    });
    toast.text(message);

    $(document.body).append(toast);

    // 宽度
    var width = toast.outerWidth();
    var left = (maxWidth - width) / 2;
    if (left < 0) {
        left = 0;
    }
    toast.css("left", left);

    // 高度
    var height = toast.outerHeight();
    var top = (maxHeight - height) / 2;
    if (top < 0) {
        top = 0;
    }
    toast.css("top", top);

    setTimeout(function() {
        toast.remove();
    }, timeout);
}

// 兼容之前的方法
window.showToast = window.xnote.toast;

/**
 * 展示选项对话框
 */
xnoteDialogModule.showOptionDialog = function (option) {
    var content = option.html;
    if (option.title === undefined) {
        option.title = false;
    }

    var oldStyle = $("body").css("overflow");
    $("body").css("overflow", "hidden");

    function recoveryStyle() {
        $("body").css("overflow", oldStyle);
    }

    var dialogIndex = layer.open({
        title: option.title,
        closeBtn: false,
        shadeClose: true,
        btn: [],
        content: content,
        skin: "x-option-dialog",
        yes: function (index, layero) {
            layer.close(index);
            // 恢复样式
            recoveryStyle();
        },
        cancel: function() {
            layer.close(index);
            // 恢复样式
            recoveryStyle();
        }
    });

    // 原组件点遮罩关闭没有回调事件，要重新一下
    $('#layui-layer-shade'+ dialogIndex).on('click', function(){
        console.log("xnote.showOptionDialog: shadowClose event")
        layer.close(dialogIndex);
        recoveryStyle();
    });
};

// 老版本的对话框，先保留在这里
window.ContentDialog = {
  open: function (title, content, size) {
    var width = $(".root").width() - 40;
    var area;

    if (isMobile()) {
      area = ['100%', '100%'];
    } else {
      if (size == "small") {
        area = ['400px', '300px'];        
      } else {
        area = [width + 'px', '80%'];
      }
    }

    layer.open({
      type: 1,
      shadeClose: true,
      title: title,
      area: area,
      content: content,
      scrollbar: false
    });
  }
}

xnote.closeAllDialog = function() {
    layer.closeAll();
}


// 自定义的dialog
$(function () {

    // 点击激活对话框的按钮
    $("body").on("click", ".dialog-btn", function() {
        var dialogUrl = $(this).attr("dialog-url");
        var dialogId = $(this).attr("dialog-id");
        var dailogTitle = $(this).attr("dialog-title");
        var optionSelector = $(this).attr("dialog-option-selector");
        if (dialogUrl) {
            // 通过新的HTML页面获取dialog
            $.get(dialogUrl, function(respHtml) {

                // 展示对话框
                xnote.showDialog(dailogTitle, respHtml);

                // 重新绑定事件
                xnote.fire("init-default-value");
            })
        } else if (optionSelector) {
            var html = $(optionSelector).html();
            var option = {};
            option.html = html;
            xnote.showOptionDialog(option);
        } else {
            xnote.alert("请定义[dialog-url]或者[dialog-option-selector]属性");
        }
    });


    /**
     * 初始化弹层
     */
    function initDialog() {
        // 初始化样式
        $(".x-dialog-close").css({
            "background-color": "red",
            "float": "right"
        });

        $(".x-dialog").each(function(index, ele) {
            var self = $(ele);
            var width = window.innerWidth;
            if (width < 600) {
                dialogWidth = width - 40;
            } else {
                dialogWidth = 600;
            }
            var top = Math.max((getWindowHeight() - self.height()) / 2, 0);
            var left = (width - dialogWidth) / 2;
            self.css({
                "width": dialogWidth,
                "left": left
            }).css("top", top);
        });

        $("body").css("overflow", "hidden");
    }

    /** 隐藏弹层 **/
    function onDialogHide() {
        $(".x-dialog").hide();
        $(".x-dialog-background").hide();
        $(".x-dialog-remote").remove(); // 清空远程的dialog
        $("body").css("overflow", "auto");
    }

    $(".x-dialog-background").click(function() {
        onDialogHide();
    });

    $(".x-dialog-close, .x-dialog-cancel").click(function() {
        onDialogHide();
    });

    function doModal(id) {
        initDialog();
        $(".x-dialog-background").show();
        $(".x-dialog-remote").show();
        $("#" + id).show();
    }

    xnote.initDialog = initDialog;
});

// 通过html元素来关闭对话框
xnoteDialogModule.closeByElement = function (target) {
    var dialogId = $(target).attr("data-dialog-id");
    if (dialogId) {
        var index = xnoteDialogModule.idToIndexMap[dialogId];
        layer.close(index, xnoteDialogModule._getCloseAnim());
    } else {
        // layer组件的ID
        var times = $(target).parents(".layui-layer").attr("times");
        layer.close(times, xnoteDialogModule._getCloseAnim());
    }
}

// 关闭最后的对话框
xnoteDialogModule.closeLast = function () {
    xnoteDialogModule.closeDialog("last");
}

xnoteDialogModule.createNewId = function() {
    return "dialog_" + xnote.createNewId();
}

// 别名
xnote.openAjaxDialog = xnoteDialogModule.openAjaxDialog;
xnote.openAjaxDialogEx = xnoteDialogModule.openAjaxDialogEx;
xnote.showAjaxDialog = xnoteDialogModule.showAjaxDialog;

xnote.showDialog = xnoteDialogModule.showDialog;
xnote.showDialogEx = xnoteDialogModule.openDialogEx;
xnote.openDialogEx = xnoteDialogModule.openDialogEx; 
xnote.openDialogExInner = xnoteDialogModule.openDialogExInner;
xnote.openDialog = xnoteDialogModule.openDialog;
xnote.closeDialog = xnoteDialogModule.closeDialog;

xnote.showIframeDialog = xnoteDialogModule.showIframeDialog;

xnote.showTextDialog = xnoteDialogModule.openTextDialog;
xnote.openTextDialog = xnoteDialogModule.openTextDialog;
xnote.showOptionDialog = xnoteDialogModule.showOptionDialog;
xnote.openTextArea = xnote.promptTextarea;
