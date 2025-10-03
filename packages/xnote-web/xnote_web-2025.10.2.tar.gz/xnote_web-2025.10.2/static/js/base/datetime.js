// @author xupingmao
// @since 2017/08/16
// @modified 2020/07/04 16:41:01

/**
 * 日期格式化
 * @param {string} format 日期格式
 */
if (!Date.prototype.format) {
    Date.prototype.format = function (format) {
        var year = this.getFullYear();
        var month = this.getMonth() + 1;
        var day = this.getDate();
        var hour = this.getHours();
        var minute = this.getMinutes();
        var second = this.getSeconds();
        if (format === undefined) {
            return sFormat("%d-%2d-%2d %2d:%2d:%2d", year, month, day, hour, minute, second);
        } if (format == "yyyy-MM-dd") {
            return sFormat("%d-%2d-%2d", year, month, day);
        } else if (format == "HH:mm:ss") {
            return sFormat("%2d:%2d:%2d", hour, minute, second);
        } else {
            throw new Error("invalid date format " + format);
        }
    };
}

