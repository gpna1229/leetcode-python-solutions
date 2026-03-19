/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var moveZeroes = function(nums) {
    let flag = 0;
    for (var i = 0; i < nums.length; i++) {
        if (nums[i] != 0) {
            [nums[flag], nums[i]] = [nums[i], nums[flag]];
            flag ++;
        }
    }
};
