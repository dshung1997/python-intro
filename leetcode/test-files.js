const gen = (n = 3) => {
  const count = {};

  for(let i = 0; i < n; i++) {
    count[i] = {
      likes: 10000,
      dislikes: 1000,
    }
  }

  console.log(JSON.stringify(count));
};

gen(1800);