/**
 * @param {number[]} nums
 * @return {number[][]}
 */
const threeSum = (nums) => {
  let result = [];
  nums.sort((a, b) => a - b);

  for(let i = 0; i < nums.length - 2 && nums[i] <= 0; i++) {
    if (i > 0 && nums[i-1] === nums[i]) {
      continue;
    }

    let l = i+1, r = nums.length - 1;

    while(l < r) {
      const sum = nums[i] + nums[l] + nums[r];

      if (sum < 0) {
        l += 1;
      } else if (sum > 0) {
        r -= 1;
      } else { // sum == 0
        result.push([nums[i], nums[l], nums[r]]);

        while(l < r && nums[l] === nums[l+1]) {
          l += 1;
        }
        l += 1;

        while(l < r && nums[r] === nums[r-1]) {
          r -= 1;
        }
        r -= 1;
      }
    }
  }

  return result;
};