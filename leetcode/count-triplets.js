const countTriplets = function(arr) {
  const xorMap = new Map();
  xorMap.set(0, [1, 0, [-1]]);
  let curXorValue = 0;
  let res = 0;

  for(let i = 0; i < arr.length; i++) {
    curXorValue ^= arr[i];
    
    let n, total, indexes;
    if (!xorMap.has(curXorValue)) {
      xorMap.set(curXorValue, [0, 0, []]);
    }
    
    [n, total, indexes] = xorMap.get(curXorValue);
    const next = (n * i - total);
    console.log('info', {next, i, n, total});
    res += next;
    xorMap.set(curXorValue, [n + 1, total + i + 1, [...indexes, i]]);
  }

  console.log(Array.from(xorMap));
  console.log(res);

  // return result;
};

const countTriplets2 = function(arr) {
  const count = new Map();
  count.set(0, [1, -1]);

  let currentXorValue = 0;
  let result = 0;

  arr.forEach((num, i) => {
    currentXorValue ^= num;
    
    if (!count.has(currentXorValue)) {
      count.set(currentXorValue, [0, 0]);
    }
    
    const [n, total] = count.get(currentXorValue);
    result += (n * (i - 1) - total);
    count.set(currentXorValue, [n + 1, total + i]);
  })

  return result;
};

// countTriplets([2,3,1,6,7,4,8,9,5])
countTriplets([7,11,12,9,5,2,7,17,22]);
countTriplets2([7,11,12,9,5,2,7,17,22]);