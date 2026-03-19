/**
 * @param {number} n
 * @return {string}
 */
var countAndSay = function(n) {
    let str = "1";
    for (var i = 0; i < n - 1; i++) {
        str = str.replace(/(.)\1*/g, (match) => match.length + match[0]);
    }
    return str;
};
