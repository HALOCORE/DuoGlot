let arr = [1, 2, 3, 4, 5, 6, 7, 8, 9];
let a = 1;
let b = -2;
arr.slice(a);
arr.slice(a);
arr.slice(0, b);
arr.filter((x, idx) => idx % b === 0);
arr.slice().reverse().filter((x, idx) => idx % 2 === 0);
arr.filter((x, idx) => idx % 3 === 0);
arr.slice(a, b);
arr.slice(a).filter((x, idx) => idx % b === 0);
arr.slice(2).filter((x, idx) => idx % 3 === 0);